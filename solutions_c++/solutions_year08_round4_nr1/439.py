#include<stdio.h>
#include<stdlib.h>
#include<memory.h>
#include<string.h>

struct node_t {
    int g,c;
    int v,t;
};

int M, V;
node_t node[20000];

int calculate(int rt) {
    if ( node[rt].t == 0 ) {
        if ( node[rt].g == 1 )
            return node[rt].v=(calculate(rt*2+1) & calculate(rt*2+2));
        else
            return node[rt].v=(calculate(rt*2+1) | calculate(rt*2+2));
    }
    else {
        return node[rt].v;
    }
}
int const inf = (1<<20);
int change(int rt, int v) {
    if ( node[rt].v == v ) {
        return 0;
    }
    if ( node[rt].t == 1) {
        return -1;
    }
    int lc1 = change(rt*2+1, 1);
    int lc0 = change(rt*2+1, 0);
    int rc1 = change(rt*2+2, 1);
    int rc0 = change(rt*2+2, 0);
    int res = inf;
    int res1 = inf;
    int res0 = inf;
    
        if ( v == 1 ) {
            if ( lc1 != -1 && rc1 != -1 ) {
                res1 = lc1 + rc1;
            }
        }
        else {
            if ( lc0 != -1 ) {
                res1 <?= lc0;
            }
            if ( rc0 != -1 ) {
                res1 <?= rc0;
            }
        }

        if ( v == 1 ) {
            if ( lc1 != -1 ) {
                res0 <?= lc1;
            }
            if ( rc1 != -1 ) {
                res0 <?= rc1;
            }
        }
        else {
            if ( lc0 != -1 && rc0 != -1 ) {
                res0 = lc0 + rc0;
            }
        }
        
    if ( res1 != inf ) {
        if ( node[rt].g == 1 )
            res <?= res1;
        else if ( node[rt].c == 1 )
            res <?= res1+1;
    }
    
    if ( res0 != inf ) {
        if ( node[rt].g == 0 )
            res <?= res0;
        else  if ( node[rt].c == 1 )
            res <?= res0+1;
    }
    
  //  printf("rt%d v%d res%d res0%d res1%d\n", rt, v, res, res0, res1);
    
    if ( res == inf )
        return -1;
    else
        return res;
}

int main(int argc, char *argv[]) {
    freopen("A-large.in", "r", stdin);
    freopen("a-large.out", "w", stdout);
    int N;
    scanf("%d", &N);
    for ( int nc = 1 ; nc <= N ; ++nc ) {
        scanf("%d%d", &M, &V);
        for ( int i = 0 ; i < (M-1)/2 ; ++i ) {
            node[i].t = 0;
            scanf("%d%d", &node[i].g, &node[i].c);
        }
        for ( int i = (M-1)/2 ; i < M ; ++i ) {
            node[i].t = 1;
            scanf("%d", &node[i].v);
        }
        
        // output
        printf("Case #%d: ", nc);
        if ( V == calculate(0) ) {
            printf("0\n");
        }
        else {
            int tmp = change(0, V);
            if ( tmp == -1 ) {
                printf("IMPOSSIBLE\n");
            }
            else {
                printf("%d\n", tmp);
            }
        }
    }
    
    return 0;
}

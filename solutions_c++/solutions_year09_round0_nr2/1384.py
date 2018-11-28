#include<stdio.h>
#include<string.h>

const int dir[4][2]={
    -1, 0,
    0, -1,
    0, 1,
    1, 0
};

int h, w, tlab;
int hig[128][128], dic[128][128], lab[128][128];
char ans[30];

void input()
{
    int i, j;
    
    scanf("%d%d", &h, &w);
    for(i=0; i<h; i++)
        for(j=0; j<w; j++) scanf("%d", &hig[i][j]);
}

void proce1()
{
    int i, j, k, t, i1, j1;
    
    memset(dic, 0xff, sizeof(dic));
    
    for(i=0; i<h; i++)
        for(j=0; j<w; j++){
            for(t=0; t<4; t++){
                i1=i+dir[t][0];
                j1=j+dir[t][1];
                if(0<=i1 && i1<h && 0<=j1 && j1<w && hig[i1][j1]<hig[i][j]) break;
            }
                        
            for(k=t+1; k<4; k++){
                i1=i+dir[k][0];
                j1=j+dir[k][1];
                if(0<=i1 && i1<h && 0<=j1 && j1<w && hig[i1][j1]<hig[i+dir[t][0]][j+dir[t][1]]) t=k;
            }
            
            if(t<4) dic[i][j]=t;
        }
}

void dfs(int i, int j)
{
    int i1, j1, d;
    
    if(lab[i][j]>=0) return;
    lab[i][j]=tlab;
    
    for(d=0; d<4; d++){
        i1=i+dir[d][0];
        j1=j+dir[d][1];
        if(0<=i1 && i1<h && 0<=j1 && j1<w && dic[i1][j1]+d==3) dfs(i1, j1);
    }
}

void numlab()
{
    int i, j;
    
    memset(lab, 0xff, sizeof(lab));
    
    tlab=0;
    for(i=0; i<h; i++)
        for(j=0; j<w; j++)
            if(dic[i][j]<0){
                dfs(i, j);
                tlab++;    
            }
}

void letlab()
{
    int i, j;
    char ch;
    
    memset(ans, 0xff, sizeof(ans));
    
    ch='a';
    for(i=0; i<h; i++)
        for(j=0; j<w; j++)
            if(ans[lab[i][j]]<0){
                ans[lab[i][j]]=ch;
                ch++;
            }
}

void output()
{
    int i, j;
    
    for(i=0; i<h; i++){
        for(j=0; j<w-1; j++) printf("%c ", ans[lab[i][j]]);
        printf("%c\n", ans[lab[i][w-1]]);
    }
}

int main()
{
    freopen("b.in", "r", stdin);
    freopen("b.out", "w", stdout);
    
    int ct, cc;
    
    scanf("%d", &cc);
    for(ct=1; ct<=cc; ct++){
        printf("Case #%d:\n", ct);
        input();
        proce1();
        numlab();
        letlab();
        output();
    }
    
    return 0;
}

//c.cpp
#include <stdio.h>

#define MAXN 30

int iCase;

bool arr[MAXN];
int res[MAXN];

void init();
void dfs(int cur,int s);
int isPure(int n);

int main(){

    scanf("%d",&iCase);

    init();

    for(int i=0;i<iCase;++i){
        int n;
        scanf("%d",&n);
        printf("Case #%d: %d\n",i+1,res[n]);
    }
    return 0;
}

void init(){
    for(int i=0;i<MAXN;++i){
        arr[i]=0;
        res[i]=0;
    }

    int start=2;
    int end = 26;
    for(int i=start;i<end;++i){
        dfs(2,i);
    }

/*
    for(int i=start;i<end;++i){
        printf("%d: %d\n",i, res[i]);
    }*/

}

void dfs(int cur,int s){
    if(cur>=s){
        //find if s is pure
        arr[cur]=1;
        if(isPure(s)){
            ++res[s];
            res[s] %= 100003;
        }

    } else {
        arr[cur]=0;
        dfs(cur+1,s);
        arr[cur]=1;
        dfs(cur+1,s);
    }
}

int isPure(int n){
    int newarr[MAXN],index=0;
    for(int i=2;i<=n;++i){
        if(arr[i]==1){
            newarr[++index]=i;
        }
    }

    int size=index;

    int i;

    while(index!=1){
        for(i=1;i<=size;++i){
            if(newarr[i]==index){
                index = i;
                break;
            }
        }
        if(i>size) return false;
    }

/*
    printf("---------------------");
    for(int i=2;i<=n;++i){
        if(arr[i]==1)
            printf("%d ",i);
    }
    printf("\n");*/
    return true;
}

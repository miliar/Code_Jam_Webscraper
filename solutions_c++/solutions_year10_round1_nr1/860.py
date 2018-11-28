#include <stdio.h>

char g[52][52];
char v[52][52];

void input(int n){
    int i;
    for(i=0;i!=n;++i)gets(g[i]);
}

int move[4][2][51];

void make_move(int k){
    for(int i=0;i!=k;++i){
        move[0][0][i]=0;
        move[0][1][i]=i;
        move[1][0][i]=i;
        move[1][1][i]=0;
        move[2][0][i]=i;
        move[2][1][i]=i;
        move[3][0][i]=i;
        move[3][1][i]=-i;
    }
    
}    
int search(char t, int n, int k){
    int i,j, a,b,ti,tj;
    bool ret=1;
    for(i=0;i!=n;++i){
        for(j=0;j!=n;++j){
            for(a=0;a!=4;++a){
                for(b=0;b!=k;++b){
                    ti=i+move[a][0][b];
                    tj=j+move[a][1][b];
                    if(ti>=n||tj>=n||ti<0||tj<0 ||v[ti][tj]!=t){
                        ret=0;
                        break;
                    }
                    else ret=1;                    
                }
                if(ret)
                {
                    //printf("(<%d,%d>=><%d,%d>)\n",i,j,a,b);
                    return 1;
                }
            }        
        }
    }
    return false;
}
void solve(){
    int n,k, i,j,t;
    char delt[25];
    scanf("%d%d",&n,&k);gets(delt);    
    input(n);
    
    for(i=0;i!=n;++i)for(j=0;j!=n;++j)v[i][j]='.';
    for(i=0;i!=n;++i){
        for(j=n-1,t=n-1;j>=0;--j)if(g[i][j]!='.'){
            v[i][t--]=g[i][j];
        }
    }
    
    //for(i=0;i!=n;++i)puts(v[i]);
    make_move(k);
    //for(i=0;i!=4;++i){for(j=0;j!=k;++j)printf("(%d,%d)",move[i][0][j],move[i][1][j]);puts("");};
    i=search('R',n,k);
    j=search('B',n,k);
    
    if(i&&j)puts("Both");
    else if(i) puts("Red");
    else if(j) puts("Blue");
    else puts("Neither");
}


int main(){
    int cases,i;
    scanf("%d",&cases);
    for(i=1;i<=cases;++i){   
        printf("Case #%d: ",i);
        solve();
    }
    return 0;
}

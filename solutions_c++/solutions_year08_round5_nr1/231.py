#include<stdio.h>
#include<memory>
#include<stdlib.h>
#include<algorithm>
using namespace std;
#define  oo 2100000000
#define  l(A) (A<<1)
#define  r(A) ((A<<1)+1)
using namespace std;
const int N = 102;
char str[100];
int dx[] = {0,-2,0,2},dy[] = {2,0,-2,0},dd = 0,nx,ny,col[4*N][4*N],row[4*N][4*N],colsum[4*N],rowsum[4*N];
bool vis[4*N][4*N];

int lowbit(int x){return x&-x;}
void add(int i,int v, int *a){for(;i<4*N;i+=lowbit(i))a[i]+=v;}
int sum(int i, int *a){int ans=0;for(;i>0;i-=lowbit(i))ans+=a[i];return ans+a[0];}

int main()
{
    int i, j, k, t, T, n, ans;
    int num, tmp;
    int times;
    scanf("%d", &T);
    //freopen("A-small-attempt0.in","r",stdin);
    freopen("A-small-.out","w",stdout);
    for (t=1;t<=T;t++){
        ans=0;
        memset(row,0,sizeof(row));
        memset(col,0,sizeof(col));
        memset(rowsum,0,sizeof(rowsum));
        memset(colsum,0,sizeof(colsum));       
        scanf("%d",&n);
        nx=N*2;ny=N*2;
        for (i=0;i<n;i++){
            scanf("%s%d", str, &times);
            while (times--){
                for (j=0;str[j];j++){
                    if (str[j]=='L'){
                        dd++;
                        if (dd==4) dd=0;
                        if (dd==-1) dd=3;
                        continue;
                    }    
                    else if (str[j]=='R'){
                        dd--;
                        if (dd==4) dd=0;
                        if (dd==-1) dd=3;
                        continue;
                    }    
                    if (dx[dd]==0){
                        add(nx, 1, col[ny + dy[dd]/2]);
                        colsum[ny + dy[dd]/2]++;
                    }    
                    else{
                        add(ny, 1, row[nx + dx[dd]/2]);
                        rowsum[nx + dx[dd]/2]++;
                    }    
                    nx += dx[dd];
                    ny += dy[dd];
                }    
            }    
        }
        for (i=1,num=0;i<4*N;i+=2){
            for (j=1;j<4*N;j+=2){
                tmp=sum(j, row[i]);
                if (tmp>0 && tmp % 2==0 && tmp<rowsum[i]){
                    ans++;
                    continue;
                }  
                tmp=sum(i, col[j]);
                if (tmp>0 &&tmp % 2==0 && tmp<colsum[j]){
                    ans++;
                    continue;
                }   
            }
        }    
        printf("Case #%d: %d\n", t, ans);
    }   
    return 0;
}    


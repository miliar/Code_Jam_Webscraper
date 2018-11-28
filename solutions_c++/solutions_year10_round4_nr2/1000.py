#include<stdio.h>
#include<string.h>
#include<memory.h>

int f[12][(1<<10) + 1];
int num[12][(1<<10) + 1];
int choose[(1<<11)];
int p;
int t;
int main(){
    freopen("B-small-attempt2.in","r",stdin);
    freopen("bout.txt","w",stdout);
    scanf("%d",&t);
    //printf("t %d\n",t);
    int ccount = 0;
    while(t--){
        //printf("t %d\n",t);
        scanf("%d",&p);
        //printf("p %d\n",p);
        for(int i=0;i<(1<<p);i++){
            int u;
            scanf("%d",&u);
            choose[i] = p - u;
        }

        //printf("-t %d\n",t);
        for(int i=1;i<=p;i++)
           for(int j=0;j<(1<<(p-i));j++)
              scanf("%d",&num[i][j]);
        //printf("t %d\n",t);
        memset(f,0,sizeof(f));
        for(int i=0;i<(1<<p);i++){
            for(int j=0;j<choose[i];j++){
                f[p-j][i/(1<<(p-j))] = 1;
            }
        }
        //printf("t %d\n",t);
        int ans = 0;
        for(int i=1;i<=p;i++)
           for(int j=0;j<(1<<p);j++)
              if(f[i][j]==1)  ans++;
        printf("Case #%d: %d\n",++ccount,ans);

        //printf("t %d\n",t);
    }

    return 0;
}


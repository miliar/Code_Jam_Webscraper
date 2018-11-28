#include<cstdio>
#include<algorithm>
#include<cstring>
#define fo(i,u,d) for(int i=u;i<=d;i++)
using namespace std;
struct queue{
    int x,y;
};
const int inf=100000000;
int D,I,M,n;
int a[200];
int best[200][300];
bool hash[200][300];
queue q[1200000];
int now[1200000];
bool use[200][300];
void init(){
    scanf("%d%d%d%d",&D,&I,&M,&n);
    fo(i,1,n)scanf("%d",&a[i]);
}

void work(){
    int f=0;
    int r=0;
    fo(i,1,n)
        fo(j,0,255)best[i][j]=inf;
    memset(use,0,sizeof(use));
    fo(i,1,n){
        fo(j,0,255){
            r++;
            r=r&((1<<20)-1);
            q[r].x=i;
            q[r].y=j;
            now[r]=(i-1)*D+abs(j-a[i]);
            best[i][j]=now[r];
            use[i][j]=1;
        }
    }
    do{
        f++;
        f=f&((1<<20)-1);
        use[q[f].x][q[f].y]=0;
        //if (now[f]!=best[q[f].x][q[f].y])continue;
        if ((q[f].x==2)&&(q[f].y==0)){
            bool find=1;
        }
        //change
        if (q[f].x<n){
            fo(i,0,255)
                if (abs(i-q[f].y)<=M)
                    if (best[q[f].x][q[f].y]+abs(i-a[q[f].x+1])<best[q[f].x+1][i]){
                        if (!use[q[f].x+1][i]){
                        r++;
                        r=r&((1<<20)-1);
                        q[r].x=q[f].x+1;
                        q[r].y=i;
                        now[r]=now[f]+abs(i-a[q[f].x+1]);
                        use[q[f].x+1][i]=1;
                        }
                        best[q[f].x+1][i]=best[q[f].x][q[f].y]+abs(i-a[q[f].x+1]);
                    }
        }

        //add
        fo(i,0,255)
            if (abs(i-q[f].y)<=M)
                if (best[q[f].x][q[f].y]+I<best[q[f].x][i]){
                    if (!use[q[f].x][i]){
                    r++;
                    r=r&((1<<20)-1);
                    q[r].x=q[f].x;
                    q[r].y=i;
                    now[r]=now[f]+I;
                    use[q[f].x][i]=1;
                    }
                    best[q[f].x][i]=best[q[f].x][q[f].y]+I;
                }
        //delete
        if (q[f].x<n)
            if (best[q[f].x][q[f].y]+D<best[q[f].x+1][q[f].y]){
                if (!use[q[f].x+1][q[f].y]){
                r++;
                r=r&((1<<20)-1);
                q[r].x=q[f].x+1;
                q[r].y=q[f].y;
                now[r]=now[f]+D;
                use[q[f].x+1][q[f].y]=1;
                }
                best[q[f].x+1][q[f].y]=best[q[f].x][q[f].y]+D;
            }
    }while (f!=r);
    int ans=inf;
    fo(i,0,255)if (best[n][i]<ans)ans=best[n][i];
    printf("%d\n",ans);
}

int main(){
    freopen("bb.in","r",stdin);
    freopen("bb.out","w",stdout);
    int ca;
    scanf("%d",&ca);
    fo(i,1,ca){
        init();
        printf("Case #%d: ",i);
        work();
    }
    return 0;
}

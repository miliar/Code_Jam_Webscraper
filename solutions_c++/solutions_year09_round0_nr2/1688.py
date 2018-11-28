#include <stdio.h>
#include <string.h>
#define maxn 100+5
const int mx[4]={-1,0,0,1};
const int my[4]={0,-1,1,0};
int a[maxn][maxn],t[maxn][maxn],b[maxn][maxn];
int q[maxn*maxn*2][2];
int f[maxn];
int n,m,sn;
int tn,l;
int move (int x,int y,int k){
    x=x+mx[k];
    y=y+my[k];
    if (x<0 || x>=n || y<0 || y>=m) return 0;else return 1;
}
int sink(int x,int y){
    for (int i=0;i<4;i++)
        if (move(x,y,i) && a[x+mx[i]][y+my[i]]<a[x][y]) return 0;
    return 1;
}
void flood(int x,int y){
     int i,p,qn;
     qn=1;
     q[0][0]=x;q[0][1]=y;
     t[x][y]=sn;
     for (p=0;p<qn;p++)
         for (i=0;i<4;i++)
             if (move(q[p][0],q[p][1],i) && b[q[p][0]+mx[i]][q[p][1]+my[i]]==3-i){
                if (t[q[p][0]+mx[i]][q[p][1]+my[i]]==-1){
                   q[qn][0]=q[p][0]+mx[i];
                   q[qn][1]=q[p][1]+my[i];
                   t[q[qn][0]][q[qn][1]]=sn;
                   qn++;
                }
             }
             
}
int main(){
    int i,j,k;
    freopen("B-small-attempt0.in","r",stdin);
    freopen("b.out","w",stdout);
    for (scanf("%d",&tn),l=1;l<=tn;l++){
        scanf("%d %d",&n,&m);
        for (i=0;i<n;i++)
            for (j=0;j<m;j++) scanf("%d",&a[i][j]);
        memset(t,-1,sizeof(t));
        sn=0;
        memset(b,-1,sizeof(b));
        for (i=0;i<n;i++)
            for (j=0;j<m;j++){
                int minn=a[i][j];
                for (k=0;k<4;k++)
                    if (move(i,j,k) && a[i+mx[k]][j+my[k]]<minn){
                       minn=a[i+mx[k]][j+my[k]];
                       b[i][j]=k;
                    }
            }
        for (i=0;i<n;i++)
            for (j=0;j<m;j++)
                if (t[i][j]==-1 && sink(i,j)){
                   flood(i,j);      
                   sn++;
                }
        k=0;
        memset(f,-1,sizeof(f));
        for (i=0;i<n;i++)
            for (j=0;j<m;j++)
                if (f[t[i][j]]==-1) f[t[i][j]]=k++;
        printf("Case #%d:\n",l);
        for (i=0;i<n;i++){
            for (j=0;j<m;j++) printf("%c ",f[t[i][j]]+'a');
            printf("\n");
        }
    }
    fclose(stdin);
    fclose(stdout);
    return 0;
}

#include<cstdio>
#include<cstring>
#define L 510

using namespace std;

typedef int matrix[L][L];

int sum(matrix a, int x1,int x2,int y1,int y2){
    return a[x2][y2]+a[x1][y1]-a[x1][y2]-a[x2][y1];
}

int T,n,m,i,j,k,I=0;
matrix a,masx,masy,smasx,smasy,sa;
char ch;
int ans;
int tempa,tempmasx,tempmasy,cx,cy;

int main(){
    scanf("%d",&T);
    while (T--){
        scanf("%d%d%*d",&n,&m);
        for (i=1;i<=n;++i)
            for (j=1;j<=m;++j){
                scanf(" %c",&ch);
                a[i][j]=ch-'0';
                masx[i][j]=(ch-'0')*i*2;
                masy[i][j]=(ch-'0')*j*2;
            }
        memset(sa,0,sizeof sa);
        memset(smasx,0,sizeof smasx);
        memset(smasy,0,sizeof smasy);
        for (i=1;i<=n;++i)
            for (j=1;j<=m;++j){
                sa[i][j]=sa[i][j-1]+a[i][j];
                smasx[i][j]=smasx[i][j-1]+masx[i][j];
                smasy[i][j]=smasy[i][j-1]+masy[i][j];
            }
        for (i=1;i<=n;++i)
            for (j=1;j<=m;++j){
                sa[i][j]+=sa[i-1][j];
                smasx[i][j]+=smasx[i-1][j];
                smasy[i][j]+=smasy[i-1][j];
            }
        ans=2;
        for (i=1;i<=n;++i)
            for (j=1;j<=m;++j)
                for (k=ans+1;i>=k && j>=k;k++){
                    tempa=sum(sa,i-k,i,j-k,j);
                    tempmasx=sum(smasx,i-k,i,j-k,j);
                    tempmasy=sum(smasy,i-k,i,j-k,j);
                    tempa-=a[i][j]+a[i-k+1][j]+a[i][j-k+1]+a[i-k+1][j-k+1];
                    tempmasx-=masx[i][j]+masx[i-k+1][j]+masx[i][j-k+1]+masx[i-k+1][j-k+1];
                    tempmasy-=masy[i][j]+masy[i-k+1][j]+masy[i][j-k+1]+masy[i-k+1][j-k+1];
                    cx=i*2-k+1;
                    cy=j*2-k+1;
                    if (tempa*cx==tempmasx && tempa*cy==tempmasy){
                        ans=k;
                    }
                }
        printf("Case #%d: ",++I);
        if (ans<3)
            puts("IMPOSSIBLE");
        else printf("%d\n",ans);
    }
}

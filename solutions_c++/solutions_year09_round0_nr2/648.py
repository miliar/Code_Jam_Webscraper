#include<cstdio>
#include<vector>
#include<algorithm>
#define MAXN 128
using namespace std;
int A[MAXN][MAXN],T;
int dx[]={-1,0,0,1},dy[]={0,-1,1,0};
pair<int,int> sink[MAXN][MAXN];
int main()
{
    int i,j,k,l;
    int ib,jb;
    int H,W;
    scanf("%d",&T);
    for(k=0;k<T;++k)
    {
        char E[MAXN][MAXN];
        scanf("%d %d",&H,&W);
        for(i=0;i<H;++i)
            for(j=0;j<W;++j)scanf("%d",&A[i][j]);
        for(i=0;i<H;++i)
            for(j=0;j<W;++j)
            {
                ib=i;jb=j;
                while(1)
                {
                    int lowest=INT_MAX,x,y;
                    for(l=0;l<4;++l)
                    {
                        x=i+dx[l];y=j+dy[l];
                        if(x<0||x>=H||y<0||y>=W||A[x][y]>=A[i][j])continue;
                        lowest=min(lowest,A[x][y]);
                    }
                    if(lowest==INT_MAX)
                    {
                        sink[ib][jb]=make_pair(i,j);
                        break;
                    }
                    for(l=0;l<4;++l)
                    {
                        x=i+dx[l];y=j+dy[l];
                        if(x<0||x>=H||y<0||y>=W||A[x][y]>=A[i][j])continue;
                        if(lowest==A[x][y])break;
                    }
                    i=x;j=y;
                }
                i=ib;j=jb;
            }
        /*for(i=0;i<H;++i,printf("\n"))
            for(j=0;j<W;++j)printf("%d %d; ",sink[i][j].first,sink[i][j].second);
        printf("===========\n");*/
        printf("Case #%d:\n",k+1);
        for(i=0;i<H;++i)
            for(j=0;j<W;++j)E[i][j]='U';
        char let='a';
        for(i=0;i<H;++i,printf("\n"))
            for(j=0;j<W;++j)
            {
                if(E[sink[i][j].first][sink[i][j].second]=='U')
                {
                    printf("%c",let);
                    E[sink[i][j].first][sink[i][j].second]=let++;
                }
                else printf("%c",E[sink[i][j].first][sink[i][j].second]);
                if(j!=W-1)printf(" ");
            }
    }
    return 0;
}

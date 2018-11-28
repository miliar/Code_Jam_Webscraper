#include <iostream>
#include <algorithm>
using namespace std;
int n;
bool init(int x,int y){return x>=0&&x<n&&y>=0&&y<n;}
int main()
{
    freopen("a.in","r",stdin);
    freopen("a.out","w",stdout);
    int dx[3]={-1,-1,0};
    int dy[3]={-1,0,-1};
	int T,k;
	char a[60][60],b[60][60];
	int re[60][60][3];
	int bl[60][60][3];
	scanf("%d",&T);
	for(int cas=1;cas<=T;cas++)
	{
	    scanf("%d %d",&n,&k);
	    for(int i=0;i<n;i++)
	    {
	        for(int j=0;j<n;j++)
	        {
	            scanf(" %c",&a[i][j]);
	            b[i][j]='.';
            }
        }
        for(int i=n-1;i>=0;i--)
        {
            int num=0;
            for(int j=n-1;j>=0;j--)
            {
                if(a[i][j]!='.')
                {
                    b[n-1-num][n-i-1]=a[i][j];
                    num++;
                }
            }
        }
//        for(int i=0;i<n;i++)
//        {
//            for(int j=0;j<n;j++)
//            {
//               // printf("%c",b[i][j]);
//            }
//           // putchar('\n');
//        }
        memset(re,0,sizeof(re));
        memset(bl,0,sizeof(bl));
        bool v1=false;
        bool v2=false;
        int max1=0;
        int max2=0;
        for(int i=0;i<n;i++)
        {
            for(int j=0;j<n;j++)
            {
                if(b[i][j]!='.')
                {
                    if(b[i][j]=='R')
                    {
                        for(int k=0;k<3;k++)
                        {
                            int tx=i+dx[k],ty=j+dy[k];
                            if(!init(tx,ty))
                            bl[i][j][k]=1;
                            else
                            bl[i][j][k]=bl[tx][ty][k]+1;
                            max1=max(max1,bl[i][j][k]);
                        }
                    }
                    else
                    {
                        for(int k=0;k<3;k++)
                        {
                            int tx=i+dx[k],ty=j+dy[k];
                            if(!init(tx,ty))
                            re[i][j][k]=1;
                            re[i][j][k]=re[tx][ty][k]+1;
                            max2=max(max2,re[i][j][k]);
                        }
                    }
                }
            }
        }
        if(max1>=k)
        v1=true;
        if(max2>=k)
        v2=true;
        printf("Case #%d: ",cas);
        if(v1&&v2)
        printf("Both\n");
        else if(v1)
        printf("Red\n");
        else if(v2)
        printf("Blue\n");
        else
        printf("Neither\n");
    }
	return 0;
}

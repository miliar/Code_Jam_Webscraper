#include <vector> 
#include <list> 
#include <map> 
#include <set> 
#include <deque> 
#include <queue> 
#include <stack> 
#include <bitset> 
#include <algorithm> 
#include <functional> 
#include <numeric> 
#include <utility> 
#include <sstream> 
#include <iostream> 
#include <iomanip> 
#include <cstdio> 
#include <cmath> 
#include <cstdlib> 
#include <cctype> 
#include <string> 
#include <cstring> 
#include <ctime> 

using namespace std;

int neigh[4][2]={{0,1},{1,1},{1,0},{1,-1}};
char a[100][100];
char b[100][100];


int main()
{
    int i,j,k,n,l,t,o,x,y,x1,y1,red,blue;
    freopen("A-large.in","r",stdin);
    freopen("A-large.out","w",stdout);
    scanf("%d",&t);
    for (l=0;l<t;l++)
    {
        scanf("%d%d",&n,&k);
        for (i=0;i<n;i++)
            scanf("%s",a[i]);
        for (i=0;i<n;i++)
            for (j=0;j<n;j++)
                b[i][j]=a[n-1-j][i];
        for (i=0;i<n;i++)
        {
            o=n-1;
            for (j=n-1;j>=0;j--)
            {
                if (b[j][i]!='.')
                {
                    b[o][i]=b[j][i];
                    o--;
                }
            }
            for (;o>=0;o--)
                b[o][i]='.';
        }
        red=0;blue=0;
        for (i=0;i<n;i++)
            for (j=0;j<n;j++)
                if (b[i][j]!='.')
                for (o=0;o<4;o++)
                {
                    x=i;y=j;
                    while ((x>=0)&&(x<n)&&(y>=0)&&(y<n)&&(b[x][y]==b[i][j]))
                    {
                        x+=neigh[o][0];
                        y+=neigh[o][1];
                    }
                    x1=i;y1=j;
                    while ((x1>=0)&&(x1<n)&&(y1>=0)&&(y1<n)&&(b[x1][y1]==b[i][j]))
                    {
                        x1-=neigh[o][0];
                        y1-=neigh[o][1];
                    }
                    if ((abs(x-x1)-1>=k)||(abs(y-y1)-1>=k))
                    {
                        if (b[i][j]=='R')
                            red=1;
                        if (b[i][j]=='B')
                            blue=1;
                    }
                }
        printf("Case #%d: ",l+1);
        if ((red==1)&&(blue==1))
            printf("Both");
        else if (red==1)
            printf("Red");
        else if (blue==1)
            printf("Blue");
        else printf("Neither");
        printf("\n");
    }
	return 0;
}


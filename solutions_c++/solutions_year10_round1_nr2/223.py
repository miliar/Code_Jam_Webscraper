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

int a[300];
int d[300][300];
int aa[300][300];

int main()
{
    int i,j,k,o,dd,ii,m,n,best,diff,t,l;
    freopen("B-large.in","r",stdin);
    freopen("B-large.out","w",stdout);
    scanf("%d",&t);
    for (l=0;l<t;l++)
    {
        scanf("%d%d%d%d",&dd,&ii,&m,&n);
        for (i=0;i<n;i++)
            scanf("%d",&a[i]);
        for (o=0;o<=256;o++)
            for (i=0;i+o<256;i++)
            {
                j=i+o;
                if (abs(i-j)<=m)
                {
                    aa[i][j]=0;
                    aa[j][i]=0;
                    continue;
                }
                aa[i][j]=2000000000;
                for (k=0;k<256;k++)
                    if (((k>i)&&(k<j))||((k>j)&&(k<i)))
                        if ((aa[i][k]!=2000000000)&&(aa[k][j]!=2000000000))
                        if (aa[i][k]+aa[k][j]+ii<aa[i][j])
                            aa[i][j]=aa[i][k]+aa[k][j]+ii;
                aa[j][i]=aa[i][j];
            }
        for (i=0;i<=256;i++)
        {
            aa[i][256]=0;
            aa[256][i]=0;
        }
        for (i=0;i<=n;i++)
            for (j=0;j<=256;j++)
                d[i][j]=2000000000;
        d[0][256]=0;
        for (i=0;i<n;i++)
        {
            for (j=0;j<=256;j++)
                if (d[i][j]!=2000000000)
                {
                    if (d[i][j]+dd<d[i+1][j])
                        d[i+1][j]=d[i][j]+dd;
                    for (k=0;k<256;k++)
                    {
                        diff=aa[j][k]+abs(k-a[i]);
                        if (diff!=2000000000)
                        if (d[i][j]+diff<d[i+1][k])
                            d[i+1][k]=d[i][j]+diff;
                    }
                }
        }
        best=2000000000;
        for (i=0;i<=256;i++)
            if (d[n][i]<best)
                best=d[n][i];
        printf("Case #%d: %d\n",l+1,best);
    }
	return 0;
}


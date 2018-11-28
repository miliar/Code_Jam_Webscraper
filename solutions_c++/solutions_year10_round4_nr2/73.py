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

int p[5000];
int m[5000];
int d[11][5000];

int main()
{
    freopen("B-large.in","r",stdin);
    freopen("B-large.out","w",stdout);
    int i,j,l,t,n,tmp,canm,k,best,mi;
    scanf("%d",&t);
    for (l=0;l<t;l++)
    {
        scanf("%d",&n);
        for (i=(1<<n)-1;i>=0;i--)
            scanf("%d",&m[i]);
        for (i=(1<<n)-2;i>=0;i--)
        {
            scanf("%d",&p[i]);
        }
        memset(d,-1,sizeof(d));
        for (i=(1<<n)-2;i>=0;i--)
        {
            if (i*2+1<(1<<n)-1)
            {
                tmp=i*2+1;
                for (j=0;j<=10;j++)
                    if (d[j][tmp]!=-1)
                        for (k=0;k<=10;k++)
                            if (d[k][tmp+1]!=-1)
                            {
                                mi=j;
                                if (k<mi) mi=k;
                                if ((d[mi][i]==-1)||(d[mi][i]>d[j][tmp]+d[k][tmp+1]+p[i]))
                                    d[mi][i]=d[j][tmp]+d[k][tmp+1]+p[i];
                                if (mi>0)
                                    if ((d[mi-1][i]==-1)||(d[mi-1][i]>d[j][tmp]+d[k][tmp+1]))
                                        d[mi-1][i]=d[j][tmp]+d[k][tmp+1];
                            }
            }
            else
            {
                tmp=i*2+1-((1<<n)-1);
                canm=m[tmp];
                if (m[tmp+1]<canm) canm=m[tmp+1];
                d[canm][i]=p[i];
                if (canm>0)
                {
                    d[canm-1][i]=0;
                }
            }
        }
        best=2000000000;
        for (i=0;i<=10;i++)
            if ((d[i][0]!=-1)&&(d[i][0]<best))
                best=d[i][0];
        printf("Case #%d: %d\n",l+1,best);
    }
	return 0;
}


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

int a[200][200];

int main()
{
    freopen("C-small-attempt0.in","r",stdin);
    freopen("C-small-attempt0.out","w",stdout);
    int i,j,k,l,t,tt,n,cnt,x1,y1,x2,y2;
    scanf("%d",&t);
    for (l=0;l<t;l++)
    {
        memset(a,0,sizeof(a));
        scanf("%d",&n);
        for (i=0;i<n;i++)
        {
            scanf("%d%d%d%d",&x1,&y1,&x2,&y2);
            for (j=x1;j<=x2;j++)
                for (k=y1;k<=y2;k++)
                    a[j][k]=1;
        }
        tt=0;
        cnt=1;
        while (cnt>0)
        {
            tt++;
            cnt=0;
            for (i=100;i>=1;i--)
                for (j=100;j>=1;j--)
                {
                    if ((a[i-1][j]==0)&&(a[i][j-1]==0)) a[i][j]=0;
                    if ((a[i-1][j]==1)&&(a[i][j-1]==1)) a[i][j]=1;
                    if (a[i][j]==1) cnt++;
                }

        }
        printf("Case #%d: %d\n",l+1,tt);
    }
	return 0;
}


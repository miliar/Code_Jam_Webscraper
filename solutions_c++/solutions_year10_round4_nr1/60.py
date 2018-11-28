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

int a[1000][1000];

int main()
{
    //freopen("pa.in","r",stdin);
    //freopen("pa.out","w",stdout);
    freopen("A-large.in","r",stdin);
    freopen("A-large.out","w",stdout);
    int i,j,k,l,t,n,o,p,min1,min2,ma,ans,x,y,b1,m,m1;
    scanf("%d",&t);
    for (l=0;l<t;l++)
    {
        scanf("%d",&n);
        memset(a,-1,sizeof(a)); 
        for (i=0;i<n+n-1;i++)
        {
            if (i+1<=n) m1=n-1-i;
            else m1=i-n+1;
            if (i+1<=n) m=i+1;
            else m=n+n-1-i;
            for (j=m1;j<m1+m+m;j+=2)
                scanf("%d",&a[i][j]);
        }
        min1=2000000000;
        min2=2000000000;
        for (o=0;o<n+n-1;o++)
        {
            b1=1;
            for (i=0;i<n+n-1;i++)
            {
                if (i+1<=n) m1=n-1-i;
                else m1=i-n+1;
                if (i+1<=n) m=i+1;
                else m=n+n-1-i;
                for (j=m1;j<m1+m+m;j+=2)
                {
                    x=o+o-i;
                    y=j;
                    if ((x>=0)&&(x<n+n-1)&&(y>=0)&&(y<n+n-1)&&(a[x][y]!=-1)&&(a[x][y]!=a[i][j]))
                    {
                        b1=0;
                        break;
                    }
                }
                if (b1==0) break;
            }
            if (b1==1)
            {
                ma=o+1;
                if (n+n-2-o+1>ma) ma=n+n-2-o+1;
                if (ma<min1) min1=ma;
            }
        }
        for (o=0;o<n+n-1;o++)
        {
            b1=1;
            for (i=0;i<n+n-1;i++)
            {
                if (i+1<=n) m1=n-1-i;
                else m1=i-n+1;
                if (i+1<=n) m=i+1;
                else m=n+n-1-i;
                for (j=m1;j<m1+m+m;j+=2)
                {
                    x=i;
                    y=o+o-j;
                    if ((x>=0)&&(x<n+n-1)&&(y>=0)&&(y<n+n-1)&&(a[x][y]!=-1)&&(a[x][y]!=a[i][j]))
                    {
                        b1=0;
                        break;
                    }
                }
                if (b1==0) break;
            }
            if (b1==1)
            {
                ma=o+1;
                if (n+n-2-o+1>ma) ma=n+n-2-o+1;
                if (ma<min2) min2=ma;
            }
        }
        ans=min1+min2-n;
        //if (min2<ans) ans=min2;
        //if (ans!=n+n-1)
        //    printf("1\n");
        printf("Case #%d: %d\n",l+1,ans*ans-n*n);
    }
	return 0;
}


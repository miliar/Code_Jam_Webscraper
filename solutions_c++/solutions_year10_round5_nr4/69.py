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

int n,b,ans,remain;
int a[100];
int used[100][100];

void search(int x)
{
    int i,j,tmp,b1,st;
    if (remain==0)
    {
        ans++;
        return;
    }
    if (x==0) st=1;
    else st=a[x-1]+1;
    for (i=st;i<=remain;i++)
    {
        tmp=i;
        b1=1;
        j=0;
        while (tmp>0)
        {
            if (used[j][tmp%b]==1)
            {
                b1=0;break;
            }
            tmp/=b;
            j++;
        }
        if (b1==1)
        {
            tmp=i;j=0;
            while (tmp>0)
            {
                used[j][tmp%b]=1;
                tmp/=b;
                j++;
            }
            remain-=i;
            a[x]=i;
            search(x+1);
            remain+=i;
            tmp=i;j=0;
            while (tmp>0)
            {
                used[j][tmp%b]=0;
                tmp/=b;
                j++;
            }
        }
    }
}

int main()
{
    freopen("D-small-attempt0.in","r",stdin);
    freopen("D-small-attempt0.out","w",stdout);
    int l,t;
    scanf("%d",&t);
    for (l=0;l<t;l++)
    {
        scanf("%d%d",&n,&b);
        memset(used,0,sizeof(used));
        remain=n;
        ans=0;
        search(0);
        printf("Case #%d: %d\n",l+1,ans);
    }
	return 0;
}


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

int getans(int n,int m,int a)
{
	int i,j,i1,j1;
	for (i=0;i<=n;i++)
	{
		if (i*m<a) continue;
		j=(a-1)/i+1;
		i1=i*j-a;
		j1=1;
		printf(" %d %d %d %d %d %d\n",0,0,i,j1,i1,j);
		return 1;
	}
	return 0;
}

int main()
{
	freopen("B-large.in","r",stdin);
	freopen("B-large.out","w",stdout);

	int t,l,n,m,a;
	scanf("%d",&t);
	for (l=0;l<t;l++)
	{
		scanf("%d%d%d",&n,&m,&a);
		printf("Case #%d:",l+1);
		if (getans(n,m,a)==0) printf(" IMPOSSIBLE\n");
	}
	return 0;
}


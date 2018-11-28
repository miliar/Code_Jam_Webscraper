#include <cstdio>
#include <iostream>
#include <string>
#include <sstream>
#include <cstring>
#include <algorithm>
#include <complex>
#include <cmath>
#include <vector>
#include <list>
#include <sstream>
#include <vector>
#include <cstdlib>
#include <set>
#include <map>
#include <ctime>
using namespace std;
int a[2000];
bool h[2000];
int T,casenum,i,j,ans,n,tmp;
void dfs(int cur)
{
	h[cur]=true;
	tmp++;
	if (!h[a[cur]])	dfs(a[cur]);
}
int main()
{
	freopen("problem.in","r",stdin);
	freopen("problem.out","w",stdout);
	cin>>T;
	for (casenum=1;casenum<=T;casenum++)
	{
		cout<<"Case #"<<casenum<<": ";
		cin>>n;
		for (i=1;i<=n;i++)
			cin>>a[i];
		memset(h,0,sizeof(h));
		ans=0;
		for (i=1;i<=n;i++)
		{
			if (h[i]) continue;
			tmp=0;
			dfs(i);
			if (tmp>1) ans+=tmp;
		}
		cout<<ans<<".000000"<<endl;
	}
	return 0;
}

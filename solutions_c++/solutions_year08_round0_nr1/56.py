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

map<string,int> mp;
int used[1000];

int main()
{
	freopen("A-large.in","r",stdin);
	freopen("A-large.out","w",stdout);
	int i,j,m,n,l,t,cnt,ans;
	char s[1000];
	vector<string> a;
	vector<int> b;
	scanf("%d",&t);
	for (l=0;l<t;l++)
	{
		a.clear();b.clear();
		mp.clear();
		scanf("%d",&m);
		gets(s);
		for (i=0;i<m;i++)
		{
			gets(s);
			mp[s]=a.size();
			a.push_back(s);
		}
		scanf("%d",&n);
		gets(s);
		for (i=0;i<n;i++)
		{
			gets(s);
			if (mp.find(s)==mp.end()) b.push_back(-1);
			else b.push_back(mp[s]);	
		}
		memset(used,0,sizeof(used));
		cnt=0;ans=0;
		for (i=0;i<n;i++)
			if (b[i]!=-1)
			{
				if (used[b[i]]==0) cnt++;
				if (cnt==m)
				{
					memset(used,0,sizeof(used));
					cnt=1;
					ans++;
				}
				used[b[i]]=1;
			}
		printf("Case #%d: %d\n",l+1,ans);
	}
	return 0;
}


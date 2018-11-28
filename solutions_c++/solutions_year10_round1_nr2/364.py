#include <iostream>
#include <vector>
#define maxn 700
using namespace std;
int tn,n,del,insert,m;
long long ans;
vector<int> a;

void dfs(int k,int prev,long long tot)
{
	if (k>=n)
	{
		ans=min(ans,tot);
		return;
	}
	if (prev==-1 || abs(a[k]-prev)<=m)
		dfs(k+1,a[k],tot);
	dfs(k+1,prev,tot+del);
	if (m>0 && prev!=-1)
	{
		int t=abs(a[k]-prev)/m;
		if (a[k]!=prev && (a[k]-prev)%m==0) t--;
		dfs(k+1,a[k],tot+insert*t);
	}
	if (prev!=-1)
		for (int i=max(0,prev-m);i<=prev+m;i++)
			dfs(k+1,i,tot+abs(a[k]-i));
	else
		for (int i=0;i<=255;i++)
			dfs(k+1,i,tot+abs(a[k]-i));
}

int main()
{
	freopen("B2-small-attempt1.in","r",stdin);
	freopen("B2_small.out","w",stdout);
	int i,j;
	cin >> tn;
	for (int t=1;t<=tn;t++)
	{
		cin >> del >> insert >> m >> n;
		a.clear();
		ans=2147483647;
		for (i=1;i<=n;i++)
		{
			int tmp;
			cin >> tmp;
			a.push_back(tmp);
		}
		dfs(0,-1,0);
		cout << "Case #" << t << ": " << ans << endl;
	}
}
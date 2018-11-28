#include <iostream>
#include <string>
#include <vector>
using namespace std;

vector <string> a;
int n,m;
string s;
int common(string c, string b)
{
	int ans=0;int i;
	for (i=0; (c[i]==b[i]) && i<min(c.size(),b.size()); i++) if (c[i]=='/') ans++;
	if ( (i==c.size() && i==b.size()) || (i==c.size() && b[i]=='/') || (i==b.size() && c[i]=='/')) ans++;
	ans--;
	return ans;
}
int finds(string b)
{
	int ans=0;
	for (int i=0; i<b.size(); i++) if (b[i]=='/') ans++;
	return ans;
}


int main()
{
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	int T;
	scanf("%d",&T);
	for (int q=1; q<=T; q++)
	{
		a.clear();
		int ans=0;
	cin >> m >> n;
	a.resize(m);
	for (int i=0; i<m; i++) 
		cin >> a[i];
	for (int w=0; w<n; w++)
	{
		cin >> s;
		int buf=finds(s);
		int maxt=0;
		for (int e=0; e<a.size(); e++)
		{
			int t = common (a[e],s);
			if (t>maxt) maxt=t;
		}
		ans+=(buf-maxt);
		if (buf-maxt)
		{
			while (buf>maxt)
			{
				a.push_back(s);
				int j;
				for (j=s.size()-1; s[j]!='/'; j--);
				s.erase(s.begin()+ j,s.end());
				buf--;
			}
		}

	}
	printf("Case #%d: %d\n",q,ans);
	}
	return 0;
}
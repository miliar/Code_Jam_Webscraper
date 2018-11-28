#include <iostream>
#include <algorithm>
#include <cstdio>

using namespace std;

int T,test,ans,n,s,p;
int t[128];

int main()
{
	cin >> T;
	for (int test=1;test<=T;++test)
	{
		cin >> n >> s >> p;
		for (int i=1;i<=n;++i) cin >> t[i];
		sort(t+1,t+n+1);
		ans=0;
		for (int i=n;i;--i)
		{
			if ((t[i]+2)/3>=p) ++ans;
			else if (t[i]!=0 && t[i]!=1 && s)
			{
				if (t[i]%3==0 && t[i]/3+1>=p) { --s; ++ans; }
				if (t[i]%3==1 && t[i]/3+1>=p) { --s; ++ans; }
				if (t[i]%3==2 && t[i]/3+2>=p) { --s; ++ans; }
			}
		}
		cout << "Case #" << test << ": " << ans << endl;
	}
	return 0;
}

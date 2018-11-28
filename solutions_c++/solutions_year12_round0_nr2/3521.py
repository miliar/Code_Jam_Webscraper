#include <iostream>
#include <algorithm>
using namespace std;
const int MAXN=111;
int n,s,p,t[MAXN],tsts;
int main()
{
	cin >> tsts;
	for(int kk=0;kk<tsts;kk++)
	{
		cin >> n >> s >> p;
		for(int i=0;i<n;i++)
			cin >> t[i];
		sort(t,t+n);
		reverse(t,t+n);
		int ans=0;
		int i=0;
		while(s&&t[i]>0&&i<n)
		{
			if(t[i]>=28)
			{
				ans++;
				i++;
				continue;
			}
			if(t[i]%3==1)
			{
				if((t[i]+2)/3>=p)
					ans++;
				i++;
				continue;
			}
			if((t[i]+2)/3>=p)
			{
				i++;
				ans++;
			}
			else
			{
				if((t[i]+2)/3+1>=p)
				{
//					cerr << "ARMIN" << endl;
					s--;
					ans++;
					i++;
				}
				else
					break;
			}
		}
//		cerr << i << endl;
		for(;i<n;i++)
			if((t[i]+2)/3>=p)
				ans++;
		cout << "Case #" << kk+1 << ": " << ans << endl;
	}
	return 0;
}

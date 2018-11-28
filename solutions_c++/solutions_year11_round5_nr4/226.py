#include <iostream>
#include <cstdio>
#include <sstream>
#include <cmath>

using namespace std;

typedef long long ll;

bool issq(ll r)
{
	double c = sqrt(r);
	if(ll(c+0.5) * ll(c+0.5) == r)
		return true;
	return false;
}

int main()
{
	int TC;
	cin >> TC;
	for(int T=1; T<=TC; T++)
	{
		string s;
		cin >> s;

		ll p = 0;
		for(ll i=0; i<s.size(); i++)
			p += s[i] == '?';

		for(ll i=0; i<(1LL<<p); i++)
		{
			ll r = 0;
			string t = s;
			for(ll j=0; j<t.size(); j++)
				if(t[j] == '?')
				{
					t[j] = ((i>>r)&1LL)+'0';
					r++;
				}
//			cout << "# " << t << endl;

			ll pp = 0;
			for(ll i=0; i<t.size(); i++)
				pp = pp*2 + (t[i] - '0');

			if(issq(pp))
			{
				cout << "Case #" << T << ": " << t << endl;
				break;
			}
		}
	}
	return 0;
}


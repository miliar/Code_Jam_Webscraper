#include <iostream>
#include <vector>
#include <string>

#define fii(x,y) for(int i=x;i<y;i++)
#define fjj(x,y) for(int j=x;j<y;j++)
#define fi(x) fii(0,x)
#define fj(x) fjj(0,x)

#define mod 10009

using namespace std;

typedef long long ll;
typedef vector <int> VI;
typedef vector <VI> VVI;
typedef vector <ll> VL;
typedef vector <VL> VVL;
typedef vector <string> VS;

ll res;
string p;
VS dic;
int k,n;
VI resp;

ll eval (VI & let)
{
	ll st=0;
	ll pt=1;
	fi (p.size())
	{
		if (p[i]=='+')
		{
			st+=pt;
			pt=1;
		}
		else
		{
			pt*=let[p[i]-'a'];
		}
		st%=mod;pt%=mod;
	}
	return (st+pt)%mod;
}

ll fact (ll a)
{
	if (a==0)
		return 1LL;
	return a*fact(a-1);
}

void back (int d, int m, int a)
{
	if (d==0)
	{
		VI let(26,0);
		ll fl = fact(m);
		fi (a)
		{
			if (resp[i]==0)
				continue;
			string s=dic[i];
			fj (s.size())
			{
				let[s[j]-'a']+=resp[i];
			}
			fl/=fact(resp[i]);
		}
		res+=fl*eval (let);
		res%=mod;
		return;
	}
	if (a>=n)
		return;
	fi (d+1)
	{
		resp[a]=i;
		back(d-i,m,a+1);
	}
}

int main()
{
	int T;
	cin >> T;
	for (int caso=1;caso<=T;caso++)
	{
		cin >> p >> k >> n;
		dic=VS (n);
		fi (n)
			cin >> dic[i];
		cout << "Case #" << caso << ":";
		for (int d=1;d<=k;d++)
		{
			resp=VI(n,0);
			res = 0;
			back (d,d,0);
			cout << " " << res;
		}
		cout << endl;
	}
}

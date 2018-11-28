#include <iostream>
#include <algorithm>
#include <vector>
#include <cmath>

using namespace std;

#define SZ(a) (ll)(a).size()
#define For(i, a, b) for(ll i=(a); i<(b); ++i)
#define ForD(i, b, a) for(ll i=(b)-1; i>=a; --i)

typedef long long ll;

vector<ll> pr;
ll P;

void Generate(ll st, ll fn)
{
	if (st<2) st=2;
	For(i, st, fn)
	{
		pr.push_back(i);
		For(j, 0, SZ(pr)-1)
			if (i%pr[j]==0) { pr.pop_back(); break; }
			/*
		For(j, 2, (int)sqrt(i*1.0)+1)
			if (j%i==0) { pr.pop_back(); break; }
			*/
	}
}

bool Check(ll n1, ll n2)
{
	ForD(i, SZ(pr), 0)
		if (pr[i]<P) break;
		else
		if (n1%pr[i]==0 && n2%pr[i]==0) return true;
	return false;
}

void main()
{
	int tc;
	cin >> tc;
	Generate(2, 1000);
	For(_case, 1, tc+1)
	{
		ll a, b, p;
		cin >> a >> b >> p;
		P=p;
		ll col[2000];
		For(i, 0, 2000)
			col[i]=i;
		//Generate(2, (int)sqrt(b*1.0)+2);
		//Generate(a, b);
		ll res=b-a+1;
		For(i, a, b+1)
			For(j, i+1, b+1)
				if (col[i]!=col[j] && Check(i, j))
				{
					res--;
					int s1=min(col[i], col[j]), s2=max(col[i], col[j]);
					For(k, a, b+1)
						if (col[k]==s1) col[k]=s2;
				}
		cout << "Case #" << _case << ": " << res << endl;
	}
}
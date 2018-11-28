#include <iostream>
#include <algorithm>
#include <vector>
#include <set>

using namespace std;

#define SZ(a) (int)(a).size()
#define For(i, a, b) for(int i=(a); i<(b); ++i)

typedef long long ll;

int A[9]={00, 01, 02, 10, 11, 12, 20, 21, 22};

void main()
{
	int _n;
	cin >> _n;
	For(_case, 1, _n+1)
	{
		ll n, m, x0, y0, a, b, c, d, x, y;
		cin >> n >> a >> b >> c >> d >> x0 >> y0 >> m;
		x=x0; y=y0;
		ll fl[50];
		For(i, 0, 50) fl[i]=0;
		set< pair<ll, ll> > s; s.clear();
		fl[(x0%3)*10+y%3]++;
		s.insert(make_pair(x, y));
		For(i, 0, n-1)
		{
			x=(a*x%m+b)%m; y=(c*y+d)%m;
			if (s.find(make_pair(x, y))==s.end()) fl[(x%3)*10+y%3]++;
			else s.insert(make_pair(x, y));
		}
		ll res=0;
		For(i1, 0, 9)
			For(i2, i1+1, 9)
				For(i3, i2+1, 9)
					if ((A[i1]/10+A[i2]/10+A[i3]/10)%3==0 && (A[i1]%10+A[i2]%10+A[i3]%10)%3==0)
						res+=fl[A[i1]]*fl[A[i2]]*fl[A[i3]];
		For(i1, 0, 9)
			For(i2, i1+1, 9)
			{
				if ((A[i1]/10+A[i1]/10+A[i2]/10)%3==0 && (A[i1]%10+A[i1]%10+A[i2]%10)%3==0)
					res+=(fl[A[i1]]*(fl[A[i1]]-1)*fl[A[i2]])/2;
			}

		For(i1, 0, 9)
			if ((A[i1]/10+A[i1]/10+A[i1]/10)%3==0 && (A[i1]%10+A[i1]%10+A[i1]%10)%3==0)
				res+=(fl[A[i1]]*(fl[A[i1]]-1)*(fl[A[i1]]-2))/6;

		cout << "Case #" << _case << ": " << res << endl;
	}
}
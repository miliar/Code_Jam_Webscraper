#include <iostream>
#include <algorithm>
#include <vector>

using namespace std;

#define SZ(a) (int)(a).size()
#define For(i, a, b) for(ll i=(a); i<(b); ++i)

typedef long long ll;

ll abs(ll a)
{
	if (a<0) return -a;
	return a;
}

void main()
{
	int tc;
	cin >> tc;
	For(_case, 1, tc+1)
	{
		ll a, n, m;
		cin >> n >> m >> a;
		bool res=false;
		cout << "Case #" << _case << ": ";
		if (n*m<a)
		{
			cout << "IMPOSSIBLE" << endl;
			continue;
		}
		if (n*m==a)
		{
			cout << "0 0 0 " << m << " " << n << " " << m << endl;
			continue;
		}
		ll x1=0, y1=0;
//		For(x1, 0, n+1)
			//For(y1, 0, m+1)
				For(x2, 0, n+1)
					For(y2, 0, m+1)
						For(x3, 0, n+1)
							For(y3, 0, m+1)
							{
								if (abs((x1-x2)*(y1+y2)+(x2-x3)*(y2+y3)+(x3-x1)*(y3+y1))==a)
								{
									cout << x1 << " " << y1 << " " << x2 << " " << y2 << " " << x3 << " " << y3;
									res=true;
									goto end;
								}
							}
end:	if (!res)
			cout << "IMPOSSIBLE";
		cout << endl;
	}
}
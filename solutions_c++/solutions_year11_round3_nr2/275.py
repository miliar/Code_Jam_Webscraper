#include <iostream>
#include <set>
using namespace std;
const int maxn = 1001 * 1003;
const long long INF = 1000000LL * 1000000LL * 1000LL;
long double mas[maxn];
long long f[maxn];
multiset <long double> s;
void init()
{
	for (int i = 0 ; i < maxn; i++)
			f[i] =  0;
	s.clear();
}
void solve(int test)
{
	long long l,n,c;
	long double t;
	cin >> l >> t >> n >> c;
	init();
	for (int i= 0 ; i < c ; i++)
		cin >> mas[i];
	for (int i = 0 ; i < n; i++)
	{
		if (f[i] + mas[i % c] * 2 > t)
			if (t > f[i])
				s.insert(mas[i % c] - (t - f[i]) / 2); 
			else
				s.insert(mas[i % c]);			
		f[i + 1] = mas[i % c] * 2 + f[i];
	}
	long long ans = (f[n] + 0.1);
	while(s.size() >l)
		s.erase(s.begin());
	for (multiset < long double > :: iterator it = s.begin(); it != s.end(); it++)
		ans -=(long long)( (*it) + 0.01);
	cout << "Case #" << test << ": " << (ans) << '\n';
	
}
int main()
{
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	int t;
	cin >> t;
	for (int i = 0 ;i  < t ;i++)
		solve(i + 1);
	return 0;
}
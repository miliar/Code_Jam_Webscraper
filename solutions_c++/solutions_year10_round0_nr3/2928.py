#include <iostream>
#include <string>
#include <vector>

using namespace std;

void Output(const char *str)
{
	static int x = 0;
	x++;
	printf("Case #%d: %s\n", x, str);
}

void Output(long long ans)
{
	static int x = 0;
	x++;
	printf("Case #%d: %lld\n", x, ans);
}

void solve()
{
	long long R, k, N, g; 
	vector <long long> Groups, Euros, Shifts;
	long long all = 0;
	scanf("%d%d%d", &R, &k, &N);
	for(int i = 0; i < N; i++) {
		scanf("%d", &g );
		Groups.push_back( g );
		Euros.push_back( 0 );
		Shifts.push_back( 0 );
		all += g;
	}
	
	for(int i = 0; i < N; i++) {
		Shifts[i] = i;
		Euros[i] = 0;
		while( Euros[i] + Groups[ Shifts[i] ] <= k
			&& Euros[i] + Groups[ Shifts[i] ] <= all ) {
			Euros[i] += Groups[ Shifts[i] ];
			Shifts[i]++;
			Shifts[i] %= N;
		}
	}
	
	long long ans = 0;
	long long s = 0;
	long long r = 0;
	bool bFirst = true;
	while( R-- ) {
		if ( s == 0 && ans != 0 && bFirst ) {
			ans += (R/r)*ans;
			R %= r;
			bFirst = false;
		}
		ans += Euros[s];
		s = Shifts[s];
		r ++;
	}
	
	Output(ans);
}

void GCJ2010_RoundQ_A()
{
	int T;
	scanf("%d", &T);
	while(T--) {
		solve();
	}
}

int main()
{
	GCJ2010_RoundQ_A();
	return 0;
}


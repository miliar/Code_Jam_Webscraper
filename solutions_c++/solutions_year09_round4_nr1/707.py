//Grzegorz Prusak
#include <iostream>

//loops
#define REP(i,n) for(int i=0; i<(n); ++i)
#define FOR(i,p,k) for(int i=(p); i<=(k); ++i)
#define FORD(i,p,k) for(int i=(p); i>=(k); --i)

const int n_max = 40 +5;

int main()
{
	int t; std::cin >> t; FOR(i,1,t)
	{
		int n; std::cin >> n;
		int A[n_max]={}; REP(j,n)
		{
			std::string s; std::cin >> std::ws >> s;
			REP(k,n) if(s[k]=='1') A[j] = k;
		}
		
		int res = 0;
		REP(j,n) FOR(k,j,n-1) if(A[k]<=j)
		{
			int x = A[k];
			FORD(l,k-1,j) A[l+1] = A[l];
			A[j] = x; res += k-j; break;
		}
		
		std::cout << "Case #" << i << ": " << res << "\n";
	}

	return 0;
}


//Grzegorz Prusak: problem "The Next Number"
#include <iostream>
#include <cstring>

//loops
#define REP(i,n)    for(int i=0; i<(n); ++i)
#define FOR(i,p,k)  for(int i=(p); i<=(k); ++i)
#define FORD(i,p,k) for(int i=(p); i>=(k); --i)

const int T_max = 500;
const int N_max = 20 +20;

template<typename T> inline void swap(T &a, T &b){ T c=a; a=b; b=c; }
template<typename T> inline void inverse(T *a, T *b){ while(a<--b){ T c = *a; *(a++) = *b; *b = c; } }

int main()
{
	int T; std::cin >> T; FOR(x,1,T)
	{
		//input
		char A[N_max]; std::cin >> std::ws >> A; //std::cout << "[" << A << "]\n";
		int n = strlen(A);
	
		int l = n-2; while(l>=0 && A[l]>=A[l+1]) l--; //std::cout << "l=" << l << "\n";
		if(l<0)
		{
			int p = n-1; while(A[p]=='0') p--; //std::cout << "p=" << p << "\n";
			inverse(A,A+p+1);
			std::cout << "Case #" << x << ": ";
			std::cout << A[0]; REP(i,n-p) std::cout << 0; FOR(i,1,p) std::cout << A[i]; std::cout << "\n";
			continue;
		}
		int r = n-1; while(A[r]<=A[l]) r--; //std::cout << "r=" << r << "\n";
		swap(A[l],A[r]); inverse(A+l+1,A+n);
		
		//output
		std::cout << "Case #" << x << ": ";
		REP(i,n) std::cout << A[i]; std::cout << "\n";
	}

	return 0;
}


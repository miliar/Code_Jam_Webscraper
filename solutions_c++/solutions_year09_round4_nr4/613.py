//Grzegorz Prusak
#include <iostream>
#include <cmath>
#include <iomanip>

//loops
#define REP(i,n) for(int i=0; i<(n); ++i)
#define FOR(i,p,k) for(int i=(p); i<=(k); ++i)
#define FORD(i,p,k) for(int i=(p); i>=(k); --i)

template<typename T> const T & min(const T &a, const T &b){ return a<b ? a : b; }
template<typename T> const T & max(const T &a, const T &b){ return a>b ? a : b; }

const double inf = 1./0.;

const int n_max = 40 +5;

int X[n_max],Y[n_max],R[n_max];

#define sqr(a) ((a)*(a))

double dist(int a, int b){ return sqrt(sqr(X[a]-X[b])+sqr(Y[a]-Y[b])); }

int main()
{
	int c; std::cin >> c; FOR(x,1,c)
	{
		int n; std::cin >> n;
		REP(i,n) std::cin >> X[i] >> Y[i] >> R[i];
		double res = inf;
		switch(n)
		{
			case 1: res = R[0]; break;
			case 2: res = max(R[0],R[1]); break;
			case 3:
				//std::cout << max<double>(R[0],(R[1]+R[2]+dist(1,2))*0.5) << "\n";
				res = min(res,max<double>(R[0],(R[1]+R[2]+dist(1,2))*0.5));
				res = min(res,max<double>(R[1],(R[2]+R[0]+dist(2,0))*0.5));
				res = min(res,max<double>(R[2],(R[0]+R[1]+dist(0,1))*0.5));
		}
		std::cout << "Case #" << x << ": " << std::fixed << std::setprecision(6) << res << "\n";
	}

	return 0;
}


#include <iostream>
#include <complex>
#include <vector>
using namespace std;
long long ntrees[9];
int main()
{
    int N;
    cin >> N;
    for (int t=0; t<N; ++t) {
	long long n, A, B, C, D, x0, y0, M;
	cin >> n >> A >> B >> C >> D >> x0 >> y0 >> M;
	fill(ntrees, ntrees+9, 0);
	for (int i=0; i<n; ++i) {
	    ++ntrees[(x0%3)*3+y0%3];
	    x0 = (A * x0 + B) % M;
	    y0 = (C * y0 + D) % M;
	}
	long long result = 0;	    
	for (int i=0; i<9; ++i) {
	    int x0 = i/3, y0 = i%3;
	    for (int j=i; j<9; ++j) {
		int x1 = j/3, y1 = j%3;
		for (int k=j; k<9; ++k) {
		    int x2 = k/3, y2 = k%3;
		    if ((x0+x1+x2) % 3 == 0 && (y0+y1+y2) % 3 == 0) {
			if (i == j && j == k) {
			    if (ntrees[i] > 2)
				result += ntrees[i]*(ntrees[i]-1)*(ntrees[i]-2)/6;
			} else if (i == j) {
			    if (i > 1)
				result += ntrees[i]*ntrees[i-1]*ntrees[k]/2;
			} else if (j == k) {
			    if (j > 1)
				result += ntrees[i]*ntrees[j]*ntrees[j-1]/2;
			}
			else result += ntrees[i]*ntrees[j]*ntrees[k];
		    }
		}
	    }
	}
	printf("Case #%d: %lld\n", t+1, result);
	
    }
    
}

#include <algorithm>
#include <fstream>
#include <string>
#include <queue>
#include <set>
#include <stack>
#include <map>
#include <sstream>
#include <iostream>
#include <cmath>
using namespace std;

typedef unsigned int uint;
typedef long long int64;
typedef vector<int> vi;
typedef vector<string> vs;
typedef pair<int,int> pI;
typedef pair<string,int> pSI;
typedef pair<int,string> pIS;

#define FOR(i,n) for(int i=0, upTo##i=n; i<upTo##i; ++i)
#define REVFOR(i,n) for(int i=(n)-1; i>=0; --i)
#define FOR2(i,b,n) for(int i=b; i<(n); ++i)
#define REVFOR2(i,b,n) for(int i=(n)-1; i>=b; --i)
#define SC(i) scanf("%d", i)
#define ALL(C) (C).begin(), (C).end()
#define RALL(C) (C).rbegin(), (C).rend()
#define MIN(C) *min_element(ALL(C))
#define MAX(C) *max_element(ALL(C))
#define A first
#define B second

int N;
int x[40], y[40], r[40];

double Distance(int x1, int x2, int y1, int y2)  {
	double distX = x1-x2;
	double distY = y1-y2;
	return sqrt(static_cast<double>(distX*distX + distY*distY));
}


int main(void) {
    int n; cin>>n;
    FOR(_i,n) {
		cin>>N;
		FOR(i,N) 
		{
			cin>>x[i]>>y[i]>>r[i];
		}

		double res;
		if (N == 3) {
			//01
			double a = max(0.5 * (Distance(x[0],x[1], y[0],y[1]) + r[0] + r[1]), double(r[2]));
			double b = max(0.5 * (Distance(x[0],x[2], y[0],y[2]) + r[0] + r[2]), double(r[1]));
			double c = max(0.5 * (Distance(x[1],x[2], y[1],y[2]) + r[1] + r[2]), double(r[0]));
			res = min(min(a,b), c);

		}
		else if (N==2) {
			res = max(r[0],r[1]);
		} else
			res = r[0];

        printf("Case #%d: %lf\n", _i+1, res);
    }
    return 0;
}

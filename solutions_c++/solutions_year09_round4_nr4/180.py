#include <algorithm>
#include <iostream>
#include <sstream>
#include <string>
#include <vector>
#include <queue>
#include <set>
#include <map>
#include <cstdio>
#include <cstdlib>
#include <cctype>
#include <cmath>

#define SIZE(a) ((int)((a).size()))
#define ALL(a) (a).begin(),(a).end()
#define FILL(a) memset(&a,0,sizeof(a))
#define PB push_back
#define MP make_pair
#define FOR(i,a,b) for (int i = (int)(a); i < (int)(b); ++i)
#define REP(i,a) for (int i = 0; i < (int)(a); ++i)
typedef long long LL;

using namespace std;

int n;
double x[100], y[100], r[100];

double d(int nom1, int nom2){
	double dist = sqrt((x[nom1]-x[nom2])*(x[nom1]-x[nom2]) + (y[nom1]-y[nom2])*(y[nom1]-y[nom2]));
	return (dist + r[nom1] + r[nom2]) / 2.; 
}

int main(){
	freopen("d.in","r",stdin);
	freopen("d.out","w",stdout);
	int tc;
	scanf("%d",&tc);
	REP(it,tc){
		printf("Case #%d: ", it+1);
		scanf("%d", &n);
		REP(i,n){
			cin >> x[i] >> y[i] >> r[i];
		}
		if (n == 1){
			printf("%.6lf\n", r[0]);
		}
		else if (n == 2){
			printf("%.6lf\n", max(r[0], r[1]));
		}
		else if (n == 3){
			double res = 1000000000;
			res *= res;
			res = min(res, max(r[0], d(1, 2)));
			res = min(res, max(r[1], d(0, 2)));
			res = min(res, max(r[2], d(0, 1)));
			printf("%.6lf\n", res);
		}
		else{
			cerr << "WTF O_o" << endl;
		}
	}
}

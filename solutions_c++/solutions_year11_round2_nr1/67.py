//be name oo
#include <cstdio>
#include <iostream>
#include <algorithm>
#include <set>
#include <string>
#include <map>
#include <utility>
#include <cstring>
#include <sstream>
#include <complex>
#include <vector>

#define FOR(i, n) for(int i = 0; i < (n); i++)
#define SZ(x) ((int)x.size())
#define PB push_back
#define F first
#define S second

using namespace std;
typedef pair<int, int> joft;
typedef complex<double> point;

const int MAX_N = 100 + 10;

int n;
char inp[MAX_N][MAX_N];
double sumw[MAX_N], suma[MAX_N];
double owp[MAX_N];
double oowp[MAX_N];

int main(){
	int t;
	scanf("%d", &t);
	for(int test = 1; test <= t; test++){
		scanf("%d", &n);
		memset(sumw, 0, sizeof sumw);
		memset(suma, 0, sizeof suma);
		FOR(i, n){
			scanf(" %s", inp[i]);
			FOR(j, n){
				if(inp[i][j] != '.')
					suma[i]++;
				if(inp[i][j] == '1')
					sumw[i]++;
			}
		}
		FOR(i, n){
			owp[i] = 0;
			FOR(j, n)
				if(inp[i][j] != '.')
					owp[i] += (sumw[j] - (inp[j][i] - '0')) / (suma[j] - 1);
			owp[i] /= suma[i];
		}
		printf("Case #%d:\n", test);
		FOR(i, n){
			oowp[i] = 0;
			FOR(j, n)
				if(inp[i][j] != '.')
					oowp[i] += owp[j];
			oowp[i] /= suma[i];
			double rpi = (sumw[i] / suma[i]) / 4 + owp[i] / 2 + oowp[i] / 4;
			printf("%0.7lf\n", rpi);
		}
	}
	return 0;
}

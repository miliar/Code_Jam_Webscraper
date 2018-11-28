#include <cstdio>
#include <iostream>
#include <vector>
#include <cstring>
#include <string>
#include <stack>
#include <queue>
#include <algorithm>
#include <cctype>
#include <functional>
#include <numeric>
using namespace std;

typedef long long llong;
typedef pair<int, int> PII;

const int N = 128;

char mp[N][N];
int n;

double wp[N], owp[N], oowp[N];

void WP()
{
	for(int i = 0; i < n; i++) {
		int cc = 0, win = 0;
		for(int j = 0; j < n; j++) if(mp[i][j] != '.') {
			cc++;
			if(mp[i][j] == '1') win++;
		}
		wp[i] = 1.0 * win / cc;
	}
}

double getWP(int a, int b)
{
	int cc = 0, win = 0;
	for(int j = 0; j < n; j++) if(mp[a][j] != '.' && j != b) {
		cc++;
		if(mp[a][j] == '1') win++;
	}
	return 1.0 * win / cc;
}

void OWP()
{
	for(int i = 0; i < n; i++) {
		int cc = 0;
		double wpsum = 0;
		for(int j = 0; j < n; j++) if(mp[i][j] != '.') {
			cc++;
			wpsum += getWP(j, i);
		}
		owp[i] = 1.0 * wpsum / cc;
	}
}

void OOWP()
{
	for(int i = 0; i < n; i++) {
		int cc = 0;
		double owpsum = 0;
		for(int j = 0; j < n; j++) if(mp[i][j] != '.') {
			cc++;
			owpsum += owp[j];
		}
		oowp[i] = 1.0 * owpsum / cc;
	}
}

int main()
{
	freopen("E:\\A-large.in", "r", stdin);
	freopen("E:\\Alarge.out", "w", stdout);
	
	int T;
	scanf("%d", &T);
	
	for(int t = 0; t < T; t++) {
		scanf("%d", &n);
		for(int i = 0; i < n; i++) scanf("%s", mp[i]);
		
		WP();
		OWP();
		OOWP();
		
		printf("Case #%d:\n", t+1);
		for(int i = 0; i < n; i++) {
			double rpi = 0.25 * wp[i] + 0.5 * owp[i] + 0.25 * oowp[i];
			printf("%.12lf\n", rpi);
		}
	}
	
	return 0;
}

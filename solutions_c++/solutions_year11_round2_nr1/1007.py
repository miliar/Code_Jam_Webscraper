#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <cctype>
#include <cstring>
#include <iostream>
#include <vector>
#include <queue>
#include <stack>
#include <string>
#include <set>
#include <map>
#include <algorithm>

#define FOR(i, a, b) for(int i = int(a); i < int(b); i++)
#define INF 2000000000
#define EPS 1e-9
#define PB push_back
#define MP make_pair
#define F first
#define S second
using namespace std;

typedef long long ll;
typedef pair <int, int> ii;

int main() {
	int T, tc = 0;
	scanf("%d", &T);
	
	while(T--) {
		int n;
		scanf("%d", &n);
		
		char mat[105][105];
		for(int i = 0; i < n; ++i)
			scanf("%s", &mat[i]);
			
		double wp[105];
		int win[105] = {0}, total[105] = {0};
		for(int i = 0; i < n; ++i) {
			for(int j = 0; j < n; ++j) {
				if(i == j) continue;
				if(mat[i][j] == '.') continue;
				if(mat[i][j] == '1') win[i]++;
				total[i]++;;
			}	
			
			wp[i] = win[i]*1.0/total[i];
		}
		
		double owp[105];
		for(int j = 0; j < n; ++j) {
			double sum = 0.0;
			int cnt = 0;
			for(int i = 0; i < n; ++i) {
				if(i == j) continue;
				if(mat[i][j] == '.') continue;
				
				int twin = win[i];
				if(mat[i][j] == '1') twin--;
				sum += twin*1.0/(total[i]-1);
				cnt++;
			}
			
			owp[j] = sum/cnt;
		}
		
		double oowp[105];
		for(int i = 0; i < n; ++i) {
			double sum = 0.0;
			int cnt = 0;
			for(int j = 0; j < n; ++j) {
				if(i == j) continue;
				if(mat[i][j] == '.') continue;
				
				sum += owp[j];
				cnt++;
			}	
			
			oowp[i] = sum/cnt;
		}
		
		printf("Case #%d:\n", ++tc);
		for(int i = 0; i < n; ++i) {
			double ans = 0.25*wp[i] + 0.50*owp[i] + 0.25*oowp[i];
			printf("%lf\n", ans);	
		}
	}
	
	return 0;
	}

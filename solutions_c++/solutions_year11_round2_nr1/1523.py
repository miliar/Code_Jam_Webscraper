#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <cctype>
#include <iostream>
#include <string>
#include <set>
#include <map>
#include <list>
#include <queue>
#include <stack>
#include <vector>
#include <deque>
#include <utility>
#include <algorithm>
#include <functional>

using namespace std;

int main(int argc, char *argv[])
{
	int T;
	scanf("%d", &T);
	for(int ts=1;ts<=T;ts++){
		int n;
		scanf("%d", &n);
		char game[n][n+1];
		int play[n], win[n];
		double wp[n], owp[n], oowp[n], rpi[n];
		for(int i=0;i<n;i++){
			scanf("%s", game[i]);
			play[i] = n - count(game[i], game[i]+n, '.');
			win[i] = count(game[i], game[i]+n, '1');
			wp[i] = (double)win[i]/play[i];
			//printf("wp[%d]=%lf\n", i, wp[i]);
		}
		for(int i=0;i<n;i++){
			owp[i] = 0.0;
			for(int j=0;j<n;j++){
				if(game[i][j] != '.'){
					owp[i] += (double)(win[j]-(game[i][j]=='0'?1:0))/(play[j]-1);
					//printf("%lf, ",(double)(win[j]-(game[i][j]=='0'?1:0))/(play[j]-1));
				}
			}
			owp[i] /= play[i];
			//printf("team %d, play=%d, ", i, play[i]);
			//printf("owp[%d]=%lf\n", i, owp[i]);
		}
		for(int i=0;i<n;i++){
			oowp[i] = 0.0;
			for(int j=0;j<n;j++)
				if(game[i][j] != '.'){
					oowp[i] += owp[j];
				}
			oowp[i] /= play[i];
		}
		for(int i=0;i<n;i++)
			rpi[i] = 0.25 * wp[i] + 0.5 * owp[i] + 0.25 * oowp[i];
		printf("Case #%d:\n", ts);
		for(int i=0;i<n;i++)
			printf("%.8lf\n", rpi[i]);
	}
	return 0;
}


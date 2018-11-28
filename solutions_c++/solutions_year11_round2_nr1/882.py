#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <vector>
#include <cstring>
#include <map>
#include <algorithm>
#include <memory.h>

using namespace std;
#define MAXN 110
int N;

int n[MAXN][MAXN];
double w[MAXN];
double l[MAXN];
double wp[MAXN];
double owp[MAXN];
double oowp[MAXN];

int main()
{
	int cases;
	int casenum = 1;
	freopen("test", "r", stdin);
	freopen("output", "w", stdout);
	scanf("%d", &cases);
	while(cases--)
	{
		char tmp[MAXN];
		memset(n, 0, sizeof(n));
		memset(w, 0, sizeof(w));
		memset(l, 0, sizeof(l));
		memset(wp, 0, sizeof(wp));
		memset(owp, 0, sizeof(owp));
		memset(oowp, 0, sizeof(oowp));

		scanf("%d", &N);
		for(int i = 0;i < N; i++){
			scanf("%s", tmp);
			for(int j = 0;j < N; j++){
				if(tmp[j] == '1')
					n[i][j] = 1, w[i]+=1;
				if(tmp[j] == '0')
					n[i][j] = -1, l[i]+=1;
				if(tmp[j] == '.')
					n[i][j] = 0;
			}
		}

		printf("Case #%d:\n", casenum++);
		for(int i = 0;i < N; i++){
			//wp
			wp[i] = w[i] / (w[i] + l[i]);

			//owp
			double cnt = 0;
			double sum = 0;
			for(int j = 0;j < N; j++){
				if(n[i][j] == 0)continue;
				cnt++;
				//cout<<w[j]<<" "<<l[j]<<endl;

				if(n[j][i] == 1){
					sum += ((w[j] - 1) / (w[j] + l[j] - 1));
				}else{
					sum += ((w[j]) / (w[j] + l[j] - 1));
				}
			}
			owp[i] = sum / cnt;
		}

		for(int i = 0;i < N; i++){
			//oowp
			double cnt = 0;
			double sum = 0;
			for(int j = 0;j < N; j++){
				if(n[i][j] == 0)continue;
				cnt++;
				sum += owp[j];
			}
			oowp[i] = sum / cnt;

			double ans = 0.25 * (wp[i] + oowp[i] + 2 * owp[i]);
			printf("%.12lf\n", ans);
			//cout<<ans<<endl;
		}

	}
	return 0;
}


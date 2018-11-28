#include<iostream>
#include<algorithm>
#include<cstring>
#include<cmath>
#include<memory.h>
using namespace std;

#define CLR(a, b) (memset(a, b, sizeof(a)))
#define pi acos(-1.0)
#define INF 0x3f3f3f3f

int mp[110][110];
double wp[110], owp[110], oowp[110];

int main(){
	int cas;
	freopen("A.in", "r", stdin);
	freopen("A.out", "w", stdout);
	scanf("%d", &cas);
	for(int t = 0; t < cas; t++){
		int n;
		scanf("%d", &n);
		for(int i = 0; i < n; i++){
			char buf[110];
			scanf("%s", buf);
			for(int j = 0; j < n; j++){
				if(buf[j] == '1') mp[i][j] = 1;
				else if(buf[j] == '0') mp[i][j] = 0;
				else mp[i][j] = -1;
			}
		}
		for(int i = 0; i < n; i++){
			int fz, fm;
			fz = fm = 0;
			for(int j = 0; j < n; j++){
				if(mp[i][j] == 1) {fz++; fm++;}
				if(mp[i][j] == 0) fm++;
			}
			wp[i] = 1.0 * fz / fm;
		}
		for(int i = 0; i < n; i++){
			double tp = 0; int cnt = 0;
			for(int j = 0; j < n; j++){
				if(mp[i][j] != -1){
					int fz, fm;
					fz = fm = 0;
					for(int k = 0; k < n; k++){
						if(k != i){
							if(mp[j][k] == 1) {fz++; fm++;}
							if(mp[j][k] == 0) fm++;
						}
					}
					tp += 1.0 * fz / fm;
					cnt++;
				}
			}
			owp[i] = 1.0 * tp / cnt;
		}
		for(int i = 0; i < n; i++){
			double tp = 0; int cnt = 0;
			for(int j = 0; j < n; j++){
				if(mp[i][j] != -1){
					tp += owp[j];
					cnt++;
				}
			}
			oowp[i] = 1.0 * tp / cnt;
		}
		printf("Case #%d:\n", t + 1);
		for(int i = 0; i < n; i++){
			printf("%.12lf\n", 0.25 * wp[i] + 0.5 * owp[i] + 0.25 * oowp[i]);
		}
	}
	return 0;
}
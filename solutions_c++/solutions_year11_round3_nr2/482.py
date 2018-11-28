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
#define MAXN 1010

int L; //max fast ship
int N;
double T;
int C;
double n[MAXN];
double c[MAXN];

int main()
{
	int cases;
	int casenum = 1;
	freopen("test", "r", stdin);
	freopen("output", "w", stdout);
	scanf("%d", &cases);
	while(cases--)
	{
		memset(n, 0, sizeof(n));
		scanf("%d%lf%d%d", &L, &T, &N, &C);
		for(int i = 0;i < C; i++){
			scanf("%lf", &c[i]);
		}

		double sum_no = 0;
		for(int i = 0;i < N; i++){
			n[i] = c[i % C];
			sum_no += n[i] * 2;
		}

		//sort(n, n + N);
		double ans = sum_no;

		//build 1
		if(L == 1){
			for(int j = 0;j < N; j++){
				double sum = 0;

				for(int k = 0;k < N; k++){
					if(j == k){
						double ori = n[k] * 2;
						double need = (sum >= T) ? 0 : (T - sum);
						double speed = need + n[k] - (need) / 2;
					//	cout<<"speed:"<<ori<<" "<<speed<<" "<<need<<endl;
						if(speed < ori && speed < n[j] * 2){
							sum += speed;
							//cout<<nowL<<" "<<n[i]<<" "<<speed<<" "<<ori<<endl;
						}else{
							sum += n[k] * 2;
							//cout<<n[i] * 2<<endl;
						}
					}else{
						sum += n[k] * 2;
					}
				}
				if(sum <ans) ans = sum;
			}
		}
		if(L == 2){
			for(int i = 0;i < N; i++){
				for(int j = 0;j < N; j++){
					double sum = 0;

					for(int k = 0;k < N; k++){
						if(i == k || j == k){
							double ori = n[k] * 2;
							double need = (sum >= T) ? 0 : (T - sum);
							double speed = need + n[k] - (need) / 2;
						//	cout<<"speed:"<<ori<<" "<<speed<<" "<<need<<endl;
							if(speed < ori && speed < n[j] * 2){
								sum += speed;
								//cout<<nowL<<" "<<n[i]<<" "<<speed<<" "<<ori<<endl;
							}else{
								sum += n[k] * 2;
								//cout<<n[i] * 2<<endl;
							}
						}else{
							sum += n[k] * 2;
						}
					}
					if(sum <ans) ans = sum;
				}
			}
		}

		printf("Case #%d: %.0lf\n", casenum++, ans);

	}
	return 0;
}


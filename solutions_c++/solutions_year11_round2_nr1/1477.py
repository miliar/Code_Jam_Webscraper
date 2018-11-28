#include <string>
#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <algorithm>
#include <map>
#include <set>
#include <cmath>
#include <ctime>
#include <iostream>
#include <sstream>
#include <vector>
#include <queue>
#include <numeric>
#define powu(a) (a)*(a)

using namespace std;

bool flag;
long long gcd (long long a , long long b){
	if( b==0) return a;
	gcd(b,a%b);
}
int n;
char arr[128][128];
double print[128];
double win[128],total[128];
double wp[128];
double op[128];
double oop[128];
int main(void){
	int t;
	scanf("%d",&t);
	for(int te=0;te<t;te++){
		printf("Case #%d:\n",te+1);
		scanf("%d",&n);
		memset(print,0,sizeof(print));
		memset(wp,0,sizeof(wp));
		memset(op,0,sizeof(op));
		memset(oop,0,sizeof(oop));
		memset(win,0,sizeof(win));
		memset(total,0,sizeof(total));
		for(int i = 0 ;i < n;i++){
			scanf("%s",arr[i]);
			double temp=0;
			int cnt=0;
			for(int j = 0 ;j < n;j++){
				if( arr[i][j] != '.'){
					cnt++;
				}
				if( arr[i][j] == '1'){
					win[i]++;
					temp++;
				}
			}
			total[i] = cnt;
			temp = temp / cnt;
			wp[i] = temp;
		}
		for(int i = 0 ;i < n;i++){
			double temp=0;
			int cnt = 0;
			for(int j = 0 ;j < n;j++){
				if( arr[i][j] != '.'){
					total[j]--;
					cnt++;
					double tt=win[j];
					if( arr[j][i] == '1')
						win[j]--;

					temp+=(win[j]/total[j]);
					total[j]++;
					win[j] = tt;
				}
			}
			op[i] = temp/cnt ;
		}
		for(int i = 0 ;i < n;i++){
			int cnt=0;
			double temp=0;
			for(int j = 0 ; j<n;j++){
				if( arr[i][j] !='.'){
					cnt++;
					temp += op[j];
				}
			}
			oop[i] = temp / cnt;
		}
		for(int i = 0 ;i < n;i++){
			print[i] = 0.25 * wp[i];
			print[i]+= ( 0.5 * op[i]);
			print[i] += (0.25 * oop[i]);
		}
		for(int i = 0 ;i < n;i++){
			printf("%.7g\n",print[i]);
		}
	}
	return 0;
}
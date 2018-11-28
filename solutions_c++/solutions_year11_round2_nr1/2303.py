#include <cstdlib>
#include <cctype>
#include <cstring>
#include <cstdio>
#include <cmath>
#include <algorithm>
#include <vector>
#include <string>
#include <iostream>
#include <sstream>
#include <set>
#include <map>
#include <queue>
#include <stack>
using namespace std;

queue<int>Q;

int main(){

	freopen("A-large.in", "r", stdin);
	freopen("Aout.txt", "w", stdout);
	int T;
	char str[105][105];
	int cas = 1;
	int n;
	int number;
	double ans1[105], ans2[105], ans3[105];

	scanf("%d", &T);
	while (T--){
		double sum_ans = 0.0;
		scanf("%d", &n);
		for (int i = 0; i < n; i++)
			scanf("%s", str[i]);

		int sum ;
		int win ;
		int count;
////////1111111111111111111111111////////
		for (int i = 0; i < n; i++){
			win = 0;
			count = 0;
			for (int j = 0; j < n; j++){
				if (str[i][j] != '.'){
					count++;
				}
				if (str[i][j] == '1'){
					win++;
				}
			}
			ans1[i+1] = (win*1.0/count);
		}
////////////////2222222222222222//////////
		for (int i = 0; i < n; i++){
			win = 0;
			number = 0;
			count = 0;

			for (int j = 0; j < n; j++){
				if (str[i][j] != '.'){
					Q.push(j);
					number++;
				}
			}

			double ans = 0;

			while (!Q.empty()){
				count = 0;
				win = 0;

				int mid = Q.front();
				Q.pop();
				for (int j = 0; j < n; j++){
					if (str[mid][j] != '.' && j != i){
						count++;
					}
					if (str[mid][j] == '1' && j != i){
						win++;
					}
				}
				ans += (win*1.0/count);
			}

			ans2[i+1] =  ans/number;
		}
////////////////33333333333333333/////////

		for (int i = 0; i < n; i++){
			number = 0;
			double ans = 0.0;
			for (int j = 0; j < n; j++){
				if (str[i][j] != '.'){
					ans += ans2[j+1];
					number ++;
				}
			}
			ans3[i+1] = ans/number;
		}

		printf("Case #%d:\n", cas++);

		for (int i = 1; i <= n; i++){
			printf("%.6lf\n", 0.25*ans1[i]+0.5*ans2[i]+0.25*ans3[i]);
		}
	}
	return 0;
}
//be name oo
#include <cstdio>
#include <iostream>
#include <cstring>

#define FOR(i, n) for(int i = 0; i < (n); i++)

using namespace std;

const int MAX_N = 1000 + 10;

double rem[MAX_N];
double cycle[MAX_N];
int prm[MAX_N];
bool mark[MAX_N];

int main(){
	for(int i = 2; i < MAX_N; i++){
		cycle[i] = 0;
		for(int j = 1; j < i; j++)
			cycle[i] += cycle[j] + rem[i - j];
		cycle[i] += i;
		cycle[i] /= (i - 1);
	
		rem[i] = 0;
		for(int j = 1; j <= i; j++)
			rem[i] += cycle[j] + rem[i - j];
		rem[i] /= i;

	}

	//cerr<<rem[2]<<endl;

	int t;
	scanf("%d", &t);
	FOR(testCase, t){
		int n;
		scanf("%d", &n);
		FOR(i, n){
			scanf("%d", &prm[i]);
			prm[i]--;
		}
		memset(mark, 0, sizeof mark);
		double ans = 0;
		for(int i = 0; i < n; i++){
			int cnt = 0, pos = i;
			while(!mark[pos]){
				cnt++;
				mark[pos] = true;
				pos = prm[pos];
			}
			ans += cycle[cnt];
		}
		printf("Case #%d: %0.9lf\n", testCase + 1, ans);
	}
	return 0;
}


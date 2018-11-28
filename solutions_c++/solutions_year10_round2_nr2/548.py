#include <stdio.h>
#include <algorithm>
#include <set>
#include <map>
#include <queue>
#include <deque>
#include <vector>

#include <string.h>
#include <string>

#include <iostream>

using namespace  std;

template<typename T> T sqr(T a) { return (a) * (a); }
template<typename T> int size(T a) { return (int)((a).size()); }

void initf(){
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
}

int X[50];
int V[50];
void solve(int t){
	int N, B, K, T;
	scanf("%d%d%d%d", &N, &K, &B, &T);
	for(int i = 0; i < N; ++i){
		scanf("%d", &X[i]);
	}
	for(int i = 0; i < N; ++i){
		scanf("%d", &V[i]);
	}
	vector<double> time(N);
	for(int i = 0; i < N; ++i){
		time[i] = (double)(B - X[i]) / (double)(V[i]);
	}
	int cnt = 0;
	int sw = 0;
	for(int i = N - 1; i >= 0; --i){
		if ( time[i] > T ) continue;
		++ cnt;
		for(int j = i + 1; j < N; ++j){
			if ( time[i] <= time[j] && time[j] > T ) {
				++ sw;
			}
		}
		if ( cnt == K ) break;
	}
	if ( cnt != K  ) printf("Case #%d: IMPOSSIBLE\n", t);
	else printf("Case #%d: %d\n",t, sw);
	
	

}
int main(){


	initf();


	int test ;
	cin >> test;
	for(int t = 0; t < test; ++t){
		solve(t + 1);
	}


	return 0;
}
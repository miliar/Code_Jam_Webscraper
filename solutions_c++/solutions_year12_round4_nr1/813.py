/*************************************************************************
    > File Name: a.cpp
    > Created Time: 六  5/26 22:06:39 2012
 ************************************************************************/

#include<iostream>
using namespace std;

int d[10032], l[10032];
int dp[10032];

int main() {
	int Ncase;
	cin >> Ncase;
	for(int c = 1; c <= Ncase; c ++)
	{
		int N, D;
		bool done = false;
		cout << "Case #" << c << ": ";
		cin >> N;
		for(int i = 1; i <= N; i ++) {
			cin >> d[i] >> l[i];
		}
		cin >> D;
		memset(dp, 0, sizeof(dp));
		d[0] = 0;
		dp[0] = d[1];
		for(int i = 0; i <= N; i ++) {
			if(dp[i] >= D) done = true;
			for(int j = i + 1; j <= N; j ++) {
				if(d[j] > dp[i]) break;
				int dis1 = l[j], dis2 = d[j] - d[i];
				int temp = d[j] + (dis1 < dis2 ? dis1 : dis2);
				if(temp > dp[j]) dp[j] = temp;
			}
		}
		if(done) cout << "YES" << endl; else cout << "NO" << endl;
	}
	return 0;
}

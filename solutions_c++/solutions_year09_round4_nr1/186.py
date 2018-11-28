#include <iostream>
#include <cstring>
#include <algorithm>
using namespace std;

char mat[50][50];
int dp[50];

int main()
{
	freopen("A-large.in", "r", stdin);
	freopen("A-large.out", "w", stdout);
	int T, N, i, j, k;
	cin>>T;
	for(int t = 1; t <= T; ++t){
		cin>>N;
		for(i = 1; i <= N; ++i)
				cin>>mat[i];
		memset(dp, 0, sizeof(dp));
		for(i = 1; i <= N; ++i)
			for(j = 0; j < N; ++j)if(mat[i][j] == '1')dp[i] = j+1;
		int sum = 0;
		for(i = 1; i <= N; ++i){
			if(dp[i] <= i)continue;
			for(j = i+1; j <= N; ++j)if(dp[j] <= i)break;
			sum += j-i;
			while(j > i){
				dp[j] = dp[j-1];--j;
			}
		}
		cout<<"Case #"<<t<<": "<<sum<<endl;
	}
	return 0;
}

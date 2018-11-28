#include <iostream>
#include <map>
#include <string>
#include <cstring>

using namespace std;
int dp[1024][1024];

int main(){
	int ncas,ti;
	for(cin >> ncas,ti=1;ti<=ncas;ti++){
		int n,m;
		string sin;
		map<string,int> s_index;//string index
		memset(dp,0,1024*1024*4);

		cin >> n;
		getline(cin,sin);
		for(int i=0;i<n;i++){
			getline(cin,sin);
			s_index[sin] = i;
		}
		cin >> m;
		getline(cin,sin);
		for(int i=1;i<=m;i++){
			getline(cin,sin);
			int sidx = s_index[sin];
			for(int j=0;j<n;j++){
				dp[i][j] = INT_MAX / 2;
				if(j==sidx) continue;
				for(int k=0;k<n;k++){
					dp[i][j] = min(dp[i][j],(j==k)?(dp[i-1][j]):(dp[i-1][k]+1));
				}
			}
		}

		int mini_query = INT_MAX;
		for(int i=0;i<n;i++) if(mini_query > dp[m][i]) mini_query = dp[m][i]; 
		printf("Case #%d: %d\n",ti,mini_query);
	}
	return 0;
}

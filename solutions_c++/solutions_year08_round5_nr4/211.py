#include <algorithm>
#include <set>
#include <cstdio>
#include <iostream>
#include <map>
#include <vector>
#include <string>
#include <sstream>
#include <queue>
#include <numeric>
#include <cctype>

using namespace std;

#define fo(i,n) for(int i=0;i<n;i++)
#define fi fo(i,n)
#define fj fo(j,n)
#define go(i,v) for(typeof(v.begin()) i=v.begin();i!=v.end();i++)

typedef long long LL;
typedef long double LD;

int get(){int x; scanf("%d",&x); return x;}

int soln(){
	int h=get();
	int w=get();
	int n=get();

	vector<vector<int> > dp(h,vector<int>(w));
	vector<vector<int> > rock(h,vector<int>(w));

	dp[0][0]=1;

	fi { int r=get();int c=get(); rock[r-1][c-1]=1; }

	fo(i,h)fo(j,w)if(!rock[i][j]){
		if(i-2>=0&&j-1>=0)dp[i][j]+=dp[i-2][j-1];
		if(i-1>=0&&j-2>=0)dp[i][j]+=dp[i-1][j-2];
		dp[i][j]%=10007;
	}

	return dp[h-1][w-1];
}

int main(){
	int n=get();
	fi{
		int ans=soln();
		printf("Case #%d: %d\n",i+1,ans);
	}
	return 0;
}

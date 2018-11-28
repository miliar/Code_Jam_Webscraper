#include<stdio.h>
#include<stdlib.h>
#include<string.h>
#include<math.h>
#include<limits.h>
#include<ctype.h>
#include<iostream>
#include<iomanip>
#include<sstream>
#include<algorithm>
#include<functional>
#include<vector>
#include<string>
#include<stack>
#include<queue>
#include<set>
#include<map>
#include<complex>
#define EPS (1e-10)
#define PI (3.141592653589793238)
#define MP make_pair
typedef long long ll;
using namespace std;

int main(void){
	int casenum;
	scanf("%d",&casenum);
	for(int casecnt=1;casecnt<=casenum;casecnt++){
		int n;
		scanf("%d",&n);
		vector<int> d(n),l(n);
		for(int i=0;i<n;i++){
			scanf("%d %d",&d[i],&l[i]);
		}
		int D;
		scanf("%d",&D);
		d.push_back(D);
		l.push_back(0);
		n++;

		vector<int> dp(n);
		dp[0]=d[0];
		for(int i=1;i<n;i++){
			int val=-1;
			for(int j=0;j<i;j++){
				if(dp[j]==-1)continue;
				if(d[j]+dp[j]<d[i])continue;
				int now=min(l[i],d[i]-d[j]);
				val=max(val,now);
			}
			dp[i]=val;
		}

		printf("Case #%d: %s\n",casecnt,dp[n-1]!=-1?"YES":"NO");
		fflush(stdout);
	}
	return 0;
}

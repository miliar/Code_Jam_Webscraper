#include <iostream>
#include <string>
#include <vector>
#include <set>
#include <map>
#include <fstream>
#include <sstream>
#include <cmath>
#include <stdlib.h>
#include <math.h>
#include <stdio.h>
#include <queue>
#include <algorithm>
#include <ctime>
int inf=1000000111;
using namespace std;

int main()
{
	freopen("A-large.in", "r", stdin);
	freopen("out.txt", "w", stdout);
	int t;
	cin>>t;
	for (int step=0; step<t; ++step)
	{
		printf("Case #%d: ", step+1);
		int n; cin>>n;
		vector <int> pl(n+1);
		vector <int> l(n+1);
		
		for (int i=0; i<n; ++i)
			cin>>pl[i]>>l[i];
		cin>>pl[n];
		vector <int> dp(n+1, -1);

		dp[0]=pl[0];
		for (int i=0; i<n; ++i)
			for (int j=i+1; j<n+1; ++j){
				if (pl[j]-pl[i]>dp[i]) break;
				else dp[j]=max(dp[j],min(l[j], pl[j]-pl[i]));
			}

		if (dp[n]>-1) cout<<"YES"<<endl;
		else cout<<"NO"<<endl;
				





	}

}
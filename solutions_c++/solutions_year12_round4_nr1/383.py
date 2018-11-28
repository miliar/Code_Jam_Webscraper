#include <algorithm>
#include <string>
#include <list>
#include <numeric>
#include <vector>
#include <math.h>
#include <set>
#include <map>
#include <sstream>
#include <stack>
#include <stdio.h>
#include <queue>
#include <iostream>
using namespace std;

pair<int,int> mas[10000];

void solveCase(int t) {
	t++;
	int N;
	cin>>N;
	for (int i=0;i<N;i++)
		cin>>mas[i].first>>mas[i].second;
	int L;
	cin>>L;
	sort(mas,mas+N);

	int dp[10000];

	for (int i=0;i<10000;i++)
		dp[i]=-1;

	dp[0]=mas[0].first;
	for (int i=0;i<N;i++) {
		for (int j=i+1; j<N; j++) {
			if (dp[i]+mas[i].first >= mas[j].first) {
				dp[j]=max(dp[j],min(mas[j].second, mas[j].first-mas[i].first));
			}
		}
	}
	for (int i=0;i<N;i++) {
		if (mas[i].first+dp[i]>=L) {
			printf("Case #%d: YES\n",t);
			return;
		}
	}
	printf("Case #%d: NO\n",t);
	return;
}

int main()
{
    freopen("in.in","rt",stdin);
	freopen("out.out","wt",stdout);
	int T;
	cin>>T;
	for (int i=0;i<T;i++) {
		solveCase(i);
	}
    return 0;
}
#include<iostream>
#include<vector>
#include<map>
#include<set>
#include<string>
#include<string.h>
#include<stdlib.h>
#include<stdio.h>
#include<algorithm>
#include<queue>
using namespace std;
const int MAXN = 10000;
int dp[MAXN],mark[MAXN];

int main(){
	int i,j,k,T,n,m,TC=1;
	int x,s,r;
	double t;
	scanf("%d",&T);
	while(T--){
		scanf("%d%d%d%lf%d",&x,&s,&r,&t,&n);
		int sum=0;
		vector<pair<int, double> >vec;
		vec.clear();
		for(i=0;i<n;i++){
			int a,b,c;
			scanf("%d%d%d",&a,&b,&c);
			sum+=b-a;
			vec.push_back(make_pair(c,b-a));
		}
		vec.push_back(make_pair(0,x-sum));
		sort(vec.begin(),vec.end());
		//for(i=0;i<n+1;i++)printf("!%d %lf\n",vec[i].first,vec[i].second);
		double ans=0,tem;
		for(i=0;i<=n;i++){
			if(t>0){
				tem = (double)vec[i].second/(r+vec[i].first);
				tem = min(tem,t);
				ans+=tem;
				t-=tem;
				//printf("$%lf\n",tem);
				vec[i].second -= tem*(r+vec[i].first);
			}
			//printf("$%lf\n",vec[i].second);
			tem = vec[i].second/(s+vec[i].first);
			ans+=tem;
		}
		printf("Case #%d: %.9lf\n",TC++,ans);
	}
}
/*
3
10 1 4 1 2
4 6 1
6 9 2
12 1 2 4 1
6 12 1
20 1 3 20 5
0 4 5
4 8 4
8 12 3
12 16 2
16 20 1
*/

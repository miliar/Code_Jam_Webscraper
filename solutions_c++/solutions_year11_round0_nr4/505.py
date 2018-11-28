#include<iostream>
#include<vector>
#include<queue>
#include<set>
#include<cstdio>
#include<algorithm>
#include<string>
#include<map>
#include<cmath>
#include<cstdlib>
#include<ctime>
using namespace std;

const int K=7;

double res;
double chance[1001];
double d[1001];

int main() {
	freopen("input.txt", "rt", stdin);
	freopen("output.txt", "wt", stdout);
	int t; cin >> t;
	chance[1]=0.0;
	chance[2]=2.0;
/*
	for (int i=3;i<=10;i++) {
		vector<int> perm;
		vector<int> d(i+1);
		vector<int> sum(i+1);
		for (int j=0;j<i;j++) perm.push_back(j);
		int all=0;
		do {
			int cnt=0;
			for (int j=0;j<i;j++)
				if (perm[j]==j) cnt++;
			d[cnt]++;
			all++;
		} while (next_permutation(perm.begin(),perm.end()));
		sum[i]=d[i];
		chance[i]=(double)all;
		for (int j=i-1;j>=1;j--) {
			sum[j]=sum[j+1]+d[j];
			if (d[j]!=0) {
				chance[i]=min(chance[i],chance[i-j]+(double)all/(double)sum[j]);
			}
		}
	}
*/
	for (int k=0;k<t;k++) {
		res=0.0;
		int n; cin >> n;
		int a[1001];
		int to[1001];
		bool used[1001];
		for (int i=0;i<n;i++) {
			cin >> a[i];
			a[i]--;
			to[i]=a[i];
			used[i]=false;
		}
		for (int i=0;i<n;i++)
			if (!used[i]) {
				int cur=1;
				for (int j=to[i];j!=i;j=to[j]) {
					cur++;
					used[j]=true;
				}
				if (cur>1) {
					res+=(double)cur;
				}
				//res+=chance[cur];
			}
		
		printf("Case #%d: %.6f\n",k+1,res);
	}
	return 0;
}

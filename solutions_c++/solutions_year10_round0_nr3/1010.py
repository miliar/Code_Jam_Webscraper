#include <algorithm>
#include <iostream>
#include <sstream>
#include <cstdlib>
#include <fstream>
#include <bitset>
#include <cctype>
#include <cstdio>
#include <string>
#include <vector>
#include <queue>
#include <deque>
#include <cmath>
#include <stack>
#include <list>
#include <map>
#include <set>
using namespace std;

#define SIZE(X) ((int)X.size())
#define MP(A,B) make_pair(A,B)
#define PB(X) push_back(X)

typedef long long LL;
typedef pair<int,int> PII;

template<class T> void out(T A[],int n) {cout<<"{"; for (int i=0;i<n;i++){ cout<<A[i];if (i==n-1) cout<<"}"; else cout<<",";} cout<<endl;}
template<class T> void out(T A[],int n, int m) {for(int i=0;i<n;++i) out(A[i],m); cout<<endl;}\
template<class T> void out(vector<T> A,int n=-1) {if (n<0 || n>SIZE(A)) n=SIZE(A);cout<<"{";for (int i=0;i<n;i++) {cout<<A[i];if (i==n-1) cout<<"}"; else cout<<",";} cout<<endl;}

const int maxn = 128;
const int inf = 1000000000;
const double eps = 1e-8;
const double pi = acos(-1.0);

map< vector<int>, int> groupID;
vector< vector<int> > groups;
vector< long long > sum;
vector< long long > loopSum;

int g[1024];

int main()
{
  	freopen("C-large.in", "r", stdin);
  	freopen("outputC.txt", "w", stdout);
	int T, R, K, N;
	scanf("%d", &T);
	for (int cas = 1; cas <= T; ++cas) {
		printf("Case #%d: ", cas);
		groupID.clear();
		groups.clear();
		sum.clear();
		loopSum.clear();
		scanf("%d %d %d", &R, &K, &N);
		LL totsum = 0;
		for (int i = 0; i < N; ++i) {
			scanf("%d", &g[i]);
			totsum += g[i];
		}
		if (totsum <= K) {
			printf("%lld\n", totsum * R);
			continue;
		}
		long long ans = 0;
		int remain = 0;
		for (int cnt = 0, ind = 0, gsum = 0; cnt < R; ++cnt, gsum = 0) {
			vector<int> group;
			while (gsum + g[ind] <= K) {
				group.push_back(ind);
				gsum += g[ind];
				ind++;
				if (ind == N) ind = 0;
			}
			ans += gsum;
			if (groupID.count(group) != 0) {
				int from = groupID[group];
				groupID[group] = cnt;
				groups.push_back(group);
				sum.push_back((LL)gsum);
				for (int i = from + 1; i <= cnt; ++i) {
					if (i == from + 1)
						loopSum.push_back(sum[i]);
					else 
						loopSum.push_back(sum[i] + loopSum[loopSum.size() - 1]);
				}
				remain = R - cnt - 1;
				break;
			}
			else {
				groupID[group] = cnt;
				groups.push_back(group);
				sum.push_back((LL)gsum);
			}
		}
		if (remain) {
			int sz = loopSum.size();
			ans += loopSum[sz - 1] * (remain / sz);
			if (remain % sz != 0)
				ans += loopSum[remain % sz - 1];
		}
		printf("%lld\n", ans);
	}
	return 0;
}

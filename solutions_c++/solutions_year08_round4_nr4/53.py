#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <cctype>
#include <vector>
#include <string>
#include <queue>
#include <deque>
#include <stack>
#include <set>
#include <map>
#include <utility>
#include <algorithm>
#include <iostream>
#include <sstream>
using namespace std;

#define size(x) int((x).size())
#define foreach(i,c) for(typeof((c).begin()) i=(c).begin();i!=(c).end();i++)
typedef long long I64; typedef unsigned long long U64;
const double EPS=1e-12;
const int INF=999999999;
typedef vector<int> VI;
typedef vector<string> VS;

const int MAXN=1010;

int m,n;
char a[MAXN],b[MAXN];
bool flag[5];
int p[5];
int ans;

int check()
{
	for(int i=0;i<n;i+=m)
		for(int j=0;j<m;j++) b[i+j]=a[i+p[j]];

	int res=0;
	char prev=-1;
	for(int i=0;i<n;i++) {
		if(b[i]!=prev) res++;
		prev=b[i];
	}
	return res;
}

void go(int t)
{
	if(t==m) {
		ans<?=check();
		return;
	}

	for(int i=0;i<m;i++) if(!flag[i]) {
		p[t]=i;
		flag[i]=1;
		go(t+1);
		flag[i]=0;
	}
}

void solve()
{
	scanf("%d",&m);
	scanf("%s",a);
	n=strlen(a);

	memset(flag,0,sizeof(flag));
	ans=INF;
	go(0);
	printf("%d",ans);
}

int main()
{
	int T;
	scanf("%d",&T);
	for(int i=1;i<=T;i++) {
		printf("Case #%d: ",i);
		solve();
		printf("\n");
	}

	return 0;
}

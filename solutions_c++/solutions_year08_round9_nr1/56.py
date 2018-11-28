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

const int MAXN=5010;

int n;
VI a[MAXN];
int nb;
VI b[MAXN];

int com(int y,int z)
{
	int res=0;
	for(int i=0;i<nb;i++) if(b[i][0]<=y && b[i][1]<=z) res++;
	return res;
}

void solve()
{
	int ans=0;

	scanf("%d",&n);
	for(int i=0;i<n;i++) {
		a[i].resize(3);
		scanf("%d%d%d",&a[i][0],&a[i][1],&a[i][2]);
	}
	sort(a,a+n);

	int x,y,z;
	for(int i1=0;i1<n;i1++) {
		x=a[i1][0];

		nb=0;
		for(int j=0;j<n;j++) {
			if(a[j][0]<=x) {
				b[nb].resize(2);
				b[nb][0]=a[j][1],b[nb][1]=a[j][2];
				nb++;
			}
		}

		if(nb<=ans) continue;

		int yz=10000-x;

		sort(b,b+nb);

		int low=0,high=nb-1;
		while(low<=high) {
			int m1=(low*2+high)/3,m2=(low+high*2)/3;

			int v1=com(b[m1][0],yz-b[m1][0]);
			int v2=com(b[m2][0],yz-b[m2][0]);
			ans>?=v1;
			ans>?=v2;

			if(v1<=v2) low=m1+1; else high=m2-1;
		}
	}
	printf("%d",ans);
}

int main()
{	
	int T;
	scanf("%d",&T);
	for(int t=1;t<=T;t++) {
		printf("Case #%d: ",t);
		solve();
		printf("\n");
	}


	return 0;
}

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

int R,C;
int a[5][5];

bool check(int m0,int m1,int *p)
{
	for(int i=0;i<C;i++) {
		int c=(m0>>i)&1;
		c+=(m1>>i)&1;
		if(i>0) {
			c+=(m0>>(i-1))&1;
			c+=(m1>>(i-1))&1;
		}
		if(i+1<C) {
			c+=(m0>>(i+1))&1;
			c+=(m1>>(i+1))&1;
		}
		if(c!=p[i]) return 0;
	}
	return 1;
}

bool check2(int m0,int m1,int m2,int *p)
{
	for(int i=0;i<C;i++) {
		int c=(m0>>i)&1;
		c+=(m1>>i)&1;
		c+=(m2>>i)&1;
		if(i>0) {
			c+=(m0>>(i-1))&1;
			c+=(m1>>(i-1))&1;
			c+=(m2>>(i-1))&1;
		}
		if(i+1<C) {
			c+=(m0>>(i+1))&1;
			c+=(m1>>(i+1))&1;
			c+=(m2>>(i+1))&1;
		}
		if(c!=p[i]) return 0;
	}
	return 1;
}

void solve()
{
	int ans=0;

	scanf("%d%d",&R,&C);
	for(int i=0;i<R;i++) 
		for(int j=0;j<C;j++) scanf("%d",&a[i][j]);

	int C2=1<<C;
	int mid=R/2;
	for(int m0=0;m0<C2;m0++)
		for(int m1=0;m1<C2;m1++)
			for(int m2=0;m2<C2;m2++) {
				int w=0;
				for(int i=0;i<C;i++) if((m0>>i)&1) w++;
				if(w<=ans) continue;

				if(!check2(m0,m1,m2,a[mid])) continue;
				if(R==3) {
					if(!check(m1,m0,a[0])) continue;
					if(!check(m2,m0,a[2])) continue;
				}
				else {
					bool ok=0;
					for(int m3=0;m3<C2;m3++) {
						if(!check(m3,m1,a[0])) continue;
						if(!check2(m1,m0,m3,a[1])) continue;
						ok=1;
						break;
					}
					if(!ok) continue;

					ok=0;
					for(int m3=0;m3<C2;m3++) {
						if(!check(m3,m2,a[4])) continue;
						if(!check2(m2,m0,m3,a[3])) continue;
						ok=1;
						break;
					}
					if(!ok) continue;
				}

				ans=w;
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

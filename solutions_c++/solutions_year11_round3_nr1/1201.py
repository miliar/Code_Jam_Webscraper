#include <string>
#include <vector>
#include <map>
#include <set>
#include <cmath>
#include <iostream>
#include <cstdio>
#include <queue>
#include <deque>
#define PB push_back
#define REP(i,n) for(int(i)=0;(i)<(int)(n);(i)++)
#define INF 1000000000

using namespace std;

vector<vector<char> > a;
int n,m;

int zap(int i,int j) {
	a[i][j]='1';
	if (j+1<m&&a[i][j+1]=='#') a[i][j+1]='2';
	else return 0;
	if (i+1<n&&a[i+1][j]=='#') a[i+1][j]='2';
	else return 0;
	if (j+1<m&&i+1<n&&a[i+1][j+1]=='#') a[i+1][j+1]='1';
	else return 0;
	return 1;
}

int body(int t) {

	scanf("%d%d\n",&n,&m);
	a.clear();
	a.resize(n,vector<char> (m));
	REP(i,n) {
		REP(j,m) {
			scanf("%c",&a[i][j]);
		}
		scanf("\n");
	}
	printf("Case #%d:\n",t);
	REP(i,n) {
		REP(j,m) {
			if (a[i][j]=='#') {
				if (!zap(i,j)) {
					printf("Impossible\n");
					return 0;
				}
			}
		}
	}
	REP(i,n) {
		REP(j,m) {
			if (a[i][j]=='1') printf("/");
			else if (a[i][j]=='2') putchar(92);
			else printf("%c",a[i][j]);
		}
		printf("\n");
	}
	return 0;
}

int main()	{
/*
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
*/

/*
	freopen("A-small-attempt0.in","r",stdin);
	freopen("A-small-attempt0.out","w",stdout);
*/


	freopen("A-large.in","r",stdin);
	freopen("A-large.out","w",stdout);


	int k;
	scanf("%d",&k);
	for (int t=1; t<=k; t++) {
		body(t);
	}
    return 0;
}

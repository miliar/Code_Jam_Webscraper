//BISMILLAHIRRAHMANIRRAHIM



#include <iostream>
#include <sstream>
#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <string>
#include <cctype>
#include <climits>
#include <cmath>
#include <utility>
#include <vector>
#include <queue>
#include <stack>
#include <algorithm>
#include <set>
#include <map>
using namespace std;

#define pii pair < int , int >
#define i64 long long
#define CLR(x) memset(x,0,sizeof x)
#define SET(x,y) memset(x,y,sizeof x)


#define mx 510

int n,m;
char g[mx][mx];
bool chk() {
	int i,j,k,l;
	for(i=0;i<n;i++) {
		for(j=0;j<m;j++) if(g[i][j]=='#') {
			if((j+1)<m && (i+1)<n && g[i][j+1]=='#' && g[i+1][j+1]=='#' &&g[i+1][j]=='#') {
				g[i][j]='/';g[i][j+1]='\\';
				g[i+1][j]='\\';g[i+1][j+1]='/';
			}
			else {
				//cout<<i<<' '<<j<<'\n';
				return false;
			}
		}
	}
	return true;
}
				

int main() {
	freopen("A-large.in","r",stdin);
	freopen("A-large.out","w",stdout);
	int i,j,k,I,T;
	cin>>T;
	for(I=1;I<=T;I++) {
		cin>>n>>m;
		for(i=0;i<n;i++) scanf("%s",g[i]);
		printf("Case #%d:\n",I);
		if(chk()) {
			for(i=0;i<n;i++) cout<<g[i]<<'\n';
		}
		else puts("Impossible");
	}
	return 0;
}


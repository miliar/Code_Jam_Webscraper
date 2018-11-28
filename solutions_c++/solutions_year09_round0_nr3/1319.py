// Maciej Andrejczuk

#include <iostream>
#include <cstdio>
#include <cstring>
#include <algorithm>
#include <vector>
#include <queue>
#include <assert.h>
using namespace std;

#define REP(i,n) for(int i=0;i<(n);i++)
#define FOR(i,p,k) for(int i=(p);i<=(k);i++)
#define FORD(i,p,k) for(int i=(p);i>=(k);i--)
#define ZERO(m) memset(m,0,sizeof(m))
#define PB push_back
#define FI first
#define SE second

typedef long long LL;
typedef pair<int,int> PI;

int n;
int solve();
int main()
{
	scanf("%d\n",&n);
	FOR(i,1,n) {
		printf("Case #%d: ",i);
		int w = solve();
		printf("%.4d\n",w);
	}
}

int solve() {
	char c[1003];
	cin.getline(c,1000);
	int n=strlen(c);
	
	int t[25];
	REP(i,24) t[i]=0;
	t[0]=1;
	string p="welcome to code jam";
	
	REP(i,n) {
		FORD(j,p.size()-1,0) {
			if (c[i]==p[j]) {
				t[j+1]+=t[j];
				t[j+1]%=10000;
			}
		}
	}
	return t[p.size()]%10000;
}

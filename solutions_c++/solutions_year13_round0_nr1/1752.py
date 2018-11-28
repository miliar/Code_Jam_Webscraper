
#include<cstdio>
#include<iostream>
#include<algorithm>
#include<cmath>
#include<cstdlib>
#include<queue>
#include<map>
#include<set>
#include<string>
#include<sstream>
#include<climits>
#include<vector>
#include<cstring>
#include<stack>

using namespace std;

#define REP(i,s,n)  for (int i=(s),_n=(n);i<=_n;i++)
#define FOR(i,s,n)  for (int i=(s),_n=(n);i<_n;i++)
#define REPD(i,e,s)  for (int i=(e),_s=(s);i>=_s;i--)
#define tr(container, it) \
	for (typeof(container.begin()) it=container.begin(); it!=container.end();it++)
#define PB push_back
#define MP make_pair

typedef long long LL;

bool check(int ar[][10],char C) {
	REP(i,1,4) {
		int c1=0,c2=0;
		REP(j,1,4) {
			if (ar[i][j]=='T') c2++;
			if (ar[i][j]==C) c1++;
		}
		if (c1==4) return true;
		if (c1==3 && c2==1) return true;
	}
	REP(i,1,4) {
		int c1=0,c2=0;
		REP(j,1,4) {
			if (ar[j][i]=='T') c2++;
			if (ar[j][i]==C) c1++;
		}
		if (c1==4) return true;
		if (c1==3 && c2==1) return true;
	}
	int cc1=0,cc2=0;
	REP(i,1,4) {
		if (ar[i][i]=='T') cc2++;
		if (ar[i][i]==C) cc1++;
	}
	if (cc1==4) return true;
	if (cc1==3 && cc2==1) return true;
	cc1=0; cc2=0;
	REP(i,1,4) {
		if (ar[i][4-i+1]=='T') cc2++;
		if (ar[i][4-i+1]==C) cc1++;
	}
	if (cc1==4) return true;
	if (cc1==3 && cc2==1) return true;
	return false;
}

bool checkd(int ar[][10]) {
	int cnt=0;
	REP(i,1,4) REP(j,1,4) if (ar[i][j]!='.') cnt++;
	if (cnt==16) return true;
	return false;
}

int main() {
	int t;
	cin >> t;
	REP(tc,1,t) {
		int ar[10][10];
		FOR(i,0,4) {
			string s;
			cin >> s;
			FOR(j,0,4) ar[i+1][j+1]=s[j];
		}
		if (check(ar,'X')) cout << "Case #" << tc << ": X won" << endl;
		else if (check(ar,'O')) cout << "Case #" << tc << ": O won" << endl;
		else if (checkd(ar)) cout << "Case #" << tc << ": Draw" << endl;
		else cout << "Case #" << tc << ": Game has not completed" << endl;
	}
	return 0;
}

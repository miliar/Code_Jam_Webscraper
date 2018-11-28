#include<cstdio>
#include<algorithm>
#include<cmath>
#include<vector>
#include<string>
#include<map>

#define FOR(i,a,b) for(int i=(a); i<(int)(b); ++i)
#define FORD(i,a,b) for(int i=(a)-1; i>=(int)(b); --i)
#define FORE(i,C) for(__typeof(C.begin()) i=C.begin(); i!=C.end(); ++i)
#define MP make_pair
#define FI first
#define SE second
#define PB push_back

using namespace std;

typedef long long LL;

const int sMax = 102;
const int qMax = 1002;
const int INF = 10000;

int s,q;
int tabQ[qMax];
int pos[sMax];
map<string,int> M;

char S[105];

bool isNorm(char c) {
	return (c<='z' && c>='a') || (c<='Z' && c>='A') || (c<='9' && c>='0') || c==' ';
}

string read() {

	int len = 0;
	char c;

	do {
		scanf("%c",&c);
	} while(!isNorm(c));
	
	do {
		S[len++] = c;
		if(scanf("%c",&c)==EOF) break;
	} while(isNorm(c));

	S[len] = 0;
	return string(S);
	
}

void testcase(int tnum) {

	M.clear();

	scanf("%d",&s);
	FOR(i,0,s) {
		string A = read();
		M.insert(MP(A,i));
	}
	scanf("%d",&q);
	FOR(i,0,q) {
		string A = read();
		tabQ[i] = M[A];
	}
	
	int res = 0;
	int cur = tabQ[0];
	
	FOR(i,0,q) if(tabQ[i] == cur) {
		if(i>0) res++;
		FOR(j,0,s) pos[j] = INF;
		FOR(j,i,q) pos[tabQ[j]] <?= j;
		int maxi = 0;
		FOR(j,0,s) if(pos[j]>pos[maxi]) maxi = j;
		cur = maxi;
	}
	
	if(tnum>1) printf("\n");
	printf("Case #%d: %d",tnum,res);
	
}

int main() {

	int t;
	scanf("%d",&t);
	
	FOR(i,0,t) testcase(i+1);
	
	return 0;
}

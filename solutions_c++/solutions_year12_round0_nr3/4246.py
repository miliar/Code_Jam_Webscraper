#include<iostream>
#include<cstdio>
#include<cstdlib>
#include<cmath>
#include<algorithm>
#include<vector>
#include<set>
#include<map>
#include<stack>
#include<queue>
#include<list>
#include<string>
#include<cstring>

using namespace std;

#define PB push_back
#define MP make_pair
#define F first
#define S second
#define ALL(x) (x).begin(),(x).end()
#define SIZE(x) (int)(x).size()
#define SORT(x) sort((x).begin(),(x).end())
#define CLEAR(tab) memset(tab, 0, sizeof(tab))
#define REP(x, n) for(int x = 0; x < (n); x++)
#define FOR(x, b, e) for(int x = (b); x <= (e); x++)
#define FORD(x, b, e) for(int x = (b); x >= (e); x--)
#define VAR(v, n) __typeof(n) v = (n)
#define FOREACH(i, c) for(VAR(i, (c).begin()); i != (c).end(); ++i)
#define DEBUG(fmt, ...) fprintf(stderr, fmt, ##__VA_ARGS__)

const int MAX_BUF_SIZE = 16384;
char BUFOR[MAX_BUF_SIZE];
int BUF_SIZE, BUF_POS;
char ZZZ;
#define GET(ZZZ){ZZZ='a';if(BUF_POS<BUF_SIZE)ZZZ=BUFOR[BUF_POS++];\
else if(!feof(stdin)){BUF_SIZE=fread(BUFOR,1,MAX_BUF_SIZE,stdin);\
ZZZ=BUFOR[0];BUF_POS=1;}}
#define GI(WW){do{GET(ZZZ);}while(!isdigit(ZZZ));WW=ZZZ-'0';\
while(1){GET(ZZZ);if(!isdigit(ZZZ))break;WW=WW*10+(ZZZ-'0');}}
#define GC(WW){do{GET(ZZZ);}while(!isalpha(ZZZ));WW=ZZZ;}

//FAST IO

typedef long long int LL;
typedef pair<int,int> PII;
typedef vector<int> VI;

const int MXN = 210;
const int C = 262144;
const int INF = 1000000001;

char a[MXN], b[MXN];

inline bool czy(int A, int B) {
	int len = 0;
	while(A) {
		a[len++] = A % 10;
		A /= 10;
	}
	FOR(i, 0, len - 1)
		a[len + i] = a[i];
	int lenB = 0;
	while(B) {
		b[lenB++] = B % 10;
		B /= 10;
	}
	if(len != lenB)
		return 0;
	FOR(i, 0, len - 1) {
		FOR(j, 0, lenB - 1) {
			if(a[i + j] != b[j])
				break;
			if(j == lenB - 1)
				return 1;
		}
	}
	return 0;
}

int main() {
	int te;
	scanf("%d", &te);
	FOR(i, 1, te) {
		printf("Case #%d: ", i);

		int A, B;
		scanf("%d %d", &A, &B);
		int res = 0;
		FOR(j, A, B)
			FOR(o, j + 1, B)
				if(czy(j, o))
					res++;
		printf("%d\n", res);
	}
	return 0;
}

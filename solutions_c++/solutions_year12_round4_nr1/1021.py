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

const int MXN = 10010;
const int C = 262144;
const int INF = 1000000001;

int test;
int n;
int D[MXN];
int L[MXN];
int dist;
int H[MXN];

void go() {
	scanf("%d", &n);
	FOR(i, 1, n)
		scanf("%d %d", &D[i], &L[i]);
	scanf("%d", &dist);
	D[n + 1] = dist;
	L[n + 1] = INF;
	int iter = 2;
	FOR(i, 1, n + 1)
		H[i] = -1;
	H[1] = D[1];
	FOR(i, 1, n) {
		if(H[i] == -1)
			continue;
		//cout<<"A"<<endl;
		while(iter <= n + 1 && D[i] + H[i] >= D[iter]) {
			int dd = D[iter] - D[i];
			//cout<<dd<<" "<<iter<<" "<<i<<endl;
			if(H[i] >= dd) {
				if(L[iter] >= dd)
					H[iter] = dd;
				else
					H[iter] = L[iter];
			}
			else {
				H[iter] = -1;
				break;
			}
			//cout<<iter<<" "<<H[iter]<<" ! "<<H[i]<<" "<<dd<<" "<<L[iter]<<endl;
			iter++;
		}//cout<<"B"<<endl;
	}
	//FOR(i, 1, n + 1)
	//	cout<<D[i]<<" "<<H[i]<<" "<<L[i]<<endl;
	printf("Case #%d: ", test);
	if(H[n + 1] == -1)
		printf("NO\n");
	else
		printf("YES\n");
	CLEAR(D);
	CLEAR(H);
	CLEAR(L);
}

int main() {
	int te;
	scanf("%d", &te);
	for(test = 1; test <= te; test++)
		go();
	return 0;
}

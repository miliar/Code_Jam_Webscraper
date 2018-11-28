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

const int MXN = 2010;
const int C = 262144;
const int INF = 1000000001;

char tab[MXN];

int main() {

tab[97] = 'y';
tab[98] = 'h';
tab[99] = 'e';
tab[100] = 's';
tab[101] = 'o';
tab[102] = 'c';
tab[103] = 'v';
tab[104] = 'x';
tab[105] = 'd';
tab[106] = 'u';
tab[107] = 'i';
tab[108] = 'g';
tab[109] = 'l';
tab[110] = 'b';
tab[111] = 'k';
tab[112] = 'r';
tab[113] = 'z';
tab[114] = 't';
tab[115] = 'n';
tab[116] = 'w';
tab[117] = 'j';
tab[118] = 'p';
tab[119] = 'f';
tab[120] = 'm';
tab[121] = 'a';
tab[122] = 'q';

	int n;
	scanf("%d\n", &n);
	FOR(i, 1, n) {
		printf("Case #%d: ", i);
		char z;
		while(scanf("%c", &z) != -1) {
			if(isalpha(z))
				printf("%c", tab[z]);
			else
				printf("%c", z);
			if(!isalpha(z) && z != ' ')
				break;
		}
	}
	return 0;
}

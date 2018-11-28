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

/*
const int MAX_BUF_SIZE = 16384;
char BUFOR[MAX_BUF_SIZE];
int BUF_SIZE, BUF_POS;
char ZZZ;
#define GET(ZZZ){ZZZ='a';if(BUF_POS<BUF_SIZE)ZZZ=BUFOR[BUF_POS++];\
else if(!feof(stdin)){BUF_SIZE=fread(BUFOR,1,MAX_BUF_SIZE,stdin);\
ZZZ=BUFOR[0];BUF_POS=1;}}
#define GETINT(WW){do{GET(ZZZ);}while(!isdigit(ZZZ));WW=ZZZ-'0';\
while(1){GET(ZZZ);if(!isdigit(ZZZ))break;WW=WW*10+(ZZZ-'0');}}
*/
//FAST IO

typedef long long int LL;
typedef pair<int,int> PII;
typedef vector<int> VI;

const int MXN = 110;

int tescik = 1;

double rpi[MXN], owp[MXN], oowp[MXN];
int w[MXN][MXN];
int n;
int wygrane[MXN], zagrane[MXN];
double wp[MXN];

void test() {
	scanf("%d\n", &n);
	for(int i = 1; i <= n; i++) {
		char z;
		for(int j = 1 ; j<=n; j++) {
			while(1) {
				z = getchar();
				if(z == '1' || z == '0' || z == '.')
					break;
			}
			if(z == '1')
				w[i][j] = 1;
			if(z == '0')
				w[i][j] = -1;
			if(z == '.')
				w[i][j] = 0;
		}
	}
	for(int i = 1;  i<= n; i++) {
		int won = 0, played = 0;
		for(int j = 1; j <= n; j++)
			if(j != i) {
				if(w[i][j] != 0)
					played++;
				if(w[i][j] == 1)
					won++;
			}
		wygrane[i] = won;
		zagrane[i] = played;
		wp[i] = (double)won / played;
	}
	for(int i = 1;  i<= n; i++) {
		double mowp = 0;
		for(int j = 1;  j<= n; j++)
			if(j != i) {
				if(w[i][j] == 0)
					continue;
				int won = wygrane[j];
				int played = zagrane[j];
				if(w[j][i] == 1) {
					won--;
					played--;
				}
				if(w[j][i] == -1) {
					played--;
				}
				mowp += (double)won / played;
			}
		owp[i] = mowp / zagrane[i];
	}
	for(int i = 1;  i<= n; i++) {
		double mowp = 0;
		for(int j = 1; j <= n; j++)
			if(w[i][j] != 0) {
				mowp += owp[j];
			}
		oowp[i] = mowp / zagrane[i];
	}
	//RPI = 0.25 * WP + 0.50 * OWP + 0.25 * OOWP
	for(int i = 1; i <= n; i++)
		rpi[i] = 0.25 * wp[i] + 0.5 * owp[i] + 0.25 * oowp[i];
	printf("Case #%d:\n", tescik++);
	for(int i = 1; i <= n; i++)
		printf("%.10lf\n", rpi[i]);
	CLEAR(rpi);
	CLEAR(wp);
	CLEAR(owp);
	CLEAR(oowp);
	CLEAR(w);
}

int main() {
	int te;
	scanf("%d", &te);
	while(te--)
		test();
	return 0;
}


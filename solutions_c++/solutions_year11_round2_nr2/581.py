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

const int MXN = 1000010;
const double EPS = 0.00000001;

PII pkt[MXN];
int tescik = 1;
int n;
int d;
int a[MXN];

inline double mini(double x, double y) {
	if(x > y)
		return y;
	return x;
}

inline double abso(double x) {
	if(x > 0)
		return x;
	else
		return -x;
}

bool check(double czas) {
	double wsp = (double)pkt[0].F - czas;
	bool dec = 1;
	for(int i = 0; i < n; i++)
		a[i] = pkt[i].S;
	a[0]--;
	//cout<<"W "<<wsp<<" "<<czas<<endl;//endl;
	for(int i = 0; dec && i < n; i++) {
		while(a[i]) {
			double newx = wsp + d;
			if(abso(newx - pkt[i].F) <= czas) {
				a[i]--;
				wsp = newx;
			}
			else if(newx < pkt[i].F - czas) {
				wsp = pkt[i].F - czas;
				a[i]--;
			}
			else {
				dec = 0;
				break;
			}
		}
	}
	return dec;
}

void test() {
	scanf("%d %d", &n, &d);
	for(int i = 0; i < n; i++)
		scanf("%d %d", &pkt[i].F, &pkt[i].S);
//cout<<"A"<<endl;
	sort(pkt, pkt + n);//cout<<"B"<<endl;
	double res = 2000000000;
	double L = 0, R = MXN;
	while((R - L) > EPS) {
		double S = (L + R) / 2;
		if(check(S) ) {
			R = S - EPS;
			res = mini(res, S);
		}
		else
			L = S + EPS;
	}
	printf("Case #%d: %.10lf\n", tescik, res);
	tescik++;
}

int main() {
	int te;
	scanf("%d", &te);
	while(te--)
		test();
	return 0;
}

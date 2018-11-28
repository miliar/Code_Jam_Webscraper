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

PII a[MXN];
int o[MXN], oo;
int b[MXN], bb;
int n;
int xx;

void test() {
	scanf("%d", &n);
	for(int i = 1; i <= n; i++) {
		char z;
		while(1) {
			z = getchar();
			if(isalpha(z))
				break;
		}
		int q;
		scanf("%d", &q);
		if(z == 'B') {
			b[bb++] = q;
			a[i] = MP(0, q);
		}
		else {
			o[oo++] = q;
			a[i] = MP(1, q);
		}
	}
	int itB = 0, itO = 0;
	int res = 0;
	int posO = 1, posB = 1;
	for(int i = 1; i <= n; i++) {
		int nextB = b[itB];
		int nextO = o[itO];
		if(a[i].F == 0) {
			//if(posB != a[i].S) {
				int czas = abs(a[i].S - posB) + 1;
				res += czas;
				posB = a[i].S;
				if(posO != o[itO]) {
					int dO = o[itO] - posO;
					if(abs(dO) <= czas)
						posO = o[itO];
					else if(dO > 0)
						posO = posO + czas;
					else
						posO = posO - czas;
				}
			//}

			itB++;
		}
		else {
			//if(posO != a[i].S) {
				int czas = abs(a[i].S - posO) + 1;
				res += czas;
				posO = a[i].S;
				//cout<<czas<<endl;
				if(posB != b[itB]) {
					int dB = b[itB] - posB;
					if(abs(dB) <= czas)
						posB = b[itB];
					else if(dB > 0)
						posB = posB + czas;
					else
						posB = posB - czas;
				}
			//}
			itO++;
		}
		//cout<<posB<<" "<<posO<<" "<<itO<<" "<<itB<<" "<<res<<endl;
	}
	printf("Case #%d: %d\n", xx, res);
	bb = oo = 0;
}

int main() {
	int te;
	scanf("%d", &te);
	xx = 1;
	while(te--) {
		test();
		xx++;
	}
	return 0;
}

#include <vector>
#include <string>
#include <cstdio>
#include <iostream>
#include <algorithm>
#include <cmath>
using namespace std;

#define DEBUGxyz(x,y,z) cerr << #x << " = " << x << ", " << #y << " = " << y << ", " << #z << " = " << z << endl;
#define REP(i,n) for(int i=0,_n=(n);i<_n;++i)
#define PB push_back
#define MP make_pair
#define ST first

typedef vector<int> VI; typedef pair<int,int > PII;
inline int getint() { int x; scanf("%d",&x); return x; }
inline void OPEN(string name) {
	string in = name+".in"; freopen(in.c_str(),"r",stdin);
	string out = name+".out"; freopen(out.c_str(),"w",stdout);
}

// Powered By TimoAI 2.2

const int MAKS = 1<<10;
int P;
int M[MAKS];
int sisaM[MAKS];
int wajibM[MAKS];
VI price[MAKS];
PII order[MAKS];

int main() {
	OPEN("b");
	REP(ncase,getint()) {
		P = getint();
		int no = 1;
		REP(i,1<<P) {
			M[i] = getint();
			price[i].clear();
			sisaM[i] = 0;
			order[i] = MP( 0, i );

		}
		int k = 1<<P;
		int d = 1;

		REP(i,P) {
			k /= 2;
			int j = 0;
			REP(i,k) {
				int x = getint();
				sisaM[j]++;
				sisaM[j+d]++;
				price[j].PB(x);
				price[j+d].PB(x);
				j += d+d;
				order[j].ST = no;
				order[j+d].ST = no;
				no++;
			}
			d *= 2;
		}
		// sort(order,order+(1<<P));
		REP(i,1<<P) {
			wajibM[i] = max(0,P - M[i]);

		}
		// REP(i,1<<P) DEBUGxyz(i,sisaM[i],wajibM[i]);


		int ans = 0;
		k = 1;
		d = 1<<P;

		int ok = 0;

		REP(i,P) {
			int s = 0;
			REP(j,k) {
				int cost = 0;
				REP(x,d) if(wajibM[s+x]>0) {
					wajibM[s+x]--;
					cost=1;
				}
				ans += cost;
				s += d;
			}
			k *= 2;
			d /= 2;
		}

		printf("Case #%d: %d\n",ncase+1,ans);
	}
	return 0;
}

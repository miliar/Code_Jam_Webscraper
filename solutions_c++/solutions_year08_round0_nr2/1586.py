#include<cstdio>
#include<iostream>
#include<sstream>
#include<cmath>
#include<algorithm>
#include<map>
#include<set>
#include<list>
#include<vector>
#include<stack>
#include<queue>
#include<string>
using namespace std;
#define FOR(i,a,b) for(int i=(a);i<=(b);++i)
#define FORD(i,a,b) for(int i=(a);i>=(b);--i)
#define REP(i,n) FOR(i,0,(n)-1)
#define FS(i,v) for(__typeof((v).begin())i=(v).begin();i!=v.end();++(i))
#define ALL(a) (a).begin(),(a).end()
#define SZ(a) ((int)(a).size())
#define MK make_pair
#define FI first
#define SE second
typedef long long ll;
typedef long double ldouble;
int N, T, NA, NB, Aile[24*60+107], Bile[24*60+107];
vector<int> Aodj[24*60+107], Bodj[24*60+107];
void lecim(int nur) {
	scanf("%d",&T);
	scanf("%d%d", &NA, &NB);
	for(int i = 0; i < 24*60; ++i) {
		Aile[i] = Bile[i] = 0;
		Aodj[i].clear();
		Bodj[i].clear();
	}
	for(int i = 0; i < NA; ++i) {
		int ha, ma, hb, mb;
		scanf("%d:%d %d:%d", &ha, &ma, &hb, &mb);
		int cza, czb;
		cza = ha * 60 + ma;
		czb = hb * 60 + mb;
		Aodj[cza].push_back(czb);
	}
	for(int i = 0; i < NB; ++i) {
		int ha, ma, hb, mb;
		scanf("%d:%d %d:%d", &ha, &ma, &hb, &mb);
		int cza, czb;
		cza = ha * 60 + ma;
		czb = hb * 60 + mb;
		Bodj[cza].push_back(czb);
	}
	int wyna = 0, wynb = 0, akta = 0, aktb = 0;
	for(int i = 0; i < 24 * 60; ++i) {
		akta += Aile[i];
		aktb += Bile[i];
		for(int j = 0; j < (int)Aodj[i].size(); ++j) {
			if(akta == 0) ++wyna, ++akta;
			--akta;
			Bile[Aodj[i][j] + T]++;
		}
		for(int j = 0; j < (int)Bodj[i].size(); ++j) {
			if(aktb == 0) ++wynb, ++aktb;
			--aktb;
			Aile[Bodj[i][j] + T]++;
		}
	}
	printf("Case #%d: %d %d\n", nur, wyna, wynb);
}
int main() {
	scanf("%d",&N);
	for(int i = 0; i < N; ++i) lecim(i + 1);
	return 0;
}

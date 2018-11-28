#include <cstdio>
#include <vector>
#include <map>
#include <set>
#include <queue>
#include <stack>
#include <cstdlib>
#include <algorithm>
#include <climits>
#include <cmath>
#include <ctime>
#define FOR(x,y,z) for(int (x)=(y);(x)<(z);(x)++)
#define FORQ(x,y,z) for(int (x)=(y);(x)<=(z);(x)++)
#define FORD(x,y,z) for(int (x)=(y);(x)>(z);(x)--)
#define FORDQ(x,y,z) for(int (x)=(y);(x)>=(z);(x)--)
#define REP(x,z) for(int (x)=1;(x)<=(z);(x)++)
#define UNIQUE(x) sort(ALL((x))); (x).resize(unique(ALL((x)))-(x).begin());
#define PB push_back
#define MP make_pair
#define ALL(x) (x).begin(),(x).end()
#define F first
#define S second
#define PII pair<int,int>
#define PACKS(Z,IdzieSobieBladWielbladMaWrotkiNaKopytachJESTNIENORMALNY) int Z;scanf("%d",&Z);FORQ(IdzieSobieBladWielbladMaWrotkiNaKoptyachJESTNIENORMALNY,1,Z)
//#define NODEBUG
#ifdef NODEBUG
	#define debug(...) /*fprintf(stderr,__VA_ARGS__);*/
#else
	#define debug(...) fprintf(stderr,__VA_ARGS__);
#endif
using namespace std;
int tab[1111];
int main(){
	int wtf=0;
	PACKS(Z,zZZXXXZ){
		++wtf;
		int n;
		scanf("%d",&n);
		FOR(i,0,n)scanf("%d",&tab[i]);
		int x=tab[0];
		FOR(i,1,n)x^=tab[i];
		int out=0;
		int mini=INT_MAX;
		if(x!=0)out=-1;
		else FOR(i,0,n)out+=tab[i];
		FOR(i,0,n)mini=min(mini,tab[i]);
		printf("Case #%d: ",wtf);
		if(out==-1)printf("NO\n");
		else printf("%d\n",out-mini);
	}
	return 0;
}

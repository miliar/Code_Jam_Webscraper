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
int n;
int main(){
	int jot=0;
	PACKS(Z,ZzZ){
		jot++;
		scanf("%d",&n);
		int p[2]={1,1};
		int t[2]={1,1};
		int bon=0;
		int out=0;
		char last = 'A';
		FOR(i,0,n){
			char x[2];
			int y;
			scanf("%c%c%d",&x[0],&x[1],&y);
			int w=abs(p[x[1]=='B']-y);
			p[x[1]=='B']=y;
			if(x[1]!=last){
				if(w<=bon){
					out+=1;
					bon=1;
				}
				else {
					out+=w-bon+1;
					bon=w-bon+1;
				}
			}
			else {
				out+=w+1;
				bon+=w+1;
			}
			last=x[1];
		}
		while(getchar()!='\n');
		printf("Case #%d: %d\n",jot,out);
	}
	return 0;
}


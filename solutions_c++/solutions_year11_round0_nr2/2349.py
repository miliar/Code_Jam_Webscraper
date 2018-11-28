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
#define PACKS(Z,IdzieSobieBladWielbladMaWrotkiNaKopytachJESTNIENORMALNY) int Z;scanf("%d",&Z);REP(IdzieSobieBladWielbladMaWrotkiNaKoptyachJESTNIENORMALNY,Z)
//#define NODEBUG
#ifdef NODEBUG
	#define debug(...) /*fprintf(stderr,__VA_ARGS__);*/
#else
	#define debug(...) fprintf(stderr,__VA_ARGS__);
#endif
using namespace std;
int c,d,n;
char t[3];
map<pair<char,char>, char > comb;
vector<char> dest[200];
struct bigletter{
	bool operator()(int x,int y){
		return x>y;
	}
};
int pos[200];
char T[111];
int main(){
	int wtf=0;
	PACKS(Z,ZzZ){
		wtf++;
		scanf("%d",&c);
		FOR(i,0,c){
			scanf("%s",t);
			comb[MP(t[0],t[1])]=t[2];
			comb[MP(t[1],t[0])]=t[2];
		}
		scanf("%d",&d);
		FOR(i,0,d){
			scanf("%s",t);
			dest[t[0]].PB(t[1]);
			dest[t[1]].PB(t[0]);
		}
		//FORQ(i,'A','Z')sort(ALL(dest[i]));
		scanf("%d",&n);
		scanf("%s",T);
		vector<char> out;
		FOR(i,0,n){
			out.PB(T[i]);
			if(out.size()==1){pos[T[i]]++;continue;}
			pair<char,char> end = MP(out[out.size()-1],out[out.size()-2]);
			bool bum=0;
			if(comb.find(end)!=comb.end()){
				out.pop_back();
				pos[out.back()]--;
				out[out.size()-1]=comb.find(end)->S;
				bum=1;
				pos[out.back()]++;
			}
			else if(!bum){
				int who=-1;
				FOR(j,0,dest[T[i]].size()){
					if(pos[dest[T[i]][j]]>0){who=1;break;}
				}
				if(who>0){
					bum=1;
					out.clear();
					FORQ(j,'A','Z')pos[j]=0;
				}
			//	printf("%d\n",who);
			}
			//FOR(j,0,out.size())printf("%c",out[j]);putchar('\n');
			if(!bum)pos[T[i]]++;
		}
		printf("Case #%d: [",wtf);if(!out.empty()){FOR(i,0,out.size()-1)printf("%c, ",out[i]);printf("%c",out.back());}printf("]\n");
		out.clear();
		FORQ(i,'A','Z'){dest[i].clear();pos[i]=0;}comb.clear();
	}
	return 0;
}

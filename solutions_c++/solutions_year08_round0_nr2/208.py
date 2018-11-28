#include <cstdlib>
#include <cstdio>
#include <cmath>
#include <cctype>
#include <iostream>
#include <fstream>
#include <algorithm>
#include <queue>
#include <string>
#include <sstream>
#include <vector>
#include <map>
#include <bitset>

#define FOR(i,a,b) for(int i=a;i<b;i++)
#define REP(i,b) FOR(i,0,b)
#define sqr(a) ((a)*(a))

const double EPS=1e-5;
#define eq(a,b) (abs((a)-(b))<=EPS)

using namespace std;

char fin[]="b.in",fout[]="b.out";
const int LEN=1440;
int n,t,na,nb,ra,rb;
vector< pair< int,int > > ma,mb;
vector< int > ha,hb;

int main(){
	freopen(fin,"r",stdin);
	freopen(fout,"w",stdout);
	int h1,m1,h2,m2,ta,tb;
	scanf("%d",&n);
	REP(z,n){
		ra=rb=ta=tb=0;
		scanf("%d%d%d",&t,&na,&nb);
		ma.resize(na);
		mb.resize(nb);
		ha=hb=vector< int >(2*LEN,0);
		REP(i,na){
			scanf("%d:%d %d:%d",&h1,&m1,&h2,&m2);
			ma[i].first=h1*60+m1;
			ma[i].second=h2*60+m2+t;
		}
		REP(i,nb){
			scanf("%d:%d %d:%d",&h1,&m1,&h2,&m2);
			mb[i].first=h1*60+m1;
			mb[i].second=h2*60+m2+t;
		}
		REP(i,na){
			ha[ma[i].first]--;
			hb[ma[i].second]++;
		}
		REP(i,nb){
			hb[mb[i].first]--;
			ha[mb[i].second]++;
		}
		REP(i,LEN){
			if(ha[i]){
				ta+=ha[i];
				ra=min(ra,ta);
			}
			if(hb[i]){
				tb+=hb[i];
				rb=min(rb,tb);
			}
		}
		printf("Case #%d: %d %d\n",z+1,-ra,-rb);
	}
	exit(0);
}

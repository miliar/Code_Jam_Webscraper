#include <algorithm>
#include <iostream>
#include <sstream>
#include <string>
#include <vector>
#include <queue>
#include <set>
#include <map>
#include <cstdio>
#include <cstdlib>
#include <cctype>
#include <cmath>

#define FOR(i,a,b) for (int i = (int)a; i < (int)b; ++i)
#define REP(i,a) FOR(i,0,a)
#define ALL(a) a.begin(),a.end()
#define SIZE(a) a.size()
#define PB push_back
#define FILL(a) memset(&a,0,sizeof(a))
typedef long long LL;

using namespace std;

int timetoint(string s){
	int res=0;
	res=10*(s[0]-'0')+s[1]-'0';
	res*=60;
	res+=10*(s[3]-'0')+s[4]-'0';
	return res;
}

struct time{
public:
	int t,place,dif;
	time(int T,int P,int D):t(T),place(P),dif(D){}
};

bool sravn (time a,time b){
	if (a.t!=b.t) return a.t<b.t;
	else return a.dif>b.dif;
}

int main(){
	freopen("a.in","r",stdin);
	freopen("a.out","w",stdout);
	int tc;
	scanf("%d",&tc);
	REP(it,tc){
		vector<time> a;
		int t,na,nb;
		scanf("%d%d%d\n",&t,&na,&nb);
		REP(i,na){
			string s1,s2;
			cin>>s1>>s2;
			int t1=timetoint(s1),t2=timetoint(s2);
			a.PB(time(t1,1,-1));
			a.PB(time(t2+t,2,1));
		}
		REP(i,nb){
			string s1,s2;
			cin>>s1>>s2;
			int t1=timetoint(s1),t2=timetoint(s2);
			a.PB(time(t1,2,-1));
			a.PB(time(t2+t,1,1));
		}
		sort(ALL(a),sravn);
		int resa=0,cura=0,resb=0,curb=0;
		REP(i,SIZE(a)){
			if (a[i].place==1){
				cura+=a[i].dif;
				if (cura<0){
					++cura;
					++resa;
				}
			}
			else{
				curb+=a[i].dif;
				if (curb<0){
					++curb;
					++resb;
				}
			}
		}
		printf("Case #%d: %d %d\n",it+1,resa,resb);
	}
}
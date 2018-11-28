#include <cstdio>
#include <cstring>
#include <vector>
#include <queue>
#include <algorithm>
using namespace std;
typedef pair<int,int> P;
#define s first
#define e second

int main(){
	int t;
	scanf("%d",&t);
	for (int z=1;z<=t;++z){
		int t,na,nb;
		scanf("%d%d%d",&t,&na,&nb);
		P aa[na+1], bb[nb+1];
		int h,m;
		char c;
		for (int i=0;i<na;++i){
			scanf("%d%c%d",&h,&c,&m);
			aa[i].s = h*60+m;
			scanf("%d%c%d",&h,&c,&m);
			aa[i].e = h*60+m;
		}
		for (int i=0;i<nb;++i){
			scanf("%d%c%d",&h,&c,&m);
			bb[i].s = h*60+m;
			scanf("%d%c%d",&h,&c,&m);
			bb[i].e = h*60+m;
		}
		sort(aa,aa+na);
		sort(bb,bb+nb);
		aa[na].s = 1<<29;
		bb[nb].s = 1<<29;
		int a=0, b=0, ca=0, cb=0;
		priority_queue<int, vector<int>, greater<int> > ta, tb;
		while (ca < na || cb < nb){
			if (aa[ca].s < bb[cb].s){
				if (ta.size()==0 || ta.top()>aa[ca].s) ++a;
					else ta.pop();
				tb.push(aa[ca].e+t);
				++ca;
			} else {
				if (tb.size()==0 || tb.top()>bb[cb].s) ++b;
					else tb.pop();
				ta.push(bb[cb].e+t);
				++cb;
			}
		}
		printf("Case #%d: %d %d\n",z,a,b);
	}
	return 0;
}

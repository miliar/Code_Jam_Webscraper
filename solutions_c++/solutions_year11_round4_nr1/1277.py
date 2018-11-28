#include<cstdio>
#include<vector>
#include<string> 
#include<cstring>
#include<map>
#include<set>
#include<algorithm>
using namespace std;
typedef __int64 i64;
#define REP(i,n) for(int i=0;i<(int)(n);++i)
#define R64(i,n) for(i64 i=0;i<(i64)(n);++i)
//typedef double ld;
typedef long double ld;

ld pos;
ld time;
ld X,S,R,t;
ld max(ld a,ld b) {
	if(a>b) return a;else return b;
}
void run(ld dist,ld bonus) {
	ld rem = max(t-time,0);

	ld prebehnem = dist/(bonus+R);
	if( prebehnem <=rem) {
		time+=prebehnem;
	} else{
		ld kok = (dist-rem*(bonus+R))/(bonus+S);
		time+=kok+rem;
		
	}


}
int main() {
	int task_count;
	scanf("%d",&task_count);
	REP(task_id,task_count) {
		int n;
		scanf("%Lf %Lf %Lf %Lf %d",&X,&S,&R,&t,&n);		
		time = 0;
		vector<pair<ld,ld > >v;
		ld sum=0;
		REP(i,n) {
			ld b,e,w;
			scanf("%Lf %Lf %Lf",&b,&e,&w);		
			sum+=(e-b);
			v.push_back(make_pair(w,e-b));
		}
		sort(v.begin(),v.end());
		run(X-sum,0);
		
		REP(i,v.size()) {
			run(v[i].second,v[i].first);
		}
		
		printf("Case #%d: %.9Lf\n",task_id+1,time);
	}
	return 0;
}
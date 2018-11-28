#include<stdio.h>
#include<vector>
#include<algorithm>
using namespace std;

#define ARRIVE 0
#define DEPART 1

#define A 0
#define B 1

int na,nb,tt;

struct Event{
	int time,term,type;
	Event(){}
	Event(int h,int m,int _term,int _type){
		time = h*60+m;
		term = _term;
		type = _type;
	}
};

bool operator<(const Event &a,const Event &b){
	if(a.time == b.time){
		if(a.term == b.term)
			return a.type < b.type;
		return a.term < b.term;
	}
	return a.time < b.time;
}

vector<Event> e;

int main(){

	int T,N,i,h,m;
	int cur[2],need[2];

	scanf("%d",&T);

	for(N=1;N<=T;N++){
		
		scanf("%d",&tt);
		scanf("%d%d",&na,&nb);

		e.clear();
		while(na--){
			scanf("%d:%d",&h,&m);
			e.push_back(Event(h,m,A,DEPART));
			scanf("%d:%d",&h,&m);
			e.push_back(Event(h,m+tt,B,ARRIVE));
		}
		while(nb--){
			scanf("%d:%d",&h,&m);
			e.push_back(Event(h,m,B,DEPART));
			scanf("%d:%d",&h,&m);
			e.push_back(Event(h,m+tt,A,ARRIVE));
		}

		sort(e.begin(),e.end());

		cur[0] = cur[1] = 0;
		need[0] = need[1] = 0;

		for(i=0;i<e.size();i++){
			if(e[i].type == ARRIVE)
				cur[ e[i].term ]++;
			else{
				if(cur[ e[i].term ] > 0)
					cur[ e[i].term ]--;
				else
					need[ e[i].term ]++;
			}
		}
		
		printf("Case #%d: %d %d\n",N,need[0],need[1]);
	}

	return 0;
}

#include <stdio.h>
#include <math.h>
#include <string.h>
#include <vector>
#include <queue>
#include <algorithm>
#include <stdlib.h>

using namespace std;

#define min(a,b) ((a)>(b)?(b):(a))
#define maxn 110
#define maxm 1010
#define maxl 110
#define INF 1000000

#define TOA 1
#define TOB 2
#define FROMA 3
#define FROMB 4

struct Event{
	int time;
	int state;
};

vector <Event> q;
int t;
int na,nb;

int cmp(Event p1,Event p2){
	if (p1.time<p2.time || p1.time==p2.time && p1.state<p2.state) return 1;
	return 0;
}

void init(){
	q.clear();
	scanf("%d",&t);
	scanf("%d%d",&na,&nb);
	int i,h1,h2,m1,m2;
	Event e;
	for (i=0;i<na;i++){
		scanf("%d:%d %d:%d",&h1,&m1,&h2,&m2);
		e.time=h1*60+m1;
		e.state=FROMA;
		q.push_back(e);
		e.time=h2*60+m2+t;
		e.state=TOB;
		q.push_back(e);
	}
	for (i=0;i<nb;i++){
		scanf("%d:%d %d:%d",&h1,&m1,&h2,&m2);
		e.time=h1*60+m1;
		e.state=FROMB;
		q.push_back(e);
		e.time=h2*60+m2+t;
		e.state=TOA;
		q.push_back(e);
	}
	sort(q.begin(),q.end(),cmp);
}

void solve(){
	int i,cura=0,curb=0,mina=0,minb=0;
	int m=q.size();
	for (i=0;i<m;i++){
		if (q[i].state==FROMA)
			cura--;
		if (q[i].state==FROMB)
			curb--;
		if (q[i].state==TOA)
			cura++;
		if (q[i].state==TOB)
			curb++;
		mina=min(mina,cura);
		minb=min(minb,curb);
	}
	printf("%d %d\n",-mina,-minb);
}

int main(){
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	int ntest,i;
	scanf("%d",&ntest);
	for (i=1;i<=ntest;i++){
		init();
		printf("Case #%d: ",i);
		solve();
	}
	return 0;
}
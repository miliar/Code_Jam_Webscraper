#include <queue>
#include <cstdio>

#include "train.table.h"

using namespace std;


// state of world
int avail[2];
int  need[2];
int turnaround;

typedef std::priority_queue<Entry*, vector<Entry*>, Comparator_func> agenda_t;
agenda_t agenda;

void Departure::process(void){
	int idx = (target != A) ? 0 : 1;
	if(avail[idx]>0)
		avail[idx]--;
	else
		need[idx]++;

	arrival.add(turnaround);
	agenda.push(new Available(arrival, target));
}


void Available::process(void){
	int idx = (target == A) ? 0 : 1;
	avail[idx]++;
}


static void solve_case(int );
static void add_dep(Target target);

int main(void)
{
	int N;
	scanf("%d",&N);

	for(int i = 0; i<N; i++){
		solve_case(i+1);
	}
}

static void solve_case(int cn)
{
	int NA,NB;

	scanf("%d",&turnaround);
	scanf("%d",&NA);
	scanf("%d",&NB);
	
	avail[0] = avail[1] = 0;
	need[0] = need[1] = 0;

	Target target = B;
	for(int i = 0; i < NA; i++){
		add_dep(target);
	}

	target = A;
	for(int i = 0; i < NB; i++){
		add_dep(target);
	}
	
	//simulate	
	while(!agenda.empty()){
		Entry * e = agenda.top();
		agenda.pop();
		e->process();
	}

	printf("Case #%d: %d %d\n", cn, need[0], need[1]);
	
}

static void add_dep(Target target){
	int m1,h1,h2,m2;

	scanf("%d:%d %d:%d",&h1,&m1,&h2,&m2);

 	Departure * nd = new Departure(Time(h1,m1),Time(h2,m2), target);
 	agenda.push(nd);
}

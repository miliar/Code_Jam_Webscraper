#include <string>
#include <vector>
#include <cstdio>
#include <iostream>
#include <cstdlib>
#include <algorithm>
#include <sstream>
#include <set>
#include <cmath>
#include <queue>

using namespace std;

#define FOR(i,a,b) for(int i=(a);i<(b);++i)
#define REP(i,n) FOR(i,0,n)
#define FORE(it,x) for(typeof((x).begin())it=(x).begin();it!=(x).end();++it)
#define all(x) (x).begin(),(x).end()
#define CLR(x,v) memset(x,v,sizeof(x))
#define pb push_back
#define sz size()
#define exist(c,x) ((c).find(x)!=(c).end())
#define cexist(c,x) (find(all(c),x)!=(c).end())

enum {
    TRAIN_AVAILABLE,
    TRAIN_NEEDED
};

class event {
public:
    int time;	// minutes from 0
    int kind;	// enum
    int side;	// 0 on A, 1 on B
    int dtime;  // arrival time

    bool operator > (const event &a) const {
	if (time < a.time) return true;
	if (time > a.time) return false;

	if (kind < a.kind) return true;
	if (kind > a.kind) return false;

	if (side < a.side) return true;
	if (side > a.side) return false;

	if (dtime < a.dtime) return true;
	if (dtime > a.dtime) return false;

	return true;
    }

    bool operator < (const event &a) const {
	return !(*this > a);
    }


};

int convert_time_to_mins(char *a) {
    int h, m;
    sscanf(a, "%d:%d", &h, &m);
    return h * 60 + m;
}


int main(int argc, char *argv[]) {
    int T;
    if (argc >= 2) {
	freopen(argv[1], "r", stdin);
    }
    scanf("%d", &T);
    for (int t = 1; t <= T; t++) {
	printf("Case #%d: ", t);
	int T;
	int na;
	int nb;

	priority_queue<event> equeue;

	scanf("%d", &T);
	scanf("%d %d", &na, &nb);

	REP(i, na) {
	    event e;
	    char deptime[128], arrtime[128];
	    scanf("%s %s", deptime, arrtime);
	    e.time = convert_time_to_mins(deptime);
	    e.dtime = convert_time_to_mins(arrtime) + T;
	    e.kind = TRAIN_NEEDED;
	    e.side = 0;
	    equeue.push(e);
	}

	REP(i, nb) {
	    event e;
	    char deptime[128], arrtime[128];
	    scanf("%s %s", deptime, arrtime);
	    e.time = convert_time_to_mins(deptime);
	    e.dtime = convert_time_to_mins(arrtime) + T;
	    e.kind = TRAIN_NEEDED;
	    e.side = 1;
	    
	    equeue.push(e);
	}

	int tA = 0; int tB = 0;
	int lA = 0;
	int lB = 0;

	while (!equeue.empty()) {
	    event e = equeue.top();
	    equeue.pop();
	    switch(e.kind) {
	    case TRAIN_AVAILABLE:
		if (e.side == 0) lA++; else lB++;
		break;
	    case TRAIN_NEEDED:
		if (e.side == 0) {
		    if (lA == 0) { tA++; lA++; };
		    lA--;
		}
		else {
		    if (lB == 0) { tB++; lB++; };
		    lB--;
		}
		event ne;
		CLR(&ne, 0);
		ne.time = e.dtime;
		ne.dtime = e.dtime;
		ne.kind = TRAIN_AVAILABLE;
		ne.side = 1 - e.side;
		equeue.push(ne);
		break;
	    }
	}

	printf("%d %d\n", tA, tB);



    }

    return 0;
}

#include <iostream>
#include <vector>
#include <algorithm>
#include <map>
#include <sstream>
using namespace std;

struct instruction {
    char rob;
    int button;
};

struct robot {
    char name;
    int pos;
    int ip;
};

//globals

int cur, times;
bool curDone;
instruction store[110];
robot Blue, Orange;


void getNextIp(robot &r) {
    do {
        r.ip = r.ip + 1;
    }while(store[r.ip].rob == r.name);
}

void runRobot(robot &r) {
    int goal;
    char x;
    goal = store[r.ip].button;
    if(goal == 0) {
        x = '0';
    } else if(r.pos != goal) {
        if(goal > r.pos) {
            r.pos = r.pos + 1;
        } else {
            r.pos = r.pos - 1;
        }
    } else {
        if(r.ip == cur) {
            getNextIp(r);
            curDone = true;
            x = 'p';
        } else {
            x = 'w';
        }
    }
}
    


int main() {
    int i,j,k,m;
	int prob;
	char c;
	int T, N, ret;
	scanf("%d", &T);
	for(int cases = 0; cases < T; cases++) {
	    scanf("%d", &N);
	    for(int p=0; p < N; p++) {
	        int a;
	        char c;
	        cin >> c >> a;
	        store[p].rob = c;
	        store[p].button = a;
	    }
	    store[N].rob = 'B'; 
	    store[N+1].rob = 'O';
	    store[N].button = 0;
	    store[N+1].button = 0;
	    
	    Blue.name = 'B';
		Blue.pos = 1; 
		Blue.ip = -1;
		getNextIp(Blue);
		
		Orange.name = 'O';
		Orange.pos = 1;
		Orange.ip = -1;
		getNextIp(Orange);
		
		times = 1;
		cur = 0;
		curDone = false;
		
		while(cur < N ) {
		    runRobot(Orange);
			runRobot(Blue);
			if(curDone) {
			    curDone = false;
			    cur += 1;
			}
			times += 1;
		}
	    printf("Case #%d: %d\n", cases+1, times-1);
	}
    return 0;
}
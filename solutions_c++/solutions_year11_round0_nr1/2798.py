#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <cctype>
#include <iostream>
#include <string>
#include <set>
#include <map>
#include <list>
#include <queue>
#include <stack>
#include <vector>
#include <deque>
#include <algorithm>
#include <functional>

using namespace std;

typedef long long int int64_t;
typedef long long unsigned int uint64_t;

struct Command {
	char robot;
	int position;
	Command(int tr, int tp): robot(tr), position(tp)
	{}
};

int main(int argc, char *argv[])
{
	int T;
	scanf("%d", &T);
	for(int ts=1;ts<=T;ts++){
		int n;
		scanf("%d", &n);
		char cmd[2];
		queue<Command> tcmd;
		queue<int> ocmd, bcmd;
		for(int i=0;i<n;i++){
			int pos;
			scanf("%s%d", cmd, &pos);
			tcmd.push(Command(cmd[0], pos));
			if(cmd[0] == 'O')
				ocmd.push(pos);
			else
				bcmd.push(pos);
		}
		ocmd.push(-1);
		bcmd.push(-1);
		int time = 0;
		int robot_b = 1, robot_o = 1;
		while(!tcmd.empty()){
			Command ncmd(tcmd.front());
			const int target_push = ncmd.position;
			const int target_move = ( ncmd.robot == 'O' ? bcmd.front() : ocmd.front() );
			int &rb_push = (ncmd.robot == 'O' ? robot_o : robot_b);
			int &rb_move = (ncmd.robot == 'O' ? robot_b : robot_o);
			const int used_time = abs(ncmd.position - rb_push) + 1;
			time += used_time;
			//printf("move: %d->%d, push: %d->%d\n", rb_move, target_move, rb_push, target_push);
			//printf("time += %d\n", used_time);
			if(abs(target_move - rb_move) <= used_time)
				rb_move = target_move;
			else
				rb_move = rb_move + used_time * (rb_move < target_move ? 1:-1);
			rb_push = target_push;
			//printf("push: %d, move:%d\n", rb_push, rb_move);
			if(ncmd.robot == 'O')
				ocmd.pop();
			else
				bcmd.pop();
			tcmd.pop();
		}
		printf("Case #%d: %d\n", ts, time);
	}
	return 0;
}


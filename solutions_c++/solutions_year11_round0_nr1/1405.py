#include <iostream>
#include <cstdio>
#include <algorithm>
#include <vector>
#define PB push_back
#define MAXN 110
using namespace std;
const int O = 0;
const int B = 1;

vector<int> move[2];
int numTests, curTime, nextAction, curPosition[2], whichRobot[MAXN], n, position[MAXN];
vector<int> :: iterator nextMove[2];
char robot;
bool click;


void moveRobots(const int robot, bool &click){
	if(nextMove[robot] == move[robot].end())
		return ;
	if(click == false && curPosition[robot] == *nextMove[robot] && whichRobot[nextAction] == robot){
		click = true;
		nextAction++;
		nextMove[robot]++;
	}
	else if(curPosition[robot] < *nextMove[robot])
		curPosition[robot] ++;
	else if(curPosition[robot] > *nextMove[robot])
		curPosition[robot] --;
}

int main(){
	scanf("%d",&numTests);
	for(int test=1; test<=numTests; test++){
		scanf("%d",&n);
		move[O].clear();
		move[B].clear();
		for(int i=1; i<=n; i++){
			scanf(" %c %d",&robot,&position[i]);
			whichRobot[i] = (robot=='O')?0:1;
			move[(robot=='O')?0:1].PB(position[i]);
		}
		nextMove[O] = move[O].begin();
		nextMove[B] = move[B].begin();
		curPosition[O] = 1;
		curPosition[B] = 1;
		nextAction = 1;
		curTime = 0;
		while(nextMove[O] != move[O].end() || nextMove[B] != move[B].end()){
			curTime ++;
			click = false;
			moveRobots(O,click);
			moveRobots(B,click);
		}
		printf("Case #%d: %d\n",test,curTime);
	}
}

#include <stdio.h>

char R[128];
int P[128];
int N;

int getNextPos(char rob, int pos){
	for(int i=pos;i<N;i++){
		if(R[i]==rob)
			return P[i];
	}
	return -1;
}

void go(char rob, int* start, int goal){
	if(goal == -1)
		return;
	if(goal > *start){
		*start += 1;
	} else if(goal < *start){
		*start -= 1;
	}
}

void run(int fall){
	scanf("%d", &N);
	for(int i=0; i<N; i++){
		scanf("%s %d", R+i, &P[i]);
	}
	int oPos = 1;
	int bPos = 1;

	int oGoal = getNextPos('O', 0);
	int bGoal = getNextPos('B', 0);
	int time=0;
	
	int i=0;
	while(i<N){
		if((R[i] == 'O' && P[i] == oPos)){
			time++;
			go('B', &bPos, bGoal);
			oGoal = getNextPos('O', ++i);
			continue;
		} else if((R[i] == 'B' && P[i] == bPos)){
			time++;
			go('O', &oPos, oGoal);
			bGoal = getNextPos('B', ++i);
			continue;
		} else {
			time++;
			go('B', &bPos, bGoal);
			go('O', &oPos, oGoal);
		}
	}
	printf("Case #%d: %d\n", fall+1, time);
}

int main() {
	int T;
	scanf("%d", &T);
	for(int i=0; i<T; i++){
		run(i);
	}
}



#ifdef HAVE_CONFIG_H
#include <config.h>
#endif

#include <iostream>
#include <cstdlib>
#include <stdio.h>

using namespace std;

// Max of input read in a single string
#define MAX_READ 10000

typedef struct AcStruct{
	int button;
	char   robot;
};

typedef struct AcRobStruct{
	int button;
	int curButton;
	int curAction;
	char   robot;
};


// buffer to get all inputs
char input[MAX_READ];


// Read all items of a file
void  fillListActions(FILE *wIn, AcStruct *wStruct, unsigned int *wNumAction){
	// get the number of case
	fgets(input,10000,wIn);
	char aux[100];
	int ict,act;
	// total number action

	ict = act = 0;
	while (input[ict] != ' '){
		aux[act++] = input[ict++];
	}
	aux[act++] = '\0';
	*wNumAction = atoi(aux);
	for (unsigned int i = 0;i<*wNumAction;i++){
		while (input[ict] == ' ') ict++;
		wStruct[i].robot = input[ict++];
		while (input[ict] == ' ') ict++;
		act = 0;
		while ((input[ict] != ' ')  && (input[ict] != '\n') && (input[ict] != '\0'))  {
			aux[act++] = input[ict++];
		}
		aux[act++] = '\0';
		wStruct[i].button = atoi(aux);
	}
}

// fill the action of robot
void fillRobotAction(AcRobStruct *wRobot,AcStruct *wStruct, unsigned int wNumAction){
	for (int curr = wRobot->curAction+1; curr < wNumAction;curr++){
		if (wStruct[curr].robot == wRobot->robot){
			wRobot->curAction = curr;
			wRobot->button = wStruct[curr].button;
			return;
		}
	}
	wRobot->curAction = wNumAction+1;
}

// process a robot action
void runActionRobot(AcRobStruct *wRobotA, AcRobStruct *wRobotB){
	// when robot A as the next action
	if (wRobotA->curAction <= wRobotB->curAction){
		// now A will push the button
		if (wRobotA->curButton == wRobotA->button) {
			// robot A push
			wRobotA->button = -1;
			printf("  Robot A : push  ");
			// robot B can move
			if ((wRobotB->curButton != wRobotB->button) && (wRobotB->button != -1)){
				if (wRobotB->curButton < wRobotB->button){
					wRobotB->curButton++;
				}
				else{
					wRobotB->curButton--;
				}
				printf("  Robot B : walk  ");
			}
			else{
				printf("  Robot B : wait  ");
				// he need to wait for the A
			}
		}
		else{
			if (wRobotA->curButton < wRobotA->button){
				wRobotA->curButton++;
			}
			else{
				wRobotA->curButton--;
			}
			printf("  Robot A : walk  ");
			if ((wRobotB->curButton != wRobotB->button)  && (wRobotB->button != -1)){
				if (wRobotB->curButton < wRobotB->button){
					wRobotB->curButton++;
				}
				else{
					wRobotB->curButton--;
				}
				printf("  Robot B : walk  ");
			}
			else{
				// he need to wait for the A
				printf("  Robot B : wait  ");
			}
		}
	}
	// when robot B as the next action
	else{
		if (wRobotB->curButton == wRobotB->button){
			// robot A push
			wRobotB->button = -1;
			printf("  Robot B : push  ");
			// robot B can move
			if ((wRobotA->curButton != wRobotA->button) && (wRobotA->button != -1)){
				if (wRobotA->curButton < wRobotA->button){
					wRobotA->curButton++;
				}
				else{
					wRobotA->curButton--;
				}
				printf("  Robot A : walk  ");
			}
			else{
				printf("  Robot A : wait  ");
				// he need to wait for the B
			}
		}
		else{
			if (wRobotB->curButton < wRobotB->button){
				wRobotB->curButton++;
			}
			else{
				wRobotB->curButton--;
			}
			printf("  Robot B : walk  ");
			if ((wRobotA->curButton != wRobotA->button) && (wRobotA->button != -1)){
				if (wRobotA->curButton < wRobotA->button){
					wRobotA->curButton++;
				}
				else{
					wRobotA->curButton--;
				}
				printf("  Robot A : walk  ");
			}
			else{
				printf("  Robot A : wait  ");
				// he need to wait for the A
			}
		}
	}

	}


int main(int argc, char *argv[]){

// 	if (argc != 2){
// 		printf(" Error, I need the input file as \"input\"");
// 		exit(1);
// 	}

	//FILE *in = fopen(argv[1],"r");
	FILE *in = fopen("input","r");
	FILE *out = fopen("out","w");


	// array of posible actions
	AcStruct actions[101];

	// current Blue/Orange  Action
	AcRobStruct OneAction;

	// current Orange/Blue Action
	AcRobStruct TwoAction;

	// number of input
	unsigned int numInput = 0;

	// get the number of case
	fgets(input,10000,in);

	// total number of actions
	unsigned int totAction = 0;

	numInput = atoi(input);

	// current number of time
	unsigned int timeCount = 0;

	for (unsigned int cCase = 0;cCase < numInput;cCase++){
		 fillListActions(in,actions,&totAction);
		 // get the first robot action
		 if (actions[0].robot == 'O'){
			 OneAction.robot = 'O';
			 TwoAction.robot = 'B';
		}
		else{
			OneAction.robot = 'B';
			TwoAction.robot = 'O';
		}
		OneAction.button = -1;
		TwoAction.button = -1;
		OneAction.curButton = 1;
		TwoAction.curButton = 1;
		OneAction.curAction = -1;
		TwoAction.curAction = -1;

		timeCount = 0;
		while (true){
			timeCount++;
			if (OneAction.button == -1){
				fillRobotAction(&OneAction,actions,totAction);
			}
			if (TwoAction.button == -1){
				fillRobotAction(&TwoAction,actions,totAction);
			}
			if ((OneAction.button == -1) && (TwoAction.button == -1)){
				timeCount--;
				printf("\n Case #%d: %d\n",cCase+1,timeCount);
				sprintf(input,"Case #%d: %d\n",cCase+1,timeCount);
				fputs(input,out);
				fflush(out);
				break;
			}
			printf("\n TIME : %d ",timeCount);
			runActionRobot(&OneAction,&TwoAction);
		}
		int num;
	}
	fclose(out);
  return EXIT_SUCCESS;
}

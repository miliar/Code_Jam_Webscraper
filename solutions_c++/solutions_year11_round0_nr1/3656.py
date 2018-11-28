#include <bot_trust.h>


//void readParams(ifstream& fd, char command[][2]){
//	return 0;
//}


int searchRobotCommandOrder(COMMAND command[], int size, char color, int nOrder){
	int order = 0;

	for( int i = 0; i < size; i++){
		if(command[i].robotColor == color){
			order++;
			if(order == nOrder)
				return command[i].buttonNum;
		}
	}
}

bool isLastCommand(COMMAND command[], int size,  char color, int nOrder){
	int maxOrder = 0;
	for( int i = 0; i < size; i++){
		if(command[i].robotColor == color)
			maxOrder++;
	}

	if(maxOrder == nOrder)
		return true;
	else return false;
}








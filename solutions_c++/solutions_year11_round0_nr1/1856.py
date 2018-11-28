//google code jam qualification a
#include <stdio.h>

const int maxn=101;

typedef struct node{
	bool isBlue;
	int buttonIndex;
}node;

node list[maxn];
int n;

void inputData(){
	scanf("%d", &n);
	char ch;
	for (int i=0; i<n; i++){
		scanf("%*c%c%d", &ch, &list[i].buttonIndex);
		if (ch=='B') list[i].isBlue=true;
		else list[i].isBlue=false;
	}
}

int abs(int val){
	return val>=0? val : -val;
}

int main(){
	int caseT, caseIndex;
	scanf("%d", &caseT);
	for ( caseIndex=1; caseIndex<=caseT; caseIndex++){
		inputData();
		int time[2]={0,0}, pos[2]={1,1};
		bool lastIsBlue;

		lastIsBlue=list[0].isBlue;
		time[lastIsBlue]=pos[lastIsBlue]=list[0].buttonIndex;
		
		for (int i=1; i<n; i++){
			int distance=abs(list[i].buttonIndex-pos[list[i].isBlue]);
			if (lastIsBlue==list[i].isBlue){
				time[lastIsBlue]+=distance+1;
				pos[lastIsBlue]=list[i].buttonIndex;
			}else {
				lastIsBlue=list[i].isBlue;
				time[lastIsBlue]+=distance;
				if (time[lastIsBlue]<time[!lastIsBlue])
					time[lastIsBlue]=time[!lastIsBlue];
				time[lastIsBlue]++;
				pos[lastIsBlue]=list[i].buttonIndex;
			}
		}

		int answer=time[0];
		if (time[1]>answer) answer=time[1];
		printf("Case #%d: %d\r\n", caseIndex, answer);
	}

	return 0;
}
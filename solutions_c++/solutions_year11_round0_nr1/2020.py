#include <stdio.h>
#include <stdlib.h>

int work();
void init();
int calc();
int main(){
	int cas;
	scanf("%d",&cas);
	for (int ti=1; ti<=cas;ti++){
		printf("Case #%d: %d\n",ti,work());
	}
	return 0;
}
const int MAX_BUFF_LEN = 150;
int list[MAX_BUFF_LEN][2];
int num=0;
int work(){
	init();
	return calc();
}

void init(){
	scanf("%d",&num);
	char type[10];
	int pos;
	for (int i=0;i<num;i++){
		scanf("%s%d",type,&pos);
		list[i][0] = (type[0]=='B'?0:1);
		list[i][1] = pos;
//		printf("type:%c  %d pos: %d\n",type[0],list[i][0],list[i][1]);
	}
	
}

int curr=0;
class Robot{
public:
	Robot(){
		pos=1;
		time=0;
	}
	int pos;
	int time;
	void move(int ind){
		time += abs(pos-list[ind][1]);
		pos = list[ind][1];
		if (curr<time){
			time++;
			curr = time;
		}else{
			curr++;
			time = curr;
		}
	}
};
int calc(){
	Robot blue , orange;
	curr=0;
	for (int i=0;i<num;i++){
		// run
		if (0==list[i][0]){ // blue
			blue.move(i);
		}else{
			orange.move(i);
		}
	}		
	return curr;
}

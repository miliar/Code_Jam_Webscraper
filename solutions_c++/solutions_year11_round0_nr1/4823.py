#include<iostream>
#include<cmath>
#include<cstdio>
using namespace std;

int main(){

int numTest;
scanf("%d",&numTest);

int i=0;
while (i++<numTest){
	int num,time=0;
	char bot;
	int button;
	int tempTime;
	int botOtime=0, botBtime=0, botOpos=1, botBpos=1;
	scanf("%d",&num);
	while(num--){
 		scanf(" %c %d",&bot,&button);
		if(bot=='O'){
			tempTime = abs((double)(botOpos-button))+1;
			botOpos = button;
			if(tempTime + botOtime <= time)
				++time;
			else
				time = tempTime + botOtime;
			botOtime = time;
		}
	
		if(bot=='B'){
			tempTime = abs((double)(botBpos-button))+1;
			botBpos = button;
			if(tempTime + botBtime <= time)
				++time;
			else
				time = tempTime + botBtime;
			botBtime = time;
		}
	}
	printf("Case #%d: %d\n",i,time);
}
	return(0);
}


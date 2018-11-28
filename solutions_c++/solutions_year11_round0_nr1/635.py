#include <stdio.h>
#include<stdlib.h>
#include<math.h>

int cost(int step,int size,int last_time){//color different
	if(abs(step-size) <=last_time)
	return 1;
	else
	return abs(step-size) - last_time +1;
}
	
void run(int casen) {
	int n=0;
	//scanf("%s",s); n=strlen(s);
	int orange=1;
	int blue=1;
	int total=0;
	
	char player='O';
	int step=0;
	int time=0;
	
	int last_time=0;
	char last_player='O';
	
	
	
	scanf("%d",&n);

	//{
	
	scanf("%c",&player);
	scanf("%c",&player);
	scanf("%d",&step);
	last_player=player;//
	if(player=='O'){
		time=abs(step-orange)+1;
		orange=step;
	}
	else{
		time=abs(step-blue)+1;
		blue=step;
	}
	last_time+=time;
	total+=time;
	
	
	
	last_player=player;
	
	//}
	for(int i=1;i<n;i++){
	
		scanf("%c",&player);
		scanf("%c",&player);
		scanf("%d",&step);
		
		//ever step
		if(player==last_player){
			if(player=='O'){
				time=abs(step-orange)+1;
				orange=step;
			}
			else{
				time=abs(step-blue)+1;
				blue=step;
			}
			last_time+=time;
		}
		else{
			if(player=='O'){
				time=cost(step,orange,last_time);
				orange=step;
			}
			else{
				time=cost(step,blue,last_time);
				blue=step;
			}
			last_time=time;
			last_player=player;
		}
		total+=time;
		
	}
	
	printf("Case #%d: %d\n",casen,total);
}

int main(int argc, char* argv[]) {
	int ncases=0;
	freopen(argv[1], "rt", stdin);
	freopen("A.out", "wt", stdout);
	scanf("%d",&ncases); 
	for(int i=1;i<=ncases;i++) run(i);
	
	return 0;
}

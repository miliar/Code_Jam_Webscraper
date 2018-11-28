#include <stdio.h>
int main(){
	unsigned int cases=0;
	scanf("%d",&cases);
	int itr=0;
	while(cases--){
		int res=0;
		int totMoves=0;
		int bpos=1;
		int opos=1;
		int prevs=0;
		scanf("%d",&totMoves);
			bool isBlue=false;

		while(totMoves--){
			int buttonPos=0;
			char c;
			scanf("%c",&c);
			scanf("%c",&c);
			scanf("%d",&buttonPos);
			if(c =='O'){
				//orange hallway
//printf("Orange at %d has to move to %d\n",opos,buttonPos);
				int move=buttonPos-opos;
				if(move<0) move*=-1;
				if(isBlue){if(move<=prevs) {move=0;}else{move-=prevs;}				isBlue=false;prevs=0;}
				res+=(move+1);
				prevs+=(move+1);
				opos=buttonPos;
//				printf("Orange moved move elapsed %d res %d new position %d\n",prevs,res,buttonPos);
				}else{
				//blue hallway
//printf("Blue at %d has to move to %d\n",bpos,buttonPos);
				int move=buttonPos-bpos;
				if(move<0) move*=-1;
				if(!isBlue){if(move<=prevs) {move=0;}else{move-=prevs;}
				isBlue=true;prevs=0;}

				res+=(move+1);
				prevs+=(move+1);
				bpos=buttonPos;
//printf("Blue moved move elapsed %d res %d new position %d\n",prevs,res,buttonPos);
				}
		}
		printf("Case #%d: %d\n",++itr,res);
	}
return 0;
}

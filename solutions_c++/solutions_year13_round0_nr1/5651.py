#include <stdio.h>
#include <stdlib.h>
#include <math.h>

#include <string>
#include <vector>

using namespace std;

#define abs(n) (n<0?-n:n)

int main(){
	int T,i;
	scanf("%d\n",&T);
	
	for(i=0;i<T;i++){
		int complete=1; //1 if all moves completed, 0 if there are still moves to make
		int rowsums[]={0,0,0,0},colsums[]={0,0,0,0},diagsums[]={0,0}; //row sums, col sums, diagonal sums
		int tlocs[]={-1,-1,-1}; //locations of the t for row, column, and diagonal
		int endgame=0; //game has ended
		int r,c;
		for(r=0;r<4;r++){
			for(c=0;c<4;c++){
				char ch;
				switch(ch=getchar()){
					case '.':
						complete=0;
						break;
					case 'X': //X is +1
						rowsums[r]++;
						colsums[c]++;
						if(r==c)
							diagsums[0]++; //0 is forward diagonal from 0,0 to 3,3
						else if(r+c==3)
							diagsums[1]++; //1 is backward diagonal from 3,0 to 0,3
						break;
					case 'O': //O is -1
						rowsums[r]--;
						colsums[c]--;
						if(r==c)
							diagsums[0]--; //0 is forward diagonal from 0,0 to 3,3
						else if(r+c==3)
							diagsums[1]--; //1 is backward diagonal from 3,0 to 0,3
						break;
					case 'T':
						tlocs[0]=r;
						tlocs[1]=c;
						if(r==c)
							tlocs[2]=0; //0 is forward diagonal from 0,0 to 3,3
						else if(r+c==3)
							tlocs[2]=1; //1 is backward diagonal from 3,0 to 0,3
						break;
				}
				if(abs(rowsums[r])==4||abs(rowsums[r])==3&&tlocs[0]==r){
					printf("Case #%d: %c won\n",i+1,rowsums[r]<0?'O':'X');
					endgame=1;
				}
				else if(abs(colsums[c])==4||abs(colsums[c])==3&&tlocs[1]==c){
					printf("Case #%d: %c won\n",i+1,colsums[c]<0?'O':'X');
					endgame=1;
				}
			}
			while(getchar()!='\n'); //line ending
		}
		while(getchar()!='\n'); //line ending
		if(!endgame){
			if(abs(diagsums[0])==4||abs(diagsums[0])==3&&tlocs[2]==0)
				printf("Case #%d: %c won\n",i+1,diagsums[0]<0?'O':'X');
			else if(abs(diagsums[1])==4||abs(diagsums[1])==3&&tlocs[2]==1)
				printf("Case #%d: %c won\n",i+1,diagsums[1]<0?'O':'X');
			else if(complete)
				printf("Case #%d: Draw\n",i+1);
			else
				printf("Case #%d: Game has not completed\n",i+1);
		}
	}
}

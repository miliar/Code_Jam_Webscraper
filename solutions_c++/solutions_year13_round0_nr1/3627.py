#include<cstdio>

using namespace std;

int tc;
char data[5][5];
int main(){
	int i,j,k;
	int c,co,cx,ho,hx,vo,vx,ht,vt,o1,o2,x1,x2,t1,t2;
	freopen("a2.in", "r", stdin);
	freopen("a2.out","w",stdout);
	scanf("%d",&tc);
	for(int tcc=1;tcc<=tc;tcc++){
		for(i=0;i<4;i++){
			scanf(" %s",&data[i]);
		}
		co=cx=c=0;
		o1=o2=x1=x2=t1=t2=0;
		for(i=0;i<4;i++){
			for(j=0;j<4;j++)
				if (data[i][j]=='.') c=1;
			ho=hx=vo=vx=ht=vt=0;
			for(j=0;j<4;j++){
				switch(data[i][j]){
				case 'O':
					ho++;
					break;
				case 'X':
					hx++;
					break;
				case 'T':
					ht=1;
					break;
				}
				switch(data[j][i]){
				case 'O':
					vo++;
					break;
				case 'X':
					vx++;
					break;
				case 'T':
					vt=1;
					break;
				}
			}
			switch(data[i][i]){
				case 'O':
					o1++;
					break;
				case 'X':
					x1++;
					break;
				case 'T':
					t1=1;
					break;
			}
			switch(data[i][3-i]){
				case 'O':
					o2++;
					break;
				case 'X':
					x2++;
					break;
				case 'T':
					t2=1;
					break;
			}
			if (ho+ht==4 || vo+vt==4 || o1+t1==4 || o2+t2==4) co=1;
			if (hx+ht==4 || vx+vt==4 || x1+t1==4 || x2+t2==4) cx=1;
		}
		printf("Case #%d: ",tcc);
		if (!(cx^co)){
			if (c){
				printf("Game has not completed\n");
			}else{
				printf("Draw\n");
			}
		} else if (co) {
			printf("O won\n");
		} else { //X
			printf("X won\n");
		}
	}
	return 0;
}

/*

Input 
 
6
XXXT
....
OO..
....

XOXT
XXOO
OXOX
XXOO

XOX.
OX..
....
....

OOXX
OXXX
OX.T
O..O

XXXO
..O.
.O..
T...

OXXX
XO..
..O.
...O

Case #1: X won
Case #2: Draw
Case #3: Game has not completed
Case #4: O won
Case #5: O won
Case #6: O won
*/
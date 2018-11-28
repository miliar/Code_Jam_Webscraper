#include <cstdio>
#include <cstring>
#include <cmath>
#include <vector>
#include <queue>
#include <stack>
#include <map>
#include <list>
#include <utility>
#include <string>
#include <algorithm>
#define infinity 2139062143
#define swap(x, y) (x) ^= (y) ^= (x) ^= (y)
#define foreach( i, n )  for(int (i) = 0; (i) < (n); ++(i))
#define min( x, y )  ( ((x) < (y)) ? (x) : (y) )
#define ma(angry) x, y )  ( ((x) > (y)) ? (x) : (y) )
#define abs( x ) (((x) < 0)? (-x) : (x) )
#define full 100

using namespace std;

int main () {
	
	int jogo[4][4];
	int n,i,j,X,Y, XT, YT, XL, YL, cont, XA, YA, XB, YB, XC, YC, XD, YD;
	char tag;
	bool check ;
	
	while(true)
	{
		scanf("%d", &n);
		
		for(int x = 0; x < n ; x++)
		{
			check = true;
			XT = 0;
			YT = 0;
			XL = 0;
			YL = 0;
			cont = 0;
			
			for(i = 0; i <= 3; i++)
			{	X = 0;
				Y = 0;
				
				for(j = 0; j <= 3; j++)
				{
					scanf(" %c ", &tag);
					
						if(tag == 'X'){
							jogo[i][j] = 1;
							cont++;
						}
						else if(tag == 'O'){
							jogo[i][j] = 2;
							cont++;
						}else if(tag == 'T'){
							jogo[i][j] = 3;
							cont++;
						}else{
							jogo[i][j] = 4;
						}
						if(jogo[i][j] == 1 || jogo[i][j] == 3){
							X++;
						}else if(jogo[i][j] == 2 || jogo[i][j] == 3){
							Y++;
						}
						
						if(i == j){
							if(jogo[i][j] == 1 || jogo[i][j] == 3){
								XT++;
							}
							if(jogo[i][j] == 2 || jogo[i][j] == 3){
								YT++;
							}
						}
						
						if(i == 0 && j == 3){
							if(jogo[i][j] == 1 || jogo[i][j] == 3){
								XL++;
							}
							if(jogo[i][j] == 2 || jogo[i][j] == 3){
								YL++;
							}
						}
						
						if(i == 1 && j == 2){
							if(jogo[i][j] == 1 || jogo[i][j] == 3){
								XL++;
							}
							if(jogo[i][j] == 2 || jogo[i][j] == 3){
								YL++;
							}
						}
						
						if(i == 2 && j == 1){
							if(jogo[i][j] == 1 || jogo[i][j] == 3){
								XL++;
							}
							if(jogo[i][j] == 2 || jogo[i][j] == 3){
								YL++;
							}
						}
						
						if(i == 3 && j == 0){
							if(jogo[i][j] == 1 || jogo[i][j] == 3){
								XL++;
							} 
							if(jogo[i][j] == 2 || jogo[i][j] == 3){
								YL++;
							}
						}
					if(check == true)	
					{
						if(X == 4){
							printf("Case #%d: X won\n",x+1);
							check = false;
						}
						else if(Y == 4){
							printf("Case #%d: O won\n",x+1);
							check = false;
						}
					}	
				}
				
			}
			XA = YA = XB = YB = XC = YC = XD = YD = 0;
			for(i = 0; i < 4; i++)
			{
				for(j = 0; j < 4; j++)
				{
					if(j == 0)
					{
						if(jogo[i][j] == 1 || jogo[i][j] == 3){
								XA++;
							} 
							if(jogo[i][j] == 2 || jogo[i][j] == 3){
								YA++;
							}
					}
					if(j == 1)
					{
						if(jogo[i][j] == 1 || jogo[i][j] == 3){
								XB++;
							} 
							if(jogo[i][j] == 2 || jogo[i][j] == 3){
								YB++;
							}
					}
					if(j == 2)
					{
						if(jogo[i][j] == 1 || jogo[i][j] == 3){
								XC++;
							} 
							if(jogo[i][j] == 2 || jogo[i][j] == 3){
								YC++;
							}
					}
					if(j == 3)
					{
						if(jogo[i][j] == 1 || jogo[i][j] == 3){
								XD++;
							} 
							if(jogo[i][j] == 2 || jogo[i][j] == 3){
								YD++;
							}
					}
				}
			}
			
			if(check == true)
			{		if(XA == 4){
			printf("Case #%d: X won\n",x+1);
							check = false;
					}
					else if(YA == 4){
					printf("Case #%d: O won\n",x+1);
						check = false;
					}
					else if(XB == 4){
					printf("Case #%d: X won\n",x+1);
							check = false;
					}
					else if(YB == 4){
					printf("Case #%d: O won\n",x+1);
						check = false;
					}
					else if(XC == 4){
					printf("Case #%d: X won\n",x+1);
							check = false;
					}
					else if(YC == 4){
					printf("Case #%d: O won\n",x+1);
						check = false;
					}
					else if(XD == 4){
					printf("Case #%d: X won\n",x+1);
							check = false;
					}
					else if(YD == 4){
					printf("Case #%d: O won\n",x+1);
						check = false;
					}
					else if(XT == 4){
						printf("Case #%d: X won\n",x+1);
						check = false;
					}
					else if(YT == 4){
						printf("Case #%d: O won\n",x+1);
						check = false;
					}else if(XL == 4){
						printf("Case #%d: X won\n",x+1);
						check = false;
					}
					else if(YL == 4){
						printf("Case #%d: O won\n",x+1);
						check = false;
					}else if(cont == 16){
						printf("Case #%d: Draw\n", x+1);
						check = false;
					}else {
						printf("Case #%d: Game has not completed\n", x+1);
						check = false;
					}
			}
			
				
		}
		
		break;
	}
 
	return 0;
}
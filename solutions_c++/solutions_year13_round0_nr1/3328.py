#include <iostream>
using namespace std;

#define OWON 	0
#define XWON 	1
#define DRAW 	2
#define GHNC 	3


// utiliser comme ./speaktong < fin > fout

int main(int argc, char **argv)
{

(void)argc,(void)argv;

	char result[4][25] = {"O won","X won","Draw","Game has not completed"};
	int r;
	
	char **board = (char**) malloc(4*sizeof(char*));
	for(int i = 0; i < 4 ; i++)
		board[i] = (char*) malloc(4*sizeof(char));
		
	char c;
	
	char res[10]; // 4 linhas + 4 colunas + duas diagonais

	int nt; // number of test cases (lines of file)
	scanf("%d",&nt);
	scanf("%c",&c);
	for(int i = 0; i < nt; i++) // (tests)
	{
		for(int k = 0; k < 4; k++) //cada linhas
		{
			res[k] = 0xFF;
			for(int j = 0; j < 4; j++) // cada coluna da linha
			{
				scanf("%c",&(board[k][j]));
				res[k] = res[k] & board[k][j]; //colunas
				//alg
				//end alg
			}
			scanf("%c",&c);
			//cout << "res[k]=" << (int)res[k] << endl;
		}
		scanf("%c",&c);

			//colunas
			for(int w = 0; w < 4; w++)
			{
				res[4+w] = 0xFF;
				for(int j = 0; j < 4; j++)
					res[4+w] = res[4+w] & board[j][w];
			//cout << "res[k]=" << (int)res[4+w] << endl;
			}
			//diagonais
			res[8] = 0xFF; res[9] = 0xFF;
			for(int w = 0; w < 4; w++)
			{
				res[8] = res[8] & board[w][w];
				res[9] = res[9] & board[w][3-w];
			}
			//final
			r = DRAW;
			for(int j = 0; j < 10; j++)
			{
				if((res[j] & 4) && (res[j] & 64))
				{
					r = OWON;
					break;
				}
				else if((res[j] & 16) && (res[j] & 64))
				{
					r = XWON;
					break;
				}
				else if((~res[j]) & 64)
					r = GHNC;
			}
		
		cout << "Case #" << i+1 << ": " << result[r] << endl;
	}
	return 0;
}



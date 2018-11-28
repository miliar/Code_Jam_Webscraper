#include <cstdio>
using namespace std;
int mapper[30]  = {0};
/**mapper[('Q'-'A')] = 1;
mapper['W'-'A'] = 2;
mapper['E'-'A'] = 3;
mapper['R'-'A'] = 4;
mapper['A'-'A'] = 5;
mapper['S'-'A'] = 6;
mapper['D'-'A'] = 7;
mapper['F'-'A'] = 8;
**/
int main()
{
	int T;
	scanf("%d",&T);
	mapper[('Q'-'A')] = 1;
mapper['W'-'A'] = 2;
mapper['E'-'A'] = 3;
mapper['R'-'A'] = 4;
mapper['A'-'A'] = 5;
mapper['S'-'A'] = 6;
mapper['D'-'A'] = 7;
mapper['F'-'A'] = 8;


	for (int k = 0 ; k < T;k++)
	{
		int C,D,N;
		//list <int> oppose[20];
		char table[10][10] = {'$'};
		char opposeTable[10][10] = {'0'};
	        for (int i = 0 ; i < 10; i++)
			for (int j = 0 ; j < 10;j++) 
				table[i][j] = opposeTable[i][j] = '0';
                /**for (int i = 0 ; i < 10; i++)
                        for (int j = 0 ; j < 10;j++)
				printf("%c %c *",table[i][j],opposeTable[i][j]);
		**/
		scanf("%d",&C);
		for ( int i = 0 ; i < C;i++){
			char str[10];
			scanf("%s",str);
			table[mapper[str[0]-'A']][mapper[str[1]-'A']] = str[2];	
			table[mapper[str[1]-'A']][mapper[str[0]-'A']] = str[2];
		}
		scanf("%d",&D);
		for (int i = 0 ; i < D;i++) {
			char str[10];
			scanf("%s",str);
			//oppose[mapper[str[0]-'A']].push_back(str[1]);
			//oppose[mapper[str[1]-'A']].push_back(str[0]);
			opposeTable[mapper[str[0] - 'A']][mapper[str[1] - 'A']] = '1';
			opposeTable[mapper[str[1] - 'A']][mapper[str[0] - 'A']] = '1';
		}
		scanf("%d",&N);
		//printf ("%d %d %d", C,D,N);
		char mystring[1000];
		int top = 0;
		for (int i = 0 ; i < N;i++) {
			char c;
			scanf(" %c",&c);
			//printf("\n%c\n",c);		
			if (top != 0 && table[mapper[c-'A']][mapper[mystring[top-1]-'A']] != '0') {
		//		printf("%d %d cool??\n",mapper[c-'A'],mapper[mystring[top-1]-'A']);
		//		printf("cool:%c\n",table[mapper[c-'A']][mapper[mystring[top-1]-'A']]);
				mystring[top-1] = table[mapper[c-'A']][mapper[mystring[top-1]-'A']];
		//		printf("here");
			}
			else {
				mystring[top++] = c;
		//		printf("%ctop:%d",mystring[top-1],top-1);
				for (int j = 0 ; j < top-1; j++) {
					if (opposeTable[mapper[mystring[top-1]-'A']][mapper[mystring[j]-'A']] != '0') {
						top = 0;
						break;
					}
				}	
			}
			
		}
		mystring[top] = '\0';
		printf("Case #%d: ",k+1);
		printf("[");
		for (int i = 0 ; i< top;i++) {
			printf("%c%s",mystring[i],(top==(i+1))?"":", ");
		}
		printf("]\n");
	}
}

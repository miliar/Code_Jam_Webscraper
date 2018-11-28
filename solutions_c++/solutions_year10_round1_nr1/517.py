/*
Problem
In the exciting game of Join-K, red and blue pieces are dropped into an N-by-N table. The table stands up vertically so that pieces drop down to the bottom-most empty slots in their column. For example, consider the following two configurations: 

    - Legal Position -

          .......
          .......
          .......
          ....R..
          ...RB..
          ..BRB..
          .RBBR..
    - Illegal Position -

          .......
          .......
          .......
          .......
   Bad -> ..BR...
          ...R...
          .RBBR..
 

In these pictures, each '.' represents an empty slot, each 'R' represents a slot filled with a red piece, and each 'B' represents a slot filled with a blue piece. The left configuration is legal, but the right one is not. This is because one of the pieces in the third column (marked with the arrow) has not fallen down to the empty slot below it. 

A player wins if they can place K pieces of their color in a row, either horizontally, vertically, or diagonally. The four possible orientations are shown below:       - Four in a row -

     R   RRRR    R   R
     R          R     R
     R         R       R
     R        R         R
  
In the "Legal Position" diagram at the beginning of the problem statement, both players had lined up two pieces in a row, but not three. 

As it turns out, you are right now playing a very exciting game of Join-K, and you have a tricky plan to ensure victory! When your opponent is not looking, you are going to rotate the board 90 degrees clockwise onto its side. Gravity will then cause the pieces to fall down into a new position as shown below:     - Start -

     .......
     .......
     .......
     ...R...
     ...RB..
     ..BRB..
     .RBBR..
    - Rotate -

     .......
     R......
     BB.....
     BRRR...
     RBB....
     .......
     .......
    - Gravity -

     .......
     .......
     .......
     R......
     BB.....
     BRR....
     RBBR...
 
Unfortunately, you only have time to rotate once before your opponent will notice. 

All that remains is picking the right time to make your move. Given a board position, you should determine which player (or players!) will have K pieces in a row after you rotate the board clockwise and gravity takes effect in the new direction. 

Notes
You can rotate the board only once.
Assume that gravity only takes effect after the board has been rotated completely.
Only count K in a row after gravity has finished taking effect.
Input
The first line of the input gives the number of test cases, T. T test cases follow, each beginning with a line containing the integers N and K. The next N lines will each be exactly N characters long, showing the initial position of the board, using the same format as the diagrams above. 

The initial position in each test case will be a legal position that can occur during a game of Join-K. In particular, neither player will have already formed K pieces in a row. 

Output
For each test case, output one line containing "Case #x: y", where x is the case number (starting from 1), and y is one of "Red", "Blue", "Neither", or "Both". Here, y indicates which player or players will have K pieces in a row after you rotate the board. 

Limits
1 ¡Ü T ¡Ü 100.
3 ¡Ü K ¡Ü N. 

Small dataset
3 ¡Ü N ¡Ü 7. 

Large dataset
3 ¡Ü N ¡Ü 50. 

Sample

Input 
   
Output 
   
4
7 3
.......
.......
.......
...R...
...BB..
..BRB..
.RRBR..
6 4
......
......
.R...R
.R..BB
.R.RBR
RB.BBB
4 4
R...
BR..
BR..
BR..
3 3
B..
RB.
RB.

Case #1: Neither
Case #2: Both
Case #3: Red
Case #4: Blue
 


 


*/

#include <stdio.h>
#include <string.h>

int C;
char a[100][100];
char b[100][100];
int n,K;

int ff[4][2]={{0,1},{1,0},{1,1},{1,-1}};


int Rwin,Bwin;

int main()
{
//	freopen("a.txt","r",stdin);
	freopen("A-large.in.txt","r",stdin);
	freopen("a.out","w",stdout);

	scanf("%d",&C);
	int i,j,k,l;
	int i2,j2;
	int tt;
	char ch;
	for (tt=1;tt<=C;tt++)
	{

		scanf("%d %d",&n,&K);

		memset(b,0,sizeof(b));
		for (i=0;i<n;i++)
		{
			scanf("%s",&a[i]);
//			printf("%s\n",a[i]);
		}
//		printf("\n");


		for (i=0;i<n;i++)
		{
			for (j=0;j<n;j++)
			{
				b[j][n-i-1]=a[i][j];
			}
		}
/*
		for (i=0;i<n;i++)
		{
			printf("%s\n",b[i]);
		}
		printf("\n");
*/

		for (j=0;j<n;j++)
		{
			for (i=n-1;i>0;i--)
			{
				if (b[i][j]=='.' && b[i-1][j]!='.')
				{
					b[i][j]=b[i-1][j];
					b[i-1][j]='.';
					i2=i+1;
					while (i2<n && b[i2][j]=='.')
					{
						b[i2][j]=b[i2-1][j];
						b[i2-1][j]='.';
						i2++;
					}
				}
			}
		}

/*
		for (i=0;i<n;i++)
		{
			printf("%s\n",b[i]);
		}
*/
		Rwin=Bwin=0;


		for (i=0;i<n;i++)
		{
			for (j=0;j<n;j++)
			{
				if (b[i][j]=='R' || b[i][j]=='B')
				for (l=0;l<4;l++)
				{
					i2=i;j2=j;
					for (k=1;k<K;k++)
					{
						i2+=ff[l][0];
						j2+=ff[l][1];
						
						if (!(i2>=0 && i2<n && j2>=0 && j2<n)) break;

						if (b[i2][j2]!=b[i][j])
						{
							break;
						}
					}
					if (k==K)
					{
						if (b[i][j]=='R') Rwin=1;
						if (b[i][j]=='B') Bwin=1;
//						printf("%d %d %ch %d\n",i,j,b[i][j],l);
					}
				}
			}
		}
		

		printf("Case #%d:",tt);

		if (Rwin+Bwin==0)
		{
			printf(" Neither\n");
		}
		else
		if (Rwin+Bwin==2)
		{
			printf(" Both\n");
		}
		else
		if (Rwin==1)
		{	
			printf(" Red\n");
		}
		else
		{
			printf(" Blue\n");
		}


//		if (i) printf(" ON\n"); else printf(" OFF\n");
		
	}

	return 0;
}

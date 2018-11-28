#include <stdio.h>
#include <string.h>

using namespace std;


int main(int argc, char** argv){

		int N;
		bool won;
		bool over;
		scanf(" %d",&N);

		char l[4][5];

		for(int i=1;i<=N;i++)
		{
			won=false;
			scanf(" %s %s %s %s", l[0], l[1], l[2], l[3]);

			int tx=-1; int ty;

			// Change T into X
			for(int k=0;k<4;k++){
			for(int j=0;j<4;j++)
			{
				if(l[k][j]=='T') 
				{
					l[k][j]='X';
					tx=k;
					ty=j;
				}
			}}




			// Check horizontal lines
			for(int j=0;j<4;j++)
			{
				if(strcmp(l[j],"XXXX")==0)
				{
					if(!won) printf("%s%d%s","Case #", i, ": X won\n");
					won=true;
					break;
				}
			}
			// Check vertical lines
			for(int j=0;j<4;j++)
			{
				//
				if(l[0][j]!='.' && l[0][j]!='O' && l[0][j]==l[1][j] && l[1][j]==l[2][j] && l[2][j]==l[3][j])
				{
					if(!won) printf("%s%d%s%c%s","Case #",i,": ",l[0][j]," won\n");
					won=true;
					break;
				}
			}
			//Check diagonals
			if(l[0][0]!='.' && l[0][0]!='O' && l[0][0]==l[1][1]&& l[1][1]==l[2][2] && l[2][2]==l[3][3])
			{
				if(!won) printf("%s%d%s%c%s","Case #",i,": ",l[0][0]," won\n");
				won=true;
			}
			if(l[0][3]!='.' && l[0][3]!='O' && l[0][3]==l[1][2] && l[1][2]==l[2][1] && l[2][1]==l[3][0])
			{
				if(!won) printf("%s%d%s%c%s","Case #",i,": ",l[0][3]," won\n");
				won=true;
			}

			if(won) continue;

			if(tx!=-1) l[tx][ty]='O';

			// Check horizontal lines
			for(int j=0;j<4;j++)
			{
				if(strcmp(l[j],"OOOO")==0)
				{
					if(!won) printf("%s%d%s","Case #", i, ": O won\n");
					won=true;
					break;
				}
			}
			// Check vertical lines
			for(int j=0;j<4;j++)
			{
				//
				if(l[0][j]!='.' && l[0][j]!='X' && l[0][j]==l[1][j] && l[1][j]==l[2][j] && l[2][j]==l[3][j])
				{
					if(!won) printf("%s%d%s%c%s","Case #",i,": ",l[0][j]," won\n");
					won=true;
					break;
				}
			}
			//Check diagonals
			if(l[0][0]!='.' && l[0][0]!='X' && l[0][0]==l[1][1]&& l[1][1]==l[2][2] && l[2][2]==l[3][3])
			{
				if(!won) printf("%s%d%s%c%s","Case #",i,": ",l[0][0]," won\n");
				won=true;
			}
			if(l[0][3]!='.' && l[0][3]!='X' && l[0][3]==l[1][2]&& l[1][2]==l[2][1] && l[2][1]==l[3][0])
			{
				if(!won) printf("%s%d%s%c%s","Case #",i,": ",l[0][3]," won\n");
				won=true;
			}

			if(won) continue;
			
			over=true;
			for(int k=0;k<4;k++){
			for(int j=0;j<4;j++)
			{
				if(l[k][j]=='.') over=false;
			}}

			if(over)
			{
				printf("%s%d%s","Case #",i,": Draw\n");
			} else {
				printf("%s%d%s","Case #",i,": Game has not completed\n");
			}

		}
		
		return 0;
}
#include <iostream>
#include <fstream>

using namespace std;

void main()
{
	ifstream ifs("C-small-attempt1.in");
	ofstream ofs("C-small-attempt1.out");

	int board[101][101]={0,};
	int board2[101][101]={0,};

	int c,r,x1,x2,y1,y2;
	int ii,i,j,k;
	ifs>>c;
	for(ii=0; ii<c; ii++)
	{
		for(i=0; i<=100; i++)
			for(j=0; j<=100; j++)
			{
				board[i][j]=0;
				board2[i][j]=0;
			}

		ifs>>r;

		for(i=0; i<r; i++)
		{
			ifs>>x1>>y1>>x2>>y2;
			for(j=x1; j<=x2; j++)
				for(k=y1; k<=y2; k++)
					board[j][k]=1;
		}

		int nn=0;
		while(true)
		{
			++nn;
			bool br=true;
			for(i=1; i<=100; i++)
				for(j=1; j<=100; j++)
				{
					if(board[i-1][j]==0 && board[i][j-1]==0)
						board2[i][j]=0;
					else if(board[i-1][j]==1 && board[i][j-1]==1)
						board2[i][j]=1;
					else 
						board2[i][j]=board[i][j];
				}

			for(i=1; i<=100; i++)
			{
				if(board[0][i-1]==1)
					board2[0][i]=board[0][i];
				else
					board2[0][i]=0;

				if(board[i-1][0]==1)
					board2[i][0]=board[i][0];
				else
					board2[i][0]=0;
			}
			board2[0][0]=0;
			
			for(i=0; i<=100; i++)
				for(j=0; j<=100; j++)
				{
					board[i][j]=board2[i][j];
					if(board[i][j]==1)
					{
						br=false;
					}
				}
			if(br)
				break;


		}


		ofs<<"Case #"<<ii+1<<": "<<nn<<endl;
						
	}
}

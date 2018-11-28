#include <iostream>
#include <fstream>
using namespace std;

ifstream fin("A-large.in");
ofstream fout("A-large.out");

int findres();

int T;
char A[4][4];

int main()
{
	 fin>>T;
	 int i=0;
	 int x,y;
	 int res;
	 while(i<T)
	 {
		 for(x=0;x<4;x++)
		 {
			 for(y=0;y<4;y++)
			 {
				 fin>>A[x][y];
			 }
		 }

		 res=findres();

         i++;
		 fout<<"Case #";
		 fout<<i;
		 fout<<": ";
		 if(res==0)
		 {
			 fout<<"X won";
		 }
		 if(res==1)
		 {
			 fout<<"O won";
		 }
		 if(res==2)
		 {
			 fout<<"Draw";
		 }
		 if(res==3)
		 {
			 fout<<"Game has not completed";
		 }

		 if(i!=T)
		 {
			 fout<<"\n";
		 }
	 }

     return(0);
}

int findres()
{
	int i,j;
	int chk;
	int tposi=5,tposj=5;
	//Check for X's win

	for(i=0;i<4;i++)
	{
		for(j=0;j<4;j++)
		{
			if(A[i][j]=='T')
			{
				tposi=i;tposj=j;
				A[i][j]='X';
			}
		}
	}
	//Check rowwise
	
	for(i=0;i<4;i++)
	{
		chk=0;
		for(j=0;j<4;j++)
		{
			if(A[i][j]!='X'){chk++;}
		}
		if(chk==0){return(0);}
	}
	//Check colwise
	
	for(i=0;i<4;i++)
	{
		chk=0;
		for(j=0;j<4;j++)
		{
			if(A[j][i]!='X'){chk++;}
		}
		if(chk==0){return(0);}
	}

	//Check Diagonally

	//Left diagonal
	if(A[0][0]=='X' && A[1][1]=='X' && A[2][2]=='X' && A[3][3]=='X')
	{
		return(0);
	}
	//Right diagonal
	if(A[0][3]=='X' && A[1][2]=='X' && A[2][1]=='X' && A[3][0]=='X')
	{
		return(0);
	}

	//Check for Y's win

	if(tposi<5)
	{
		A[tposi][tposj]='O';
	}
	//Check rowwise
	
	for(i=0;i<4;i++)
	{
		chk=0;
		for(j=0;j<4;j++)
		{
			if(A[i][j]!='O'){chk++;}
		}
		if(chk==0){return(1);}
	}
	//Check colwise
	
	for(i=0;i<4;i++)
	{
		chk=0;
		for(j=0;j<4;j++)
		{
			if(A[j][i]!='O'){chk++;}
		}
		if(chk==0){return(1);}
	}

	//Check Diagonally

	//Left diagonal
	if(A[0][0]=='O' && A[1][1]=='O' && A[2][2]=='O' && A[3][3]=='O')
	{
		return(1);
	}
	//Right diagonal
	if(A[0][3]=='O' && A[1][2]=='O' && A[2][1]=='O' && A[3][0]=='O')
	{
		return(1);
	}

	//Check for games's completion
	for(i=0;i<4;i++)
	{
		for(j=0;j<4;j++)
		{
			if(A[i][j]=='.'){return(3);}
		}
	}
	return(2);
}	
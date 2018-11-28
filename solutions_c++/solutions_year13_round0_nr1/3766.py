#include <iostream>
#include <stdio.h>
#include <algorithm>

using namespace std;

int main()
{
	FILE* fin = fopen("A-large.in","r");
	/*if(fin!=NULL)
		cout<<"Success in file opening"<<endl<<endl;
		*/
	FILE* fout = fopen("output.txt","w+");
	int number_of_cases=0;

	fscanf(fin,"%d",&number_of_cases);
	int board[4][4]={0};
	char c;
	fscanf(fin,"%c",&c);	
	for(int ncase=0;ncase<number_of_cases;ncase++)
	{
		//scan 16 
		if(ncase>0)
		{
			fscanf(fin,"%c",&c);	
		}
		for(int e1=0;e1<4;e1++)
		{
			for(int e2=0;e2<4;e2++)
			{
				fscanf(fin,"%c",&c);	
				board[e1][e2]=(int)c;
				//fscanf(fin,"%c",&board[e1][e2]);	
			}
			fscanf(fin,"%c",&c);	
			//fscanf(fin,"%c",&c);	
		}//scan16
		
		bool IsX = false;
		bool IsO = false;
		bool IsDraw = true;
		bool IsEmpty = false;
		//check for empty i.e "."
		for(int e1=0;e1<4;e1++)
		{
			for(int e2=0;e2<4;e2++)
			{
				if(board[e1][e2]==46)
				{
					IsEmpty=true;
					break;
				}
				if(IsEmpty)
					break;
			}
		}//check empty
		//check rows
		for(int i = 0; i < 4; i++)
		{
			if((board[i][0]==88||board[i][0]==84)&&(board[i][1]==88||board[i][1]==84)&&(board[i][2]==88||board[i][2]==84)&&(board[i][3]==88||board[i][3]==84))
			{
				IsX=true;
			}
			if((board[i][0]==79||board[i][0]==84)&&(board[i][1]==79||board[i][1]==84)&&(board[i][2]==79||board[i][2]==84)&&(board[i][3]==79||board[i][3]==84))
			{
				IsO=true;
			}
		}//check rows
		//check columns
		for(int i = 0; i < 4; i++)
		{
			if((board[0][i]==88||board[0][i]==84)&&(board[1][i]==88||board[1][i]==84)&&(board[2][i]==88||board[2][i]==84)&&(board[3][i]==88||board[3][i]==84))
			{
				IsX=true;
			}
			if((board[0][i]==79||board[0][i]==84)&&(board[1][i]==79||board[1][i]==84)&&(board[2][i]==79||board[2][i]==84)&&(board[3][i]==79||board[3][i]==84))
			{
				IsO=true;
			}
		}//check column

		//check diagonal X
		if((board[0][0]==88||board[0][0]==84)&&(board[1][1]==88||board[1][1]==84)&&(board[2][2]==88||board[2][2]==84)&&(board[3][3]==88||board[3][3]==84))
		{
			IsX=true;
		}

		//check diagonal X
		if((board[0][3]==88||board[0][3]==84)&&(board[1][2]==88||board[1][2]==84)&&(board[2][1]==88||board[2][1]==84)&&(board[3][0]==88||board[3][0]==84))
		{
			IsX=true;
		}
		//check diagonal O
		if((board[0][0]==79||board[0][0]==84)&&(board[1][1]==79||board[1][1]==84)&&(board[2][2]==79||board[2][2]==84)&&(board[3][3]==79||board[3][3]==84))
		{
			IsO=true;
		}

		//check diagonal O
		if((board[0][3]==79||board[0][3]==84)&&(board[1][2]==79||board[1][2]==84)&&(board[2][1]==79||board[2][1]==84)&&(board[3][0]==79||board[3][0]==84))
		{
			IsO=true;
		}


		if(IsX==true)
		{
			fprintf(fout,"Case #%d: X won\n",ncase+1);
		}
		if(IsO==true)
		{
			fprintf(fout,"Case #%d: O won\n",ncase+1);
		}
		if(IsEmpty==false)
		{
			if(IsO==false&&IsX==false)
			{
				fprintf(fout,"Case #%d: Draw\n",ncase+1);
			}
		}
		else
		{
			if(IsO==false&&IsX==false)
			{
				fprintf(fout,"Case #%d: Game has not completed\n",ncase+1);
			}
		}

	}	
	return 0;
}
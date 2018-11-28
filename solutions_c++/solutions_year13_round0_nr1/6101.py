// google_1.cpp : 定义控制台应用程序的入口点。
//

#include "stdafx.h"


int _tmain(int argc, _TCHAR* argv[])
{

	char board[4][4];
	int N;
	char a;
	char row;
	char col;
	char pdiag;
	char ndiag;
	bool isfull;
	bool flag;
	FILE *fin;
	FILE *fout;
	fin=fopen("A-small-attempt1.in","r");
	if(fin==NULL)
		printf("input file open error!\n");
	fout=fopen("A-small-attempt1.out","w");
	if(fout==NULL)
		printf("output file open error!\n");
	//读入

	fscanf(fin,"%d",&N);
	fscanf(fin,"%c",&a);
	for(int i=1;i<=N;i++)
	{
		/******************************read file*******************/
		if(i!=1)
		{
			fscanf(fin,"%c",&a);
		}
		for(int j=0;j<4;j++)
		{
			for(int k=0;k<4;k++)
			{
				fscanf(fin,"%c",&board[j][k]);

			
			}

		fscanf(fin,"%c",&a);
		
		}
		/***********************************************************/
		//X是否胜
		//Y是否胜
		//是否平
		isfull=true;
		pdiag='T';
		ndiag='T';
		flag=false;
		for(int j=0;j<4;j++)
		{
			if(pdiag=='T')
			{
					pdiag=board[j][j];
			}
			if(ndiag=='T')
			{
					ndiag=board[j][3-j];
			}
			
			if(board[j][3-j]!=ndiag&&board[j][3-j]!='T')
			{			
				ndiag='.';
				
			}
			if(board[j][j]!=pdiag&&board[j][j]!='T')
			{			
				pdiag='.';


			}
			if(board[j][j]=='.')
			{
				isfull=false;
				continue;
			}
			else
			{
				row=board[j][j];
				col=board[j][j];
			}

			for(int k=0;k<4;k++)
			{
				//row
				if(row=='T')
				{
					row=board[j][k];
				}
				if(board[j][k]=='.')
				{
					row='.';
					isfull=false;
				}
				if(board[j][k]!=row&&board[j][k]!='T')
				{
					row='.';
				}
				

				//column
				if(col=='T')
				{
					col=board[k][j];
				}
				if(board[k][j]=='.')
				{
					col='.';
					isfull=false;
				}
				if(board[k][j]!=col&&board[k][j]!='T')
				{
					col='.';
				}
				
			
			}
			if(row!='.')
			{
				fprintf(fout,"Case #%d: %c won\n",i,row);
				flag=true;
				break;
			
			}
			if(col!='.')
			{
				fprintf(fout,"Case #%d: %c won\n",i,col);
				flag=true;
				break;
			
			}

			
		
		}
		if(flag==true)
		{
			continue;
		}
		if(pdiag!='.')
		{
			fprintf(fout,"Case #%d: %c won\n",i,pdiag);
			continue;
		
		}
		if(ndiag!='.')
		{
			fprintf(fout,"Case #%d: %c won\n",i,ndiag);
			continue;
		
		}
		if(isfull==false)
		{
			fprintf(fout,"Case #%d: Game has not completed\n",i);
			continue;
		}
		else
		{
			fprintf(fout,"Case #%d: Draw\n",i);
			continue;
		}
	
	}
	fclose(fin);
	fclose(fout);
	return 0;
	
}


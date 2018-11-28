#include<stdio.h>

int main()
{
	FILE *fin=fopen("input.txt","r");
	FILE *fout=fopen("output.txt","w");

	int T,K,N;

	char board[100][100];

	fscanf(fin,"%d",&T);

	for(int i=1;i<=T;i++)
	{
		bool R=false;
		bool B=false;
		fscanf(fin,"%d %d",&N,&K);
		for(int j=0;j<N;j++)
		{
			fscanf(fin,"%s",board[j]);
			int l=N-1;
			for(int k=l;k>=0;k--)
			{
				if(board[j][k]!='.')
				{
					board[j][l]=board[j][k];
					if(k!=l) board[j][k]='.';

					if(board[j][l]=='R' && !R)
					{
						int a;
						for(a=0;a<K;a++)
							if(!(j>=K-1 && l>=K-1 && board[j-a][l-a]==board[j][l]))
								break;
						if(a==K) R=true;
						for(a=0;a<K;a++)
							if(!(j>=K-1 && board[j-a][l]==board[j][l]))
								break;
						if(a==K) R=true;
						for(a=0;a<K;a++)
							if(!(j>=K-1 && l<=N-K && board[j-a][l+a]==board[j][l]))
								break;
						if(a==K) R=true;
						for(a=0;a<K;a++)
							if(!(l<=N-K && board[j][l+a]==board[j][l]))
								break;
						if(a==K) R=true;
					}
					else if(board[j][l]=='B' && !B)
					{
						int a;
						for(a=0;a<K;a++)
							if(!(j>=K-1 && l>=K-1 && board[j-a][l-a]==board[j][l]))
								break;
						if(a==K) B=true;
						for(a=0;a<K;a++)
							if(!(j>=K-1 && board[j-a][l]==board[j][l]))
								break;
						if(a==K) B=true;
						for(a=0;a<K;a++)
							if(!(j>=K-1 && l<=N-K && board[j-a][l+a]==board[j][l]))
								break;
						if(a==K) B=true;
						for(a=0;a<K;a++)
							if(!(l<=N-K && board[j][l+a]==board[j][l]))
								break;
						if(a==K) B=true;
					}
					l--;
				}
			}
		}

		fprintf(fout,"Case #%d: ",i);
		if(!R && !B) fprintf(fout,"Neither\n");
		else if(R && B) fprintf(fout,"Both\n");
		else if(R) fprintf(fout,"Red\n");
		else fprintf(fout,"Blue\n");
	}

	return 0;
}
#include <stdio.h>
#include <conio.h>



void main()
{
	FILE *InStream, *OutStream;
	InStream = fopen("in.txt", "a+");
	OutStream = fopen("out.txt", "a+");


	int NumCase;
	fscanf(InStream, "%d", &NumCase);

	for (int Case = 1; Case<=NumCase; Case++)
	{
		bool RPlus = false;
		bool BPlus = false;

		int N, K;
		char q;
		fscanf(InStream, "%d %d", &N, &K);
		fscanf(InStream, "%c", &q);

		char ** Table = new char* [N];
		char ** NewTable = new char* [N];
		for (int i=0; i<N; i++)
		{
			Table[i] = new char [N];
			NewTable[i] = new char [N];
		}

		for (int i=0; i<N; i++)
		{
			for (int j=0; j<N; j++)
				fscanf(InStream, "%c", &Table[i][j]);
			fscanf(InStream, "%c", &q);
		}


		/*Rotate*/
		for (int i=0; i<N; i++)
			for (int j=0; j<N; j++)
				NewTable[j][(N-1)-i] = Table[i][j];

		char ** FallTable = new char* [N];
		for (int i=0; i<N; i++)
		{
			FallTable[i] = new char [N];
			for (int j=0; j<N; j++)
				FallTable[i][j] = NewTable[i][j];
		}
		/*Fall*/
		for (int j=0; j<N; j++)
		{
			int curr = N-1;
			for (int i=N-1; i>=0; i--)
			{
				if (NewTable[i][j] != '.')
					FallTable[curr--][j]=NewTable[i][j];
			}
			for (int i=curr; i>=0; i--)
				FallTable[i][j] = '.';
		}

	/*	for (int a=0; a<N; a++)
		{
			for (int b=0; b<N; b++)
				printf("%c ", FallTable[a][b]);
			printf("\n");
		}
		printf ("\n\n");
		getch();*/

		/*Count*/
		for (int i=0; ((i<N)&&(!(RPlus&&BPlus))); i++)
		{
			for (int j=0; ((j<N)&&(!(RPlus&&BPlus))); j++)
			{
				if (((FallTable[i][j] == 'B')&&(!BPlus))||((FallTable[i][j] == 'R')&&(!RPlus)))
				{
					int Count = 1;
					/*right*/
					for (int k=1; k<K; k++)
					{
						if  ((j+k<N)&&(FallTable[i][j+k] == FallTable[i][j]))
							Count++;
						else break;
					}
					if (Count==K)
					{
						if (FallTable[i][j] == 'R')
							RPlus = true;
						else
							BPlus = true;
						break;
					}
					/*left*/
					Count = 1;
					for (int k=1; k<K; k++)
					{
						if  ((j-k>=0)&&(FallTable[i][j-k] == FallTable[i][j]))
							Count++;
						else break;
					}
					if (Count==K)
					{
						if (FallTable[i][j] == 'R')
							RPlus = true;
						else
							BPlus = true;
						break;
					}
					/*up*/
					Count = 1;
					for (int k=1; k<K; k++)
					{
						if  ((i-k>=0)&&(FallTable[i-k][j] == FallTable[i][j]))
							Count++;
						else break;
					}
					if (Count==K)
					{
						if (FallTable[i][j] == 'R')
							RPlus = true;
						else
							BPlus = true;
						break;
					}
					/*down*/
					Count = 1;
					for (int k=1; k<K; k++)
					{
						if  ((i+k<N)&&(FallTable[i+k][j] == FallTable[i][j]))
							Count++;
						else break;
					}
					if (Count==K)
					{
						if (FallTable[i][j] == 'R')
							RPlus = true;
						else
							BPlus = true;
						break;
					}
					/*diagonal*/
					/*up right*/
					Count = 1;
					for (int k=1; k<K; k++)
					{
						if  ((i-k>=0)&&(j+k<N)&&(FallTable[i-k][j+k] == FallTable[i][j]))
							Count++;
						else break;
					}
					if (Count==K)
					{
						if (FallTable[i][j] == 'R')
							RPlus = true;
						else
							BPlus = true;
						break;
					}
					/*up left*/
					Count = 1;
					for (int k=1; k<K; k++)
					{
						if  ((i-k>=0)&&(j-k>=0)&&(FallTable[i-k][j-k] == FallTable[i][j]))
							Count++;
						else break;
					}
					if (Count==K)
					{
						if (FallTable[i][j] == 'R')
							RPlus = true;
						else
							BPlus = true;
						break;
					}
					/*down right*/
					Count = 1;
					for (int k=1; k<K; k++)
					{
						if  ((j+k<N)&&(i+k<N)&&(FallTable[i+k][j+k] == FallTable[i][j]))
							Count++;
						else break;
					}
					if (Count==K)
					{
						if (FallTable[i][j] == 'R')
							RPlus = true;
						else
							BPlus = true;
						break;
					}
					/*down left*/
					Count = 1;
					for (int k=1; k<K; k++)
					{
						if  ((j-k>=0)&&(i+k<N)&&(FallTable[i+k][j-k] == FallTable[i][j]))
							Count++;
						else break;
					}
					if (Count==K)
					{
						if (FallTable[i][j] == 'R')
							RPlus = true;
						else
							BPlus = true;
						break;
					}


				}
			}
		}





		if ((RPlus==false)&&(BPlus==false))
			fprintf(OutStream, "Case #%d: Neither\n", Case);
		if ((RPlus==true)&&(BPlus==false))
			fprintf(OutStream, "Case #%d: Red\n", Case);
		if ((RPlus==false)&&(BPlus==true))
			fprintf(OutStream, "Case #%d: Blue\n", Case);
		if ((RPlus==true)&&(BPlus==true))
			fprintf(OutStream, "Case #%d: Both\n", Case);

		for (int i=0; i<N; i++)
		{
			delete [] Table[i];
			delete [] NewTable[i];
			delete [] FallTable[i];
		}
		delete [] Table;
		delete [] NewTable;
		delete [] FallTable;

	}

	fclose(InStream);
	fclose(OutStream);
}

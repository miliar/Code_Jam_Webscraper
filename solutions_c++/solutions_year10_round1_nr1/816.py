#include <stdio.h>

void RotateClockwise(char** Table, int N)
{
	char **TmpTable = new char*[N];
	for(int j=0;j<N;++j)
	{
		TmpTable[j] = new char[N];
	}

	for(int i=0;i<N;++i)
	{
		for(int j=0;j<N;++j)
		{
			TmpTable[i][j] = Table[N-1-j][i];
		}
	}

	for(int i=0;i<N;++i)
	{
		for(int j=0;j<N;++j)
		{
			Table[i][j] = TmpTable[i][j];
		}
	}

	for(int j=0;j<N;++j)
	{
		delete[] TmpTable[j];
	}
	delete[] TmpTable;
}

void ApplyGravity(char** Table, int N)
{
	int *GroundPos = new int[N];
	char **TmpTable = new char*[N];
	for(int j=0;j<N;++j)
	{
		TmpTable[j] = new char[N];
		for(int h=0;h<N;++h)
		{
			TmpTable[j][h] = '.';
		}
	}
	for(int i=0;i<N;++i)
	{
		GroundPos[i] = N-1;
	}
	for(int i=N-1;i>=0;--i)
	{
		for(int j=0;j<N;++j)
		{
			if(Table[i][j] != '.')
			{
				TmpTable[GroundPos[j]][j] = Table[i][j];
				Table[i][j] = '.';
				GroundPos[j]--;
			}
		}
	}

	for(int i=0;i<N;++i)
	{
		for(int j=0;j<N;++j)
		{
			Table[i][j] = TmpTable[i][j];
		}
	}

	for(int j=0;j<N;++j)
	{
		delete[] TmpTable[j];
	}
	delete[] TmpTable;
	delete[] GroundPos;
}

bool CanMade(char** Table, int N, int K, int i, int j)
{
	char Team = Table[i][j];
	int Count = 0;
	int ti = i, tj = j;
	while(ti < N)
	{
		if(Table[ti][tj] == Team)
		{
			Count++;
		}
		else
		{
			break;
		}
		if(Count == K)
		{
			return true;
		}
		ti++;
	}
	Count = 0;
	ti = i;
	while(tj < N)
	{
		if(Table[ti][tj] == Team)
		{
			Count++;
		}
		else
		{
			break;
		}
		if(Count == K)
		{
			return true;
		}
		tj++;
	}
	Count = 0;
	tj = j;
	while(tj < N && ti < N)
	{
		if(Table[ti][tj] == Team)
		{
			Count++;
		}
		else
		{
			break;
		}
		if(Count == K)
		{
			return true;
		}
		tj++;
		ti++;
	}
	Count = 0;
	tj = j;
	ti = i;
	while(tj >= 0 && ti < N)
	{
		if(Table[ti][tj] == Team)
		{
			Count++;
		}
		else
		{
			break;
		}
		if(Count == K)
		{
			return true;
		}
		tj--;
		ti++;
	}
	return false;
}

char* WhoWin(char** Table, int N, int K)
{
	bool bRedWin = false, bBlueWin = false;
	for(int i=0;i<N;++i)
	{
		for(int j=0;j<N;++j)
		{
			if(Table[i][j] == 'R')
			{
				if(CanMade(Table, N, K, i, j))
				{
					bRedWin = true;
				}
			}
			else if(Table[i][j] == 'B')
			{
				if(CanMade(Table, N, K, i, j))
				{
					bBlueWin = true;
				}
			}
		}
	}
	if(bRedWin && bBlueWin)
	{
		return "Both";
	}
	else if(bRedWin)
	{
		return "Red";
	}
	else if(bBlueWin)
	{
		return "Blue";
	}
	return "Neither";
}

void main()
{
	FILE* fp = NULL;
	FILE* outfp = NULL;
	fopen_s(&fp, "A-large.in", "r");
	fopen_s(&outfp, "A-large.out", "w");
	if(fp)
	{
		int T;
		fscanf_s(fp, "%d", &T);
		for(int i=0;i<T;++i)
		{
			int N, K;
			fscanf_s(fp, "%d %d\n", &N, &K);
			char **Table = new char*[N];
			for(int j=0;j<N;++j)
			{
				Table[j] = new char[N];
				for(int h=0;h<N;++h)
				{
					fscanf_s(fp, "%c", &Table[j][h]);
				}
				fscanf_s(fp, "\n");
			}
			RotateClockwise(Table, N);
			ApplyGravity(Table, N);
			fprintf(outfp, "Case #%d: %s\n", i+1, WhoWin(Table, N, K));
			for(int j=0;j<N;++j)
			{
				delete[] Table[j];
			}
			delete[] Table;
		}
		fclose(fp);
		fclose(outfp);
	}
}
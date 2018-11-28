#include "stdio.h"
#include "stdlib.h"
#include "memory.h"
#include "string.h"
#include "math.h"

FILE *fin, *fout;

#define INPUT_FILE_NAME "B-small-attempt0"
#define INPUT_FILE INPUT_FILE_NAME##".in"
#define OUTPUT_FILE INPUT_FILE_NAME##".out"

#define print(format,...) {fprintf(fout, format, __VA_ARGS__); printf(format, __VA_ARGS__);}

#define min(a,b) ((a)<(b)?(a):(b))
#define max(a,b) ((a)>(b)?(a):(b))
#define pow2(a) ((a)*(a))

template<class T>
inline void swap(T &a, T &b)
{
	T c;
	c=a;
	a=b;
	b=c;
}

void problem(int nCase);
void init();

void main(int argc, char **argv)
{
	int N,k;
	printf("%s\n", INPUT_FILE);
	fopen_s(&fin, INPUT_FILE, "rt");
	fopen_s(&fout, OUTPUT_FILE, "wt");
	fscanf_s(fin, "%d\n", &N);
	k=0;
	init();
	while(N--)
	{
		++k;
		print("Case #%d: ", k);
		problem(k);
		print("\n");
	}
	fclose(fin);
	fclose(fout);
}

void init()
{
}

int S,M;
bool **data;
bool **checkData;

bool check(int x, int y, int move)
{
	int i,j;
	bool bFork, bBridge, bRing;
	bFork = bBridge = bRing = false;
	bool bEnd = false;
	for (i=0;i<S*2;++i)
	{
		memset(checkData[i], 0, sizeof(bool)*S*2);
	}
	checkData[x][y] = true;
	while (!bEnd)
	{
		bEnd = true;
		for (i=1;i<S*2; ++i)
		{
			for (j=1;j<S*2;++j)
			{
				if (abs(i-j)<S)
				{
					if (checkData[i][j])
					{
						if (checkData[i-1][j] == false && data[i-1][j])
						{
							bEnd = false;
							checkData[i-1][j] = true;
						}
						if (checkData[i-1][j-1] == false && data[i-1][j-1])
						{
							bEnd = false;
							checkData[i-1][j-1] = true;
						}
						if (checkData[i][j-1] == false && data[i][j-1])
						{
							bEnd = false;
							checkData[i][j-1] = true;
						}
						if (checkData[i+1][j] == false && data[i+1][j])
						{
							bEnd = false;
							checkData[i+1][j] = true;
						}
						if (checkData[i+1][j+1] == false && data[i+1][j+1])
						{
							bEnd = false;
							checkData[i+1][j+1] = true;
						}
						if (checkData[i][j+1] == false && data[i][j+1])
						{
							bEnd = false;
							checkData[i][j+1] = true;
						}
					}
				}
			}
		}
	}
	int nCorn;
	nCorn = checkData[1][1] + checkData[S][1] + checkData[1][S] + checkData[S][S*2-1] + checkData[S*2-1][S] + checkData[S*2-1][S*2-1];
	bBridge = (nCorn >= 2);
	bool bEdge[6];
	bEdge[0] = bEdge[1] = bEdge[2] = bEdge[3] = bEdge[4] = bEdge[5] = false;
	for (i=2;i<S;++i)
	{
		bEdge[1] |= checkData[i][1];
		bEdge[2] |= checkData[1][i];
		bEdge[3] |= checkData[i][i+S-1];
		bEdge[4] |= checkData[i+S-1][i];
		bEdge[5] |= checkData[S*2-1][S*2-i];
		bEdge[0] |= checkData[S*2-i][S*2-1];
	}
	int nEdges = bEdge[0] + bEdge[1] + bEdge[2] + bEdge[3] + bEdge[4] + bEdge[5];
	bFork = (nEdges>=3);

	for (i=0;i<S*2;++i)
	{
		memset(checkData[i], 0, sizeof(bool)*S*2);
	}
	for (i=1;i<=S;++i)
	{
		if (data[i][1] == false)
			checkData[i][1] = true;
		if (data[1][i] == false)
			checkData[1][i] = true;
		if (data[i][i+S-1] == false)
			checkData[i][i+S-1] = true;
		if (data[i+S-1][i] == false)
			checkData[i+S-1][i] = true;
		if (data[S*2-1][S*2-i] == false)
			checkData[S*2-1][S*2-i] = true;
		if (data[S*2-i][S*2-1] == false)
			checkData[S*2-i][S*2-1] = true;
	}
	bEnd = false;
	while (!bEnd)
	{
		bEnd = true;
		for (i=1;i<S*2; ++i)
		{
			for (j=1;j<S*2;++j)
			{
				if (abs(i-j)<S)
				{
					if (checkData[i][j])
					{
						if (checkData[i-1][j] == false && data[i-1][j] == false)
						{
							bEnd = false;
							checkData[i-1][j] = true;
						}
						if (checkData[i-1][j-1] == false && data[i-1][j-1] == false)
						{
							bEnd = false;
							checkData[i-1][j-1] = true;
						}
						if (checkData[i][j-1] == false && data[i][j-1] == false)
						{
							bEnd = false;
							checkData[i][j-1] = true;
						}
						if (checkData[i+1][j] == false && data[i+1][j] == false)
						{
							bEnd = false;
							checkData[i+1][j] = true;
						}
						if (checkData[i+1][j+1] == false && data[i+1][j+1] == false)
						{
							bEnd = false;
							checkData[i+1][j+1] = true;
						}
						if (checkData[i][j+1] == false && data[i][j+1] == false)
						{
							bEnd = false;
							checkData[i][j+1] = true;
						}
					}
				}
			}
		}
	}

	for (i=1;i<S*2; ++i)
	{
		for (j=1;j<S*2;++j)
		{
			if (abs(i-j)<S)
			{
				bRing |= (checkData[i][j]==false && data[i][j]== false);
			}
		}
	}

	
	if (bBridge)
	{
		if (bFork)
		{
			if (bRing)
			{
				print("bridge-fork-ring in move %d", move);
			}
			else
			{
				print("bridge-fork in move %d", move);
			}
		}
		else
		{
			if (bRing)
			{
				print("bridge-ring in move %d", move);
			}
			else
			{
				print("bridge in move %d", move);
			}
		}
	}
	else
	{
		if (bFork)
		{
			if (bRing)
			{
				print("fork-ring in move %d", move);
			}
			else
			{
				print("fork in move %d", move);
			}
		}
		else
		{
			if (bRing)
			{
				print("ring in move %d", move);
			}
		}
	}
	return bBridge | bFork | bRing;
}

void problem(int nCase)
{
	int i,j,k;
	int a,b,c;
	bool bFound = false;
	fscanf_s(fin, "%d %d", &S, &M);
	data = new bool*[S*2+10];
	checkData = new bool*[S*2+10];
	for (i=0;i<S*2+10;++i)
	{
		data[i] = new bool[S*2+10];
		checkData[i] = new bool[S*2+10];
		memset(data[i], 0, sizeof(bool)*S*2);
	}
	for (i=0;i<M;++i)
	{
		int x,y;
		fscanf_s(fin, "%d %d", &x, &y);
		data[x][y] = true;
		if (!bFound)
			bFound = check(x,y,i+1);
	}
	if (!bFound)
		print("none");
	for (i=0;i<S*2+10;++i)
	{
		delete data[i];
		delete checkData[i];
	}
	delete []data;
	delete []checkData;
}
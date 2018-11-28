#include <iostream>
#include <vector>
#include <set>
#include <string>
#include <fstream>


using namespace std;

ifstream myin("B-large.in");
ofstream myout("2.out");
const int inf = 10010;
const int MAXN = 110;
int att[MAXN][MAXN]; // attitude
int auxType[MAXN][MAXN]; // intermediate classified info
char finalType[10010]; //auxType as index
bool visited[MAXN][MAXN];
int main()
{
	int T, H, W;
	myin >> T;
	for(int caseCnt=0; caseCnt<T; ++caseCnt)
	{
		memset(finalType, 0, sizeof(finalType));
		myin >> H >> W;
		for(int i=0; i<=H+1; ++i)
			for(int j=0; j<=W+1; ++j)
			{
				if(i==0 || j==0 || i==H+1 || j==W+1)
					att[i][j] = inf;
				else
					myin >> att[i][j];
				auxType[i][j] = -1;
				visited[i][j] = false;
			}

		int curAuxType = 0;
		char curChar = 'a';
		for(int i=1; i<=H; ++i)
			for(int j=1; j<=W; ++j)
			{
				if(visited[i][j]) continue;
				bool canBFS = true;
				bool foundOld = false;
				int curi=i, curj=j;
				int nexti, nextj;
				auxType[curi][curj] = curAuxType;
				while(canBFS)
				{
					if(visited[curi][curj]) break;
					if(att[curi-1][curj] >= att[curi][curj] && 
							att[curi][curj-1] >= att[curi][curj] &&
							att[curi][curj+1] >= att[curi][curj] &&
							att[curi+1][curj] >= att[curi][curj]) //sink
					{
						visited[curi][curj] = true;
						canBFS = false;
					}
					else
					{
						if(att[curi-1][curj] <= att[curi][curj-1] &&
								att[curi-1][curj] <= att[curi][curj+1] &&
								att[curi-1][curj] <= att[curi+1][curj]) // flow north
						{
							nexti = curi - 1;	nextj = curj;
						}
						else if(//att[curi][curj-1] <= att[curi-1][curj] &&
								att[curi][curj-1] <= att[curi][curj+1] &&
								att[curi][curj-1] <= att[curi+1][curj]) //flow west
						{
							nexti = curi;		nextj = curj - 1;
						}
						else if(//att[curi][curj+1] <= att[curi-1][curj] &&
								//att[curi][curj+1] <= att[curi][curj-1] &&
								att[curi][curj+1] <= att[curi+1][curj]) //flow east
						{
							nexti = curi;		nextj = curj + 1;
						}
						else // flow south
						{
							nexti= curi + 1;	nextj = curj;
						}

						
						if(auxType[nexti][nextj] != -1) // neighbor already has a type
						{
							finalType[curAuxType] = finalType[ auxType[nexti][nextj] ];
							foundOld = true;
						}
						else
							auxType[nexti][nextj] = curAuxType;

						visited[curi][curj] = true;
						curi = nexti;	curj = nextj;
					}
				}// end of while, end of a BFS

				if(!foundOld)	finalType[curAuxType] = curChar++;
				++curAuxType;
			}//end of the whole process

			if(caseCnt>0)	myout << endl;
			myout << "Case #" << caseCnt+1 << ":" << endl; //Case #1:
			for(int i=1; i<=H; ++i)
			{
				if(i>1) myout << endl;
				for(int j=1; j<=W; ++j)
				{
					if(j>1) myout << " ";
					myout << finalType[auxType[i][j]];
				}
			}
	}
	return 0;
}
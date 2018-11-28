#include <cstdio>
#include <algorithm>
#include <vector>
#include <queue>

using namespace std;

#define MAXARR 105

struct StReg
{
	int Alti;
	vector< vector<int> > From;
	vector< vector<int> > To;
};

int SinkTo(StReg R[MAXARR][MAXARR], int x, int y)
{
	int M[4][2] = {{-1,0}, {0,-1}, {0,1}, {1,0}};
	int Ans = R[x][y].Alti;
	int To = 5;
	
	for (int i=0; i<4; i++)
	{
		if (Ans > R[ x+M[i][0] ][ y+M[i][1] ].Alti)
		{
			Ans = R[ x+M[i][0] ][ y+M[i][1] ].Alti;
			To = i;
		}
	}
	
	if (Ans<R[x][y].Alti)
		return To;
	else
		return 5;
}


int main()
{
	int T;
	scanf("%d", &T);

	for (int test=1; test<=T; test++)
	{
		int H, W, i, j;
		
		StReg Reg[MAXARR][MAXARR];
		
		scanf("%d %d", &H, &W);
		
		for (i=0; i<=H; i++)
		{
			Reg[i][W+1].Alti = 11000;
			Reg[i][0].Alti = 11000;
		}
		
		for (i=0; i<=W; i++)
		{
			Reg[H+1][i].Alti = 11000;
			Reg[0][i].Alti = 11000;
		}
		
		for (i=1; i<=H; i++)
			for (j=1; j<=W; j++)
				scanf("%d", &(Reg[i][j].Alti));
			
		for (i=1; i<=H; i++)
		{
			for (j=1; j<=W; j++)
			{
				int To = SinkTo(Reg,i,j);
				switch (To)
				{
					case 0 : 	{
									vector<int> VT;
									VT.push_back(i-1);
									VT.push_back(j);
									Reg[i][j].To.push_back(VT);
									VT.clear();
									VT.push_back(i);
									VT.push_back(j);
									Reg[i-1][j].From.push_back(VT);
									VT.clear();
									break;
								}	
					case 1 : 	{
									vector<int> VT;
									VT.push_back(i);
									VT.push_back(j-1);
									Reg[i][j].To.push_back(VT);
									VT.clear();
									VT.push_back(i);
									VT.push_back(j);
									Reg[i][j-1].From.push_back(VT);
									VT.clear();
									break;
								}	
					case 2 : 	{
									vector<int> VT;
									VT.push_back(i);
									VT.push_back(j+1);
									Reg[i][j].To.push_back(VT);
									VT.clear();
									VT.push_back(i);
									VT.push_back(j);
									Reg[i][j+1].From.push_back(VT);
									VT.clear();
									break;
								}	
					case 3 : 	{
									vector<int> VT;
									VT.push_back(i+1);
									VT.push_back(j);
									Reg[i][j].To.push_back(VT);
									VT.clear();
									VT.push_back(i);
									VT.push_back(j);
									Reg[i+1][j].From.push_back(VT);
									VT.clear();
									break;
								}
					default : break;
				}
			}
		}
		
		char c = 'a';
		char Col[MAXARR][MAXARR];
		
		for (i=1; i<=H; i++)
			fill(Col[i], Col[i]+W+1, '-');
		
		for (i=1; i<=H; i++)
		{
			for (j=1; j<=W; j++)
			{
				if (Col[i][j]=='-')
				{
					queue<int> QuX;
					queue<int> QuY;
					QuX.push(i);
					QuY.push(j);
					
					while (!QuX.empty())
					{
						int PjgQ = QuX.size();
						for (int qs = 0; qs < PjgQ; qs++)
						{
							int Xn = QuX.front();
							int Yn = QuY.front();
							QuX.pop();
							QuY.pop();
							Col[Xn][Yn] = c;
							
							for (int fr = 0; fr < Reg[Xn][Yn].From.size(); fr++)
							{
								int Xf = Reg[Xn][Yn].From[fr][0];
								int Yf = Reg[Xn][Yn].From[fr][1];
								if (Col[Xf][Yf]=='-')
								{
									QuX.push(Xf);
									QuY.push(Yf);
								}
							}
							
							for (int ft = 0; ft < Reg[Xn][Yn].To.size(); ft++)
							{
								int Xt = Reg[Xn][Yn].To[ft][0];
								int Yt = Reg[Xn][Yn].To[ft][1];
								if (Col[Xt][Yt]=='-')
								{
									QuX.push(Xt);
									QuY.push(Yt);
								}
							}
						}
					}
					c++;
				}
			}
		}
		
		printf("Case #%d:\n", test);
		for (i=1; i<=H; i++)
		{
			for (j=1; j<=W-1; j++)
				printf("%c ", Col[i][j]);
			printf("%c\n", Col[i][W]);
		}
	}
	
	return 0;
}

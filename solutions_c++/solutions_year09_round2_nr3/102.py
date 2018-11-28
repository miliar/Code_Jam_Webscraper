#include<stdio.h>
#include<string>
#include<vector>
#define pb push_back
#define mkp make_pair

using namespace std;

const int maxn = 30;
const int maxl = 300;

string STR[maxn][maxn][maxl * 2 + 3];
int DIN[maxn][maxn][maxl * 2 + 3];
int NRT,N,M,Q[maxl];
char S[maxn][maxn];
int ANS[maxl];
const int X[5] = {0,1,0,-1,0};
const int Y[5] = {0,0,1,0,-1};
vector<pair<int,pair<int,int> > > VECT;

int main()
{
	freopen("math.in","r",stdin);
	freopen("math.out","w",stdout);
	scanf("%d\n",&NRT);
//	printf("%d\n",'-' < '+');
//	return 0;
	for(int i = 1;i <= NRT; ++i)
	{
		printf("Case #%d:\n",i);
		scanf("%d %d",&N,&M);
		for(int i = 1;i <= N; ++i)
		{
				for(int j = 1;j <= N; ++j)
				{
					scanf("%c",&S[i][j]);		
//					printf("%c\n",S[i][j]);
					while(!((S[i][j] >= '0' && S[i][j] <= '9') || S[i][j] == '+' || S[i][j] == '-')) scanf("%c",&S[i][j]);			
				}
		}
/*		for(int i = 1;i <= N; ++i)
		{
				for(int j = 1;j <= N; ++j) printf("%c",S[i][j]);
			printf("\n");
		}*/
		int maxc = 0;
		for(int i = 1;i <= M; ++i)
		{	
			scanf("%d\n",&Q[i]);
			maxc = max(maxc,Q[i]);
		}
		for(int i = 1;i <= N; ++i) for(int j = 1;j <= N; ++j) for(int l = 0;l <= maxl * 2; ++l) {DIN[i][j][l] = 10000;STR[i][j][l].clear();}
		VECT.clear();
		for(int i = 1;i <= N; ++i)
			for(int j = 1;j <= N; ++j)
			{
				if (S[i][j] == '+' || S[i][j] == '-') continue;
				DIN[i][j][maxl + S[i][j] - '0'] = 1;
				VECT.pb(mkp(i,mkp(j,maxl + S[i][j] - '0')));
				STR[i][j][maxl + S[i][j] - '0'] = S[i][j];
//				printf("%c",S[i][j]);
			}
//		printf("%d\n",maxc);
		for(int i = 0;i < (int)VECT.size(); ++i)
		{
			int x = VECT[i].first;
			int y = VECT[i].second.first;
			int v = VECT[i].second.second;
//			printf("%d %d %d %s\n",x,y,v,STR[x][y][v].c_str());
			for(int i = 1;i <= 4; ++i)
			{
				int x1 = x + X[i];
				int y1 = y + Y[i];
				if (!(x1 >= 1 && x1 <= N && y1 >= 1 && y1 <= N))continue;
				int semn = 1;
				string s1 = STR[x][y][v];
				s1 += S[x1][y1];
				if (S[x1][y1] == '-') semn = -1;
				int xaux = x1,yaux = y1;
				for(int j = 1;j <= 4; ++j)
				{
					x1 = xaux;y1 = yaux;
					x1 += X[j];
					y1 += Y[j];
					if (!(x1 >= 1 && x1 <= N && y1 >= 1 && y1 <= N))continue;
					s1 += S[x1][y1];
					int val = v + semn * (S[x1][y1] - '0');
//					printf("%d\n",val);
					if (val < 0 || val > maxl * 2) continue;
					if (DIN[x1][y1][val] > DIN[x][y][v] + 2 || (DIN[x1][y1][val] == DIN[x][y][v] + 2 && STR[x1][y1][val] > s1))
					{
						STR[x1][y1][val] = s1;
						DIN[x1][y1][val] = DIN[x][y][v] + 2;
						VECT.pb(mkp(x1,mkp(y1,val)));
					}
					s1 = STR[x][y][v] + S[xaux][yaux];
				}
								  
			}
		}
		for(int nr = 1;nr <= M; ++nr)
		{
			ANS[nr] = 1000;
			Q[nr] += maxl;
			string s;
			for(int i = 1;i <= N; ++i)
				for(int j = 1;j <= N; ++j)
				{

					if (DIN[i][j][Q[nr]] < ANS[nr] || (DIN[i][j][Q[nr]] == ANS[nr] && s > STR[i][j][Q[nr]])) 
					{
						ANS[nr] = DIN[i][j][Q[nr]];
						s = STR[i][j][Q[nr]];
					}
				}	
			printf("%s\n",s.c_str());		
		}
	}


	return 0;
}



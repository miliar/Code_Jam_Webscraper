#include <cstdio>
#include <vector>
#include <utility>

using namespace std;

vector<pair<int,int> >v;

int tab[4][4];

bool x()
{
	for(int i=0;i<4;i++)
	{
		for(int j=0;j<4;j++)
		{
			if(tab[i][j]^2) break;
			if(j==3) return true;
		}
		for(int j=0;j<4;j++)
		{
			if(tab[j][i]^2) break;
			if(j==3) return true;
		}
	}
	if(tab[0][0]==2 && tab[1][1]==2 && tab[2][2]==2 && tab[3][3]==2) return true;
	if(tab[0][3]==2 && tab[1][2]==2 && tab[2][1]==2 && tab[3][0]==2) return true;
	return false;
}

void przyp()
{
	v.resize(0);
	bool draw=true;
	for(int i=0;i<4;i++) for(int j=0;j<4;j++)
	{
		char c;
		scanf(" %c",&c);
		if(c=='T') tab[i][j]=2,v.push_back(make_pair(i,j));
		else if(c=='X') tab[i][j]=2;
		else if(c=='O') tab[i][j]=3;
		else tab[i][j]=0,draw=false;
	}
	if(x())
	{
		printf("X won\n");
		return;
	}
	for(int i=0;i<4;i++) for(int j=0;j<4;j++)
	{
		if(tab[i][j]==2) tab[i][j]=3;
		else if(tab[i][j]==3) tab[i][j]=2;
	}
	for(int i=0;i<v.size();i++) tab[v[i].first][v[i].second]=2;
	if(x())
	{
		printf("O won\n");
		return;
	}
	if(draw) printf("Draw\n");
	else printf("Game has not completed\n");
}

int main()
{
	int t;
	scanf("%d",&t);
	for(int i=1;i<=t;i++)
	{
		printf("Case #%d: ",i);
		przyp();
	}
	return 0;
}

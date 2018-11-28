#include <iostream>
#include <fstream>
#include <vector>
using namespace std;

#define MAX 102
#define MAXN 100000
int  inTable[MAX][MAX];
char outTable[MAX][MAX];
char lc;
int H,W;
struct point
{
	int i;
	int j;
};

bool getSink(int i, int j, int& nexti, int& nextj)
{
	int min = 1000000;
	if(inTable[i][j]  < inTable[i+1][j] && inTable[i][j]<inTable[i][j-1] && inTable[i][j]<inTable[i][j+1] && inTable[i][j]<inTable[i-1][j])
	{
		nexti = i;
		nextj = j;
		return true;
	}
	else if(inTable[i+1][j] <= inTable[i-1][j] && inTable[i+1][j] <= inTable[i][j+1] && inTable[i+1][j] <= inTable[i-1][j])
	{
		nexti = i+1;
		nextj = j;
		return false;
	}
	else if(inTable[i][j-1] < inTable[i+1][j] && inTable[i][j-1] <= inTable[i][j+1] && inTable[i][j-1] <= inTable[i-1][j])
	{
		nexti = i;
		nextj = j-1;
		return false;
	}
	else if(inTable[i][j+1] < inTable[i+1][j] && inTable[i][j+1] < inTable[i-1][j] && inTable[i][j+1] <= inTable[i-1][j])
	{
		nexti = i;
		nextj = j+1;
		return false;
	}
	else if(inTable[i-1][j] < inTable[i+1][j] && inTable[i-1][j] <= inTable[i][j+1] && inTable[i-1][j] <= inTable[i-1][j]) 
	{
		nexti = i-1;
		nextj = j;
		return false;
	}

}
void setLable(int i,int j, char c)
{
	vector<point> vc;
	point p,tp;
	p.i =i;
	p.j =j;
	vc.push_back(p);
	while(vc.size () > 0)
	{
		vc.push_back(tp);
		vc.pop_back();
		if(outTable[i+1][j] == 0 && inTable[i+1][j] > inTable[tp.i][tp.j])
		{
			p.i = i+1;
			p.j = j;
			outTable[p.i][p.j] = c;
			if(p.i <= H && p.i >= 1 && p.j <= W && p.j >=1)
			{
				vc.push_back(p);
			}
		}

		if(outTable[i][j-1] == 0 && inTable[i][j-1] > inTable[tp.i][tp.j])
		{
			p.i = i;
			p.j = j-1;
			outTable[p.i][p.j] = c;
			if(p.i <= H && p.i >= 1 && p.j <= W && p.j >=1)
			{
				vc.push_back(p);
			}
		}

		if(outTable[i][j+1] == 0 && inTable[i][j+1] > inTable[tp.i][tp.j])
		{
			p.i = i;
			p.j = j+1;
			outTable[p.i][p.j] = c;
			if(p.i <= H && p.i >= 1 && p.j <= W && p.j >=1)
			{
				vc.push_back(p);
			}
		}

		if(outTable[i-1][j] == 0 && inTable[i-1][j] > inTable[tp.i][tp.j])
		{
			p.i = i-1;
			p.j = j;
			outTable[p.i][p.j] = c;
			if(p.i <= H && p.i >= 1 && p.j <= W && p.j >=1)
			{
				vc.push_back(p);
			}
			
		}
		
	}
	
	
}
void label()
{
	int i,j;
	int nexti,nextj;
	char lc = 'a';

	for(i=1; i <= H; ++i)
	{
		for(j=1; j <= W; ++j )
		{
	
			nexti = 0;
			nextj = 0;
			if(outTable[i][j] != 0)
			{
				continue;
			}
			if( getSink(i,j,nexti,nextj) == false)
			{
				i = nexti;
				j = nextj;
				cout<<i<<" "<<j<<endl;
			}
			else
			{
				outTable[i][j] = lc;
				cout<<lc<<outTable[i][j]<<endl;
				setLable(i,j, lc);
				lc ++;
				i=1;
				j=1;
				return;
			}
		}
	}
}

int main()
{
	int N;

	int n;
	int  inTable[MAX][MAX];
	char outTable[MAX][MAX];
	memset(inTable,0, sizeof(int)*MAX*MAX);
	memset(outTable, 0, sizeof(char)*MAX*MAX);

	ifstream fin("B.in");
	ofstream fout("B.out");
	fin>>N;
	n=N;
	int i,j;

	while(n--)
	{
		fin>>H>>W;
		for(i=1; i<=H; ++i)
		{
			for(j=1; j<=W; ++j)
			{
				fin>>inTable[i][j];
			}
			
		}
		for(i=0; i < H +2; ++i)
		{
			inTable[i][0] = MAXN;
			inTable[i][W+1] = MAXN;
		}
		for(i=0; i<W+2; ++i)
		{
			inTable[0][i] = MAXN;
			inTable[H+1][i] = MAXN;
		}
		label();
		
		
		fout<<"Case #"<<n<<": "<<endl;
		for(i=1; i <= H; ++i)
		{
			for(j=1; j<=W; ++j)
			{
				cout<<outTable[i][j]<<" ";
			}
			cout<<endl;
		}
	}
		


	return 0;
}
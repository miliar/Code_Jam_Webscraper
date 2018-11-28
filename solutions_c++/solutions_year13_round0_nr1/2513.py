#include <iostream>
#include <cstdio>
using namespace std;

int t;
int m[5][5];
int rc[9];
int d[3];
int draw;

int main()
{
	int k, i, j;
	char tmp;
	int x, y;
	bool jump;

	//freopen("in.txt", "r", stdin);
	//freopen("out.txt", "w", stdout);

	cin>>t;
	for (k=1; k<=t; k++)
	{
		//init
		draw = x = y = d[1]= d[2]= 0;
		for (i=1; i<=8; i++)
			rc[i] = 0;
		//input
		for (i=1; i<=4; i++)
		{
			for (j=1; j<=4; j++)
			{
				cin>>tmp;
				switch(tmp)
				{
					case 'X':
						m[i][j] = 1;
						rc[i]++; rc[j+4]++;
						break;
					case 'O':
						m[i][j] = -1;
						rc[i]--; rc[j+4]--;
						break;
					case 'T':
						m[i][j] = 0;
						x = i; y = j;
						break;
					case '.':
						m[i][j] = 0;
						draw = 1;
						break;
				}
			}
		}
		//judge1
		jump = false;
		for (i=1; i<=8; i++)
		{
			if (rc[i]==4)
			{
				cout<<"Case #"<<k<<": X won"<<endl;
				jump = true; break;
			}
			if (rc[i]==-4)
			{
				cout<<"Case #"<<k<<": O won"<<endl;
				jump = true; break;
			}
		}
		if (jump) continue;
		//judge3
		for (i=1; i<=4; i++)
		{
			d[1] += m[i][i];
			d[2] += m[i][4-i+1];
		}
		if (d[1]==4 || d[2] == 4)
		{
			cout<<"Case #"<<k<<": X won"<<endl;
			continue;
		}
		if (d[1]==-4 || d[2] == -4)
		{
			cout<<"Case #"<<k<<": O won"<<endl;
			continue;
		}
		//judge2
		if (x>0)
		{
			if (rc[x]+1==4 || rc[x+4]+1==4)
			{
				cout<<"Case #"<<k<<": X won"<<endl;
				continue;
			}
			if (rc[x]-1==-4 || rc[x+4]-1==-4)
			{
				cout<<"Case #"<<k<<": O won"<<endl;
				continue;
			}
			if (x==y && d[1]+1==4)
			{
				cout<<"Case #"<<k<<": X won"<<endl;
				continue;
			}
			if (x==y && d[1]-1==-4)
			{
				cout<<"Case #"<<k<<": O won"<<endl;
				continue;
			}
			if (x+y==5 && d[2]+1==4)
			{
				cout<<"Case #"<<k<<": X won"<<endl;
				continue;
			}
			if (x+y==5 && d[2]-1==-4)
			{
				cout<<"Case #"<<k<<": O won"<<endl;
				continue;
			}
		}
		if (draw == 0)
			cout<<"Case #"<<k<<": Draw"<<endl;
		else
			cout<<"Case #"<<k<<": Game has not completed"<<endl;
	}
	return 0;
}
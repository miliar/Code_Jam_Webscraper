//CODEJAM - B

#include <iostream>
#include <fstream>
using namespace std;

int n,m;
int req0[105];
int req1[105][105];
bool req2[105][105];
int bestN;
bool bestM[15];
bool curM[15];

void rec(int i,int curN)
{
	//done?
	if (i==n)
	{
		//check for validity
		int a,b;
			for (a=0; a<m; a++)
			{
					for (b=0; b<req0[a]; b++)
						if (curM[req1[a][b]]==req2[a][b])
							goto cont;
				return;
cont:
				a=a;
			}
		//all good!!!
		bestN=curN;
		memcpy(bestM,curM,sizeof(curM));
		return;
	}
	//continue?
	if (curN<bestN)
	{
		//malt
		if (curN+1<bestN)
		{
			curM[i]=true;
			rec(i+1,curN+1);
		}
		//non-malt
		curM[i]=false;
		rec(i+1,curN);
	}
}

int main()
{
	//vars
	ifstream f ("B.in");
	ofstream g ("B.out");
	int t,tt,a,b;
	//testcase loop
	f >> tt;
		for (t=1; t<=tt; t++)
		{
			//input
			f >> n;
			f >> m;
				for (a=0; a<m; a++)
				{
					f >> req0[a];
						for (b=0; b<req0[a]; b++)
						{
							f >> req1[a][b] >> req2[a][b];
							req1[a][b]--;
						}
				}
			//brute force
			bestN=999;
			rec(0,0);
			//output
			cout << "Case #" << t << ": ";
			g << "Case #" << t << ": ";
				if (bestN==999)
				{
					cout << "IMPOSSIBLE" << endl;
					g << "IMPOSSIBLE" << endl;
				}
				else
				{
						for (a=0; a<n; a++)
							if (bestM[a])
							{
								cout << "1 ";
								g << "1 ";
							}
							else
							{
								cout << "0 ";
								g << "0 ";
							}
					cout << endl;
					g << endl;
				}
		}
	return(0);
}
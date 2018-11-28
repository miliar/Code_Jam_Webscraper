#include <iostream>
#include <vector>
#include <map>

using namespace std;

typedef pair<int,int> PI;

vector <vector <int> > Pi,Pj;

void rep (int i, int j, int &si, int &sj)
{
	if (Pi[i][j]==i and Pj[i][j]==j)
	{
		si=i;sj=j;
		return;
	}
	rep(Pi[i][j],Pj[i][j],si,sj);
	Pi[i][j]=si;
	Pj[i][j]=sj;
}

void une (int i1, int j1, int i2, int j2)
{
	int r1i,r1j,r2i,r2j;
	rep (i1,j1,r1i,r1j);
	rep (i2,j2,r2i,r2j);
	Pi[r1i][r1j]=r2i;
	Pj[r1i][r1j]=r2j;
}

int di[4]={-1,0,0,1};
int dj[4]={0,-1,1,0};

int main()
{
	int T;
	cin >> T;
	for (int caso=1;caso<=T;caso++)
	{
		int H,W;
		cin >> H >> W;
		vector <vector <int> > M (H, vector <int> (W));
		for (int i=0;i<H;i++)
		{
			for (int j=0;j<W;j++)
				cin >> M[i][j];
		}
		Pi = Pj = vector <vector <int> >  (H, vector <int> (W));
		for (int i=0;i<H;i++)
		{
			for (int j=0;j<W;j++)
			{
				Pi[i][j]=i;
				Pj[i][j]=j;
			}
		}
		for (int i=0;i<H;i++)
		{
			for (int j=0;j<W;j++)
			{
				int am = M[i][j];
				int dm = -1;
				for (int d=0;d<4;d++)
				{
					int ni=i+di[d];
					int nj=j+dj[d];
					if (ni>=0 and ni<H and nj>=0 and nj<W)
					{
						if (M[ni][nj]<am)
						{
							am=M[ni][nj];
							dm=d;
						}
					}
				}
				if (dm>-1)
				{
					int ni=i+di[dm];
					int nj=j+dj[dm];
					Pi[i][j]=ni;
					Pj[i][j]=nj;
				}
			}
		}
		cout << "Case #" << caso << ":" << endl;
		char lac = 'a';
		map <PI, char> ral;
		for (int i=0;i<H;i++)
		{
			for (int j=0;j<W;j++)
			{
				if (j>0)
					cout << " ";
				int ri,rj;
				rep (i,j,ri,rj);
				PI r (ri,rj);
				char let = lac;
				if (ral.find(r)==ral.end())
					ral[r]=lac++;
				else
					let = ral[r];
				cout << let;
			}
			cout << endl;
		}
	}
}

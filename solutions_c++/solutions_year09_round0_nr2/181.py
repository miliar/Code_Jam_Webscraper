#include <iostream>
using namespace std;

int alt[100][100];
char label[100][100];

int H, W;

int di[] = {-1, 0, 0, 1};
int dj[] = {0, -1, 1, 0};

void flood(int i, int j, char ch, int mi=-1, int mj=-1)
{
	if(i<0 || i>=H || j<0 || j>=W) return;
	if(label[i][j] != '-') return;

	int ni=-1, nj=-1;
	int best = alt[i][j];

	for(int k=0 ; k<4 ; k++)
	{
		int ti = i + di[k];
		int tj = j + dj[k];

		if(ti>=0 && ti<H && tj>=0 && tj<W && alt[ti][tj]<best)
		{
			best = alt[ti][tj];
			ni = ti;
			nj = tj;
		}
	}

	if((mi==-1 && mj==-1) || (ni==mi && nj==mj))
	{
		label[i][j] = ch;
		for(int k=0 ; k<4 ; k++)
		{
			int ti = i + di[k];
			int tj = j + dj[k];

			if(ti>=0 && ti<H && tj>=0 && tj<W)
			{
				if(alt[ti][tj] > alt[i][j])
					flood(ti, tj, ch, i, j);
			}
		}

		flood(ni, nj, ch);
	}
}

int main()
{
	int T;
	cin >> T;

	for(int t=1 ; t<=T ; t++)
	{
		cin >> H >> W;

		for(int i=0 ; i<H ; i++)
			for(int j=0 ; j<W ; j++)
			{
				cin >> alt[i][j];
				label[i][j] = '-';
			}

		char curr = 'a' - 1;
		for(int i=0 ; i<H ; i++)
			for(int j=0 ; j<W ; j++)
				if(label[i][j] == '-')
					flood(i, j, ++curr);

		cout << "Case #" << t << ":" << endl;
		for(int i=0 ; i<H ; i++, cout<<endl)
			for(int j=0 ; j<W ; j++)
				cout << label[i][j] << " ";
	}

	return 0;
}

#include <cstdio>
#include <iostream>
#include <sstream>
#include <string>
#include <vector>
#include <algorithm>

using namespace std;

const int MaxN = 105;

int N;
string color[MaxN];
int bpos[MaxN];
int nextO[MaxN], nextB[MaxN];

int main()
{
	int Ncase;
	freopen("0.a_large.in", "r", stdin);
	freopen("0.a_large.out", "w", stdout);
	cin >> Ncase;
	for (int i = 0; i < Ncase; ++i)
	{
		cin >> N;
		for (int j = 0; j < N; ++j)
			cin >> color[j] >> bpos[j];
		
		for (int j = 0; j < N; ++j)
		{
			if (color[j] == "O") nextO[j] = bpos[j];
			if (color[j] == "B") nextB[j] = bpos[j];
			for (int k = j+1; k < N; ++k)
				if (color[k] == color[j])
				{
					if (color[j] == "O") nextO[j] = bpos[k];
					if (color[j] == "B") nextB[j] = bpos[k];
					break;
				}
		}

		//for (int j = 0; j < N; ++j)
		//	cout << color[j] << " " << bpos[j] << " " << nextO[j] << " " << nextB[j] << endl;
		//if (i == 3) while (1);

		int dirB = 0, dirO = 0;
		int nextBAim = 1, nextOAim = 1;
		for (int j = 0; j < N; ++j)
			if (color[j] == "O")
			{
				nextOAim = bpos[j];
				if (bpos[j] > 1) dirO = 1;
				else dirO = 0;
				break;
			}
		for (int j = 0; j < N; ++j)
			if (color[j] == "B")
			{
				nextBAim = bpos[j];
				if (bpos[j] > 1) dirB = 1;
				else dirB = 0;
				break;
			}

		int posO = 1, posB = 1;
		int time = 0, cntAim = 0;
		while (true)
		{
			if (color[cntAim] == "O" && posO == bpos[cntAim])
			{
				nextOAim = nextO[cntAim];
				if (nextO[cntAim] > posO)
					dirO = 1;
				else if (nextO[cntAim] < posO)
					dirO = -1;
				else	dirO = 0;
				posB += dirB;
				cntAim++;
			}
			else if (color[cntAim] == "B" && posB == bpos[cntAim])
			{
				nextBAim = nextB[cntAim];
				if (nextB[cntAim] > posB)
					dirB = 1;
				else if (nextB[cntAim] < posB)
					dirB = -1;
				else	dirB = 0;
				posO += dirO;
				cntAim++;
			}
			else
			{
				posB += dirB;
				posO += dirO;
			}
			++time;
			if (cntAim >= N) break;
			if (posB == nextBAim) dirB = 0;
			if (posO == nextOAim) dirO = 0;
			//cout << posB << " " << posO << " " << cntAim << " " << time << "     " << nextBAim << " " << nextOAim << endl;
		}
		cout << "Case #" << i+1 << ": " << time << endl;
	}
}

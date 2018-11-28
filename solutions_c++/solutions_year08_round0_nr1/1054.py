
#include <fstream>
#include <string>
#include <vector>
#include <iostream>
#include <algorithm>
#include <conio.h>
using namespace std;

int S;
int Q;

vector<string> ss;
int qq[1000];
int qMap[1000][100];

int go(int indexQ, int numS)
{
	while (indexQ < Q)
	{
		if (qq[indexQ] == numS)
		{
			if (qMap[indexQ][numS] != 2000)
			{
				return qMap[indexQ][numS];
			}
			int minTime = 2000;
			for (int i=0; i<S; i++)
			{
				if (i!=numS)
				{
					int tTime = go(indexQ+1, i);
					if (tTime < minTime)
					{
						minTime = tTime;
					}
				}
			}
			qMap[indexQ][numS] = minTime + 1;
			return minTime + 1;
		}
		indexQ ++;
	}
	return 0;
}

void main()
{
	ifstream inf("A-large.in");
	ofstream outf("A-large.out");

	int i;
	int N;
	inf >> N;
	int time;
	for (time=0; time <N; time++)
	{
		for (i=0; i<1000; i++)
		{
			for (int j=0; j<100; j++)
			{
				qMap[i][j] = 2000;
			}
		}

		inf >> S;
		ss.clear();		
		char tt[101];
		inf.getline(tt, 101);
		for (i=0; i<S; i++)
		{
			memset(tt, '\0', 101);
			inf.getline(tt, 101);
			string tStr(tt);
			ss.push_back(tStr);

		//	cout << tt << endl;
		}

		inf >> Q;
		inf.getline(tt, 101);
		for (i=0; i<Q; i++)
		{
			memset(tt, '\0', 101);
			inf.getline(tt, 101);
			string tStr(tt);
			int j;
			for (j=0; j<S; j++)
			{
				if (tStr == ss[j])
				{
					qq[i] = j;
					break;
				}
			}
		}

		int minTime = 2000;
		for (int i=0; i<S; i++)
		{
			int tTime = go(0, i);
			if (tTime < minTime)
			{
				minTime = tTime;
			}
		}

		outf << "Case #" << time+1 << ": " << minTime << endl;

	}

	inf.close();
	outf.close();
}

#include <cstdlib>
#include <string>
#include <cstdio>
#include <iostream>

using namespace std;


#define forl(x,a,b) for(int x = a; x < b; ++x)

int teams;

int sched[100][100];
int numgames[100];
int numwins[100];
double owp[100];
double oowp[100];

void calcOWP()
{

	forl(j,0,teams)
	{
		double op = 0;
		int games = 0;
		forl(i,0,teams)
		{
			int og = 0, ow = 0;
			if (i == j) continue;
			if (sched[j][i] == -1) continue;
			games++;
			og = numgames[i] - 1;
			ow = numwins[i];
			if (sched[i][j] == 1) ow -= 1;
//			cerr << "j: " << j << " i: " << i << " og " << og << " ow " << ow << endl;
			op += (double)ow/(double)og;
		}
		owp[j] = op/games;
	}
}

void calcOOWP()
{

	forl(j,0,teams)
	{
		double op = 0;
		int games = 0;
		forl(i,0,teams)
		{
			int og = 0, ow = 0;
			if (i == j) continue;
			if (sched[j][i] == -1) continue;
			games++;
			op += owp[i];
		}
		oowp[j] = op/games;
	}
}



main()
{
	int t;
	cout.precision(12);
	cin >> t;
	forl(i,0,t)
	{
		cin >> teams;
		forl(z,0,teams) forl(x,0,teams) sched[z][x] = 0;
		forl(z,0,teams) { numgames[z] = 0; numwins[z] = 0; owp[z] = 0; oowp[z] = 0;}
		forl(k,0,teams)
		{
			string blah;
			cin >> blah;
			forl(l,0,teams)
			{
				int rsp;
				switch(blah[l])
				{
					case '.':
						rsp = -1;
						break;
					case '0':
						numgames[k]++;
						rsp = 0;
						break;
					case '1':
						numgames[k]++;
						numwins[k]++;
						rsp = 1;
						break;
				}
				sched[k][l] = rsp;
			}
		}
		calcOWP();
		calcOOWP();
		cout << "Case #" << i + 1 << ":" << endl;
		forl(i,0,teams)
		{
			double wp = (double)numwins[i]/(double)numgames[i];
//			cerr << "wp: " << wp << " owp: " << owp[i] << " oowp: " << oowp[i] << endl;
			cout <<  wp*0.25 + owp[i]*0.5 + oowp[i]*0.25 << endl;
		}
	}
}

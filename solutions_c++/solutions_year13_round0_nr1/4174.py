#include <stdio.h>
#include <iostream>
#include <fstream>
#include <vector>
#include <limits.h>
#include <string.h>
#include <list>

using namespace std;



int main(void)
{
	unsigned long N;
	//unsigned long lRides, lSeats, nGroups, lEuros;
	//vector<int> vGroup;

	freopen("A-large.in", "rt", stdin);
	//freopen("prova.in", "rt", stdin);
	freopen("data.out", "wt", stdout);

	cin >> N;

	//unsigned long G, S, Best, i, j, p, rN, rS, R, med, mod;
	//vector <int> vP[100];
	//char t[4][4];
	char ci; int fi, win, i, j;
	int f[4][2], c[4][2], d[2][2];


	unsigned long n;
	for (n=1;n<=N;n++)
	{

		for (i=0; i<4; i++) { f[i][0]=1; f[i][1]=1; c[i][0]=1; c[i][1]=1; }
		d[0][0]=1; d[0][1]=1; d[1][0]=1; d[1][1]=1;
		fi = 1; win = -1;

		for (i=0; i<4; i++)
		{
		    for (j=0; j<4; j++)
		    {
		        cin >> ci;
		        if (ci=='X' || ci=='.') { f[i][0]=0; c[j][0]=0; if (i==j) d[0][0]=0; if (i==3-j) d[1][0]=0; }
		        if (ci=='O' || ci=='.') { f[i][1]=0; c[j][1]=0; if (i==j) d[0][1]=0; if (i==3-j) d[1][1]=0; }
                if (ci=='.') fi=0;
		    }
		}

        for (i=0; i<4; i++)
        {   if (f[i][0]==1) win=0;  if (c[i][0]==1) win=0;
            if (f[i][1]==1) win=1;  if (c[i][1]==1) win=1;
        }
        if (d[0][0]==1) win=0; if (d[1][0]==1) win=0;
        if (d[0][1]==1) win=1; if (d[1][1]==1) win=1;


        cout << "Case #" << n << ": " ;
        if (win==0) cout << "O won"; if (win==1) cout << "X won";
        if (win==-1) if (fi==0) cout << "Game has not completed"; else cout << "Draw";
        cout << endl;
   	}
}

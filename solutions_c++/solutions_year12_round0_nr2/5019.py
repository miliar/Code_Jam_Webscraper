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

	//freopen("B-small-attempt3.in", "rt", stdin);
	freopen("B-large.in", "rt", stdin);
	//freopen("prova.in", "rt", stdin);
	//freopen("C-small-practice.in", "rt", stdin);
	freopen("data.out", "wt", stdout);

	cin >> N;

	unsigned long G, S, Best, i, j, p, rN, rS, R, med, mod;
	//vector <int> vP[100];

	unsigned long n;
	for (n=1;n<=N;n++)
	{
		rN = 0; rS = 0;
		cin >> G; cin >> S; cin >> Best;

		for (i=0; i<G; i++)
		{	cin >> p;
			//vP.push_back(j);
            mod = p % 3;
            med = (p-mod)/3;

            if (mod==0)
            {
                if (med >= Best) rN++;
                else if (med+1 == Best && med>0 && med<10) rS++;

            }

            if (mod==1)
            {
                if (med+1 >= Best) rN++;
            }

            if (mod==2)
            {
                if (med+1 >= Best) rN++;
                else if (med+2 == Best && med<9) rS++;
            }
            //cout << p << ": " << med << " " << mod << " ("<< rN <<","<<rS<<")"<< endl;
		}
        if (rS>S) rS = S;
        R = rN + rS;



		cout << "Case #" << n << ": " << R << endl;

   	}
}

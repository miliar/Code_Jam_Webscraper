#include <stdio.h>
#include <iostream>
#include <fstream>
#include <vector>
#include <limits.h>
#include <string.h>
#include <list>
#include <math.h>

using namespace std;



int main(void)
{
	unsigned long N;


	freopen("C-small-attempt0.in", "rt", stdin);
	//freopen("prova.in", "rt", stdin);
	freopen("data.out", "wt", stdout);

	cin >> N;

	unsigned long min, max;
	vector <int> x;
	vector <int> x2;
	int nx;
	//vector <int> vP[100];

	unsigned long n, i, j, k, P;
	int c, c2, co, xa;
    vector<int>::iterator it;

	for (n=1;n<=N;n++)
	{
        P=0;
		cin >> min >> max;
        nx = (int)floor(log10((double)min))+1;

        for (i=min; i<max; i++)
        {
            //cout << "  -- case #" << n << ": " << max << " " << nx << endl;
           j = i;
           for (c=0; c<nx; c++)
           {
               //cout insertant
                it = x.begin();
                x.insert(x.begin(), j%10);

                //x.push_back(j % 10);
                j /= 10;

            }
            //cout << i << " :";
            //for (co=0; co<nx; co++) cout << " "<< x[co]; cout << endl;

            for (c=0; c<nx-1; c++)
            {
                xa = x[nx-1];
                //for (co=0; co<nx; co++) cout << " "<< x[co]; cout << " agafo:"<<xa<< endl;
                x.pop_back();
                //for (co=0; co<nx-1; co++) cout << " "<< x[co]; cout << endl;
                x.insert(x.begin(), xa);

                //for (co=0; co<nx; co++) cout << " "<< x[co]; cout << endl;

                k=0;
                for (c2=0; c2<nx; c2++)
                {
                    k *= 10;
                    k += x[c2];
                }

                if (k==i) c=nx;


                //cout << i << " "<< k;
                if (k>i && k<=max) {P++;}
                //cout << endl;
            }


        }
		//cout << "Case #" << n << ": " << max << " " << nx << endl;
		cout << "Case #" << n << ": " << P << endl;

   	}
}

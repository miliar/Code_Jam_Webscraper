#include <iostream>
#include <fstream>
#include <cmath>
#include <vector>
#include <list>
#include <map>
#include <utility>
#include <string>
#include <algorithm>
#include <string.h>
using namespace std;

long long ans;
long long s,in;
int k;
int main ()
{
    ifstream fin("C.in");
    ofstream fout("C.out");
	bool *isPrime = new bool[1000001];
	memset (isPrime , 0 , 1000001 * sizeof (bool));
	isPrime[0] = 1;
	isPrime[1] = 1;
	for (int i = 2 ; i <= 1000000; i++)
	{
		if (!isPrime[i])
		{
			k = i+i;
			while (k <= 1000000){isPrime[k] = 1; k +=i;}
		}
	}
    int T;
    fin >> T;
    for (int t = 0 ; t < T; t++)
    {
		fin >> in;
		ans = 0;
		if (in == 1){fout << "Case #" << t+1 << ": " << 0 << endl; continue;}
		for (int i = 2 ; (i <= sqrt((double)in) + 1) && (i <= 1000000) ; i++)
		{
			if (!isPrime[i])
			{
				s = i;
				while (1)
				{
					s *= i;
					if (s > in) break;
					if (s < 0) break;
					ans ++ ;
				}
			}
		}
        fout << "Case #" << t+1 << ": " << ans+1 << endl; 
    }
}

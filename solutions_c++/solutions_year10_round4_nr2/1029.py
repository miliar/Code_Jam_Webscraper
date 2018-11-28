#include <cstring>
#include <iostream>
#include <algorithm>

using namespace std;

const int M = 100000000;

int P;
int c[2048];
int prc[2048][20];
int tab[1048][1048][20];

int f(int s, int e, int m, int d = 0)
{
    if (tab[s][e][m] >= 0)
	return tab[s][e][m];
    if (s + 2 >= e)
    {
	if (m > c[s] || m > c[s+1])
	    return (tab[s][e][m] = M);
	if (m == c[s] || m == c[s+1])
	    return (tab[s][e][m] = prc[P-1][s>>1]);
	return (tab[s][e][m] = 0);
    }

    int h = (s+e)>>1;

    int cand1 = prc[d][s>>(P-d)] + f(s, h, m, d+1) + f(h, e, m, d+1);
    cand1 = min(M, cand1);
    int cand2 = f(s, h, m+1, d+1) + f(h, e, m+1, d+1);
    cand2 = min(M, cand2);
    
    return (tab[s][e][m] = min(cand1, cand2));
}

int main()
{
    int T;
    cin >> T;
    for (int t = 1; t <= T; ++t)
    {
	cin >> P;
	for (int i = 0; i < (1<<P); ++i)
	{
	    cin >> c[i];
	}
	for (int p = P-1; p >= 0; --p)
	{
	    for (int i = 0; i < (1<<p); ++i)
	    {
		cin >> prc[p][i];
	    }
	}

	memset(tab, 0xff, sizeof(tab));
       	cout << "Case #" << t << ": " << f(0, 1<<P, 0) << endl;
    }
    
    return 0;
}

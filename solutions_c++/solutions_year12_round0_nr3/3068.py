#include <iostream>
#include <fstream>
#include <map>

using namespace std;

int f(int a)
{
    int i = 1;
    for (; a >= 10; ++i, a /= 10) ;
    return i;
}

int p(int a)
{
	int c = 1;
	while (a--)
		c *= 10;
	return c;
}

main()
{
    ifstream fin("C-small-attempt0.in");
    ofstream fout("c.txt");
    int x, a, b, g, t;
    fin >> x;
    for (int cnt = 1; cnt <= x; ++cnt)
    {
		int c = 0;
		map<int, int> m;
        fin >> a >> b;
        for (int i = a; i <= b; ++i)
        {
            g = f(i);
            for (int j = 1; j < g; ++j)
            {
                t = i / p(j) + i % p(j) * p(g - j);
                if (i != t && t >= a && t <= b && m[i] != t)
                {
					++c;
					m[i] = t;
				}
            }
        }
    	fout << "Case #" << cnt << ": " << c / 2 << endl;
    }
}

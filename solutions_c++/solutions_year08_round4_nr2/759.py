#include <string>
#include <vector>
#include <algorithm>
#include <numeric>

#include <iostream>
#include <fstream>
#include <sstream>
#include <queue>
#include <set>
#include <map>
#include <list>

#include <cstdio>
#include <cstdlib>
#include <cctype>
#include <cassert>

#include <cmath>
#include <complex>
using namespace std;


int main()
{

	ifstream cin("in.txt");
	ofstream cout("out.txt");
	//freopen("out.txt","w",stdout);
	int ncase,m;
	cin >> ncase;
	m = 0;
	while (ncase--)
	{
		m++;
		int x1,x2,y1,y2;
		int N,M,A;
		bool bisok = false;
		cin >> N >> M >> A;
		cout << "Case #" << m << ": " ;
		for (x1 = 0 ; x1 <= N ; x1++)
		{
			for (x2 = 0 ; x2 <= N ; x2++)
			{
				for (y1 = 0 ; y1 <= M ; y1++)
				{
					for (y2 = 0 ; y2 <= M ; y2++)
					{
						if (x1 == 0 && y1 == 0 || x2 == x1 && y2 == y1 || x2 == 0 && y2 == 0 )
							continue;
						if (x2 * y1  - y2 * x1 == A || x2 * y1  - y2 * x1 == -A)
						{

							cout << 0 << " "<<0 <<" "<< x1 << " "<< y1 << " " << x2 << " " << y2 << endl;
							bisok = true;
							break;
						}
					}
					if (bisok)
						break;
				}
				if (bisok)
					break;
			}
			if (bisok)
				break;
		}
		if (!bisok)
			cout << "IMPOSSIBLE" << endl;
		//printf("Case #%d: ",m);
	}
}

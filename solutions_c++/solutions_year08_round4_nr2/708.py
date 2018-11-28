#include <iostream>
#include <vector>
#include <cmath>
#include <algorithm>
#include <string>
#include <fstream>
#include <map>
#include <set>
using namespace std;


int main()
{
	int N;
	cin >> N;

	for(int i = 1; i <= N; ++i)
	{
		int N;
		int M;
		int A;
		cin >> N >> M >> A;

		int x0 = 0;
		int y1 = 0;

		for(int x1 = 0; x1 <= N; ++x1)
			for(int y0 = 0; y0 <= M; ++y0)
				for(int x2 = 0; x2 <= N; ++x2)
					for(int y2 = 0; y2 <= M; ++y2)
					{
						int val = abs( x2*(y0+y2) - (x2-x1)*y2 - x1*y0);
						if (val == A)
						{
							cout << "Case #" << i << ": " <<x0 << ' ' << y0 << ' ' << x1 << ' ' << y1 << ' ' << x2 << ' ' << y2 << endl; 
							goto next;
						}
					}

		cout << "Case #" << i << ": IMPOSSIBLE" << endl;

next:;

	}
}
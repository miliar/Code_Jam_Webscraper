#include <iostream>
#include <string>
#include <vector>
#include <fstream>
using namespace std;


int main()
{
	long long N,n,A,B,C,D,x0,y0,M,tris,c;
	c = 0;
	
	
	freopen("small.in","r",stdin);
	cin>>N;

	while (c < N)
	{
		// Read Input
		cin >> n >> A >> B >> C >> D >> x0 >> y0 >> M;
		long long treesx[100000];
		long long treesy[100000];
tris = 0;
		treesx[0] = x0;
		treesy[0] = y0;

		for(long long i=1; i<n;++i)
		{
			x0 = (A*x0 + B) % M;
			y0 = (C*y0 + D) % M;
			treesx[i] = x0;
			treesy[i] = y0;	
		}
		// Inspect all triangles
		for(long long i = 0; i < n -2; ++i)
		{
			long long xi = treesx[i] % 3;
			long long yi = treesy[i] % 3;

			for(long long j = i+1; j < n-1; ++j)
			{
				long long xj = (xi + treesx[j]) % 3;
				long long yj = (yi + treesy[j]) % 3;

				for (long long k = j+1; k < n; ++k)
				{
					long long xk = (xj + treesx[k]) % 3;
					long long yk = (yj + treesy[k]) % 3;

					if (xk == 0 && yk ==0)
					{
						tris++;
					}
				}
			}
		}
		cout << "Case #" << ++c << ": " << tris << "\n";
	}

	return 0;
}
	

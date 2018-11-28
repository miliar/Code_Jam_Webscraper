// Code Jam 2010 No.3
// Yuxiang Wang @ Tsinghua University

#include <fstream>
#include <memory>
#include <cmath>
using namespace std;

int main()
{
	ifstream in ("input.in");
	int T, R, k, N;
	in >> T;
	
	ofstream out ("output.out");
	for (int i=0; i<T; i++)
	{
		in >> R >> k >> N;
		int *g = new int[N];
		for (int j=0; j<N; j++)
			in >> g[j];
		int sum = 0;
		for (int j=0; j<N; j++)
			sum += g[j];

		int flag = 0, y = 0, r = 0;
		if (sum <= k)
			y = sum * R;
		else
		{
			while (r < R)
			{
				int temp = 0;
				while (temp < k)
				{
					int m = flag % N;
					temp += g[m];
					if (temp <= k)
					{
						flag ++;
						y += g[m];
					}
				}
				r ++;
			}
		}

		out << "Case #" << i+1 << ": " << y << endl;
	}

	out.close();
	return 0;
}
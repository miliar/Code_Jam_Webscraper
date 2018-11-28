#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <fstream>

using namespace std;

/*
The first line of input gives the number of cases, N.
 N test cases follow. Each test case consists of one line containing the integers
  n, A, B, C, D, x0, y0 and M separated by exactly one space. n will be the number of
   trees in the input set. Using the numbers n, A, B, C, D, x0, y0 and M the following
   pseudocode will print the coordinates of the trees in the input set. mod indicates
    the remainder operation.

The parameters will be chosen such that the input set of trees will not have duplicates.

X = x0, Y = y0
print X, Y
for i = 1 to n-1
  X = (A * X + B) mod M
  Y = (C * Y + D) mod M
  print X, Y
 *
 */
struct Pt
{
	unsigned long long x, y;
	Pt(unsigned long long _x, unsigned long long _y)
	{
		x = _x;
		y = _y;
	}
};
int main()
{
	ifstream cin ("A.in");
	ofstream cout ("A.out");
	unsigned long long N, n, A, B, C, D, X0, Y0, M;
	cin >> N;
	for (int iCase = 1; iCase <= N; ++iCase)
	{
		vector <Pt> Points;
		cin >> n >> A >> B >> C >> D >> X0 >> Y0 >> M;
		unsigned long long X = X0;
		unsigned long long Y = Y0;

		Points.push_back(Pt(X, Y));
		for (unsigned long long i=1; i < n; ++i)
		{
			X = (((A%M)*(X%M))%M+(B%M))%M;
			Y = (((C%M)*(Y%M))%M+(D%M))%M;

			Points.push_back(Pt(X,Y));
		}

		int Count =0;

		for (int i=0 ; i < n; ++i)
		{
			for (int j=i+1; j < n; ++j)
			{
				for (int k=j+1; k < n; ++k)
				{
					unsigned long long X1 = Points[i].x;
					unsigned long long Y1 = Points[i].y;

					unsigned long long X2 = Points[j].x;
					unsigned long long Y2 = Points[j].y;

					unsigned long long X3 = Points[k].x;
					unsigned long long Y3 = Points[k].y;

					if (((X1 + X2 + X3) % 3 == 0) && ((Y1 + Y2 + Y3) % 3 == 0))
					{
						//cout << "Triangle at : " << X1 <<" "<< Y1 << "    "<< X2 << " " <<Y2 << "      " << X3 << " " << Y3 << endl;
						Count++;
					}
				}
			}
		}

		cout << "Case #"<<iCase<<": "<<Count<<endl;
	}
	return 0;
}

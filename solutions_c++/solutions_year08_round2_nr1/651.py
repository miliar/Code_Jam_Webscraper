#include <fstream>
#include <iostream>
#include <string>

using namespace std;
int vertex[100000][2];

int main()
{
	int test_cases;
	ofstream out("out.txt");
	ifstream in("A.in");
	//string line;
	//getline(in, line);
	in >> test_cases;
	for(int i = 0; i < test_cases; i++)
	{	int n, a, b, c, d, m;
		long long x, y;
		in >> n >> a >> b >> c >> d >> x >> y >> m;
		vertex[0][0] = x;
		vertex[0][1] = y;
		//cout << x << " " << y << endl;
		for(int j = 1; j < n; j++)
		{
			x = (a * x + b) % m;
			y = (c * y + d) % m;
			vertex[j][0] = x % 3;
			vertex[j][1] = y % 3;
		//	cout << x << " " << y << endl;
		}
		long answer = 0;
		for(int x1 = 0; x1 < n - 2; x1++)
			for(int x2 = x1 + 1; x2 < n - 1; x2++)
				for(int x3 = x2 + 1; x3 < n; x3++)
					if( ((vertex[x1][0] + vertex[x2][0] + vertex[x3][0]) % 3 == 0) && 
						((vertex[x1][1] + vertex[x2][1] + vertex[x3][1]) % 3 == 0) )
							answer++;
		out << "Case #" << i + 1 << ": " << answer << endl;
	}
	return 0;
}
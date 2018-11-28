#include <iostream>
#include <fstream>
#include <vector>
#include <algorithm>
#include <cstdlib>
#include <memory.h>
using namespace std;

ifstream in;
ofstream out;

int rows[64];

bool is_ok(int n)
{
	int rows2[64];
	memcpy(rows2, rows, n * sizeof(int));
	sort(rows2, rows2 + n);

	for(int i = 0; i < n; ++i)
	{
		if(rows2[i] > i)
			return false;
	}
	return true;
}

int main(int argc, char** argv)
{
	in.open(argv[1]);
	out.open(argv[2]);

	int T;
	in >> T;
	for(int it = 1; it <= T; ++it)
	{
		int N;
		in >> N;
		for(int i = 0; i < N; ++i)
		{
			int v = 0;
			for(int j = 0; j < N; ++j)
			{
				char c;
				in >> skipws >> c;
				if(c == '1')
					v = max(v, j);
				else if(c != '0')
					abort();
			}
			rows[i] = v;
		}

		cout << "Case " << it << endl;
		for(int i = 0; i < N; ++i)
		{
			cout << rows[i] << endl;
		}

		if(!is_ok(N))
			abort();

		int r = 0;

		for(int j = N - 1; j > 0; --j)
		{
			for(int k = j; k >= 0; --k)
			{
				swap(rows[k], rows[j]);
				if(is_ok(j))
				{
					swap(rows[k], rows[j]);
					for(int l = k; l < j; ++l)
					{
						swap(rows[l], rows[l + 1]);
					}
					r += j - k;
					break;
				}
				swap(rows[k], rows[j]);
			}
		}

		for(int i = 0; i < N; ++i)
		{
			cout << rows[i] << endl;
		}
		out << "Case #" << it << ": " << r << endl;
	}

	return 0;
}

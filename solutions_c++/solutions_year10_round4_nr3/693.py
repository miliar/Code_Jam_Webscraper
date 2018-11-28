#include <fstream>
#include <string>
using namespace std;

bool A[102][102];
int C, R, X1, X2, Y1, Y2;

bool evolve()
{
	bool ret = false;
	for (int i=100; i>0; --i)
	{
		for (int j=100; j>0; --j)
		{
			A[i][j] = A[i][j] ? (A[i-1][j] || A[i][j-1]) : (A[i-1][j] && A[i][j-1]);
			if (A[i][j]) ret = true;
		}
	}
	return ret;
}

int main()
{
	ifstream fin("C-small-attempt0.in");
	ofstream fout("C-small-attempt0.out");

	fin >> C;
	for (unsigned int z=1; z<=C; ++z)
	{
		memset(A, 0, sizeof(A));

		fin >> R;
		for (int k=0; k<R; ++k)
		{
			fin >> X1 >> Y1 >> X2 >> Y2;
			for (int i=X1; i<=X2; ++i)
				for (int j=Y1; j<=Y2; ++j)
					A[i][j] = true;
		}

		int ret = 1;
		while (evolve()) ++ret;

		fout << "Case #" << z << ": " << ret << endl;
	}

	return 0;
}
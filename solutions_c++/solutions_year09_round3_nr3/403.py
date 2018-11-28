#include <fstream>
#include <algorithm>

using namespace std;

ifstream fin ("input.txt");
ofstream fout("output.txt");

const int MAX = 110;

bool a[MAX];
int l, k, sum;
int v[MAX];
int n;
int best_ans;

int main()
{
	fin >> n;

	for (int jj = 0; jj < n; ++jj)
	{
		fin >> k >> l;
		best_ans = k*(k+1);
		for (int i = 0; i < l; ++i)
		{
			fin >> v[i]; --v[i];
		}
		sort(v, v+l);
		do
		{
			sum = 0;
			memset(a, false, sizeof(a));
			for (int i = 0; i < l; ++i)
			{
				a[v[i]] = true;
				for (int j = v[i]-1; j >= 0 && !a[j]; --j)
					++sum;
				for (int j = v[i]+1; j < k && !a[j]; ++j)
					++sum;
			}
			best_ans = min(best_ans, sum);
		}while(next_permutation(v, v+l));
		fout << "Case #" << jj+1 << ": " << best_ans << endl;
	}

	return 0;
}
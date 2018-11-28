#include <fstream>
using namespace std;
int main()
{
	const int MAXN = 100;
	int t, i, n, s, p, j, tp[MAXN], result;
	ifstream fin("input.txt");
	ofstream fout("output.txt");
	fin >> t;
	for(i = 1; i <= t; i++)
	{
		fin >> n >> s >> p;
		for(j = 0; j < n; j++)
			fin >> tp[j];
		result = 0;
		for(j = n - 1; j >= 0; j--)
			if((tp[j] + 2) / 3 >= p)
				result++;
			else if(tp[j] >= 2 && tp[j] <= 28 && s > 0 && (tp[j] + 4) / 3 >= p)
			{
				result++;
				s--;
			}
		fout << "Case #" << i << ": " << result << endl;
	}
	return 0;
}
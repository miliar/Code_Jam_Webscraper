#include <fstream>
#include <cstdlib>
using namespace std;

int compare (const void * a, const void * b)
{
  return ( *(int*)a - *(int*)b );
}

int main()
{
	int t;
	ifstream ifs("B-small-attempt0.in");
	ofstream ofs("output.txt");
	ifs >> t;
	for (int i = 0; i < t; i++)
	{
		int n,s,p;
		int t[30];
		ifs >> n >> s >> p;
		for (int j = 0; j < n; j++)
			ifs >> t[j];
		qsort(t, n, sizeof(int), compare);
		int sum = 0;
		for (int j = 0; j < n; j++)
			if (t[j] % 3 == 0)
			{
				if (t[j] / 3 >= p) sum++;
				else if (s > 0 && t[j] / 3 + 1 >= p && t[j] >=p)
				{
					sum++;
					s--;
				}
			}
			else
			{
				if (t[j] / 3 + 1 >= p && t[j] >= p) sum++;
				else if (s > 0 && t[j] % 3 == 2 && t[j] / 3 + 2 >= p && t[j] >= p)
				{
					sum++;
					s--;
				}
			}
				
		ofs << "Case #" << i+1 << ": " << sum << endl;

	}
}

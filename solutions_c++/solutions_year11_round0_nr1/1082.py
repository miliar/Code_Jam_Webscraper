#include <fstream>
#include <string>
using namespace std;

int dist(int a, int b) { return a<b ? b-a : a-b; }
int main()
{
	ifstream fin("A-large.in");
	ofstream fout("A-large.out");

	unsigned int numberOfCases;
	fin >> numberOfCases;
	
	char R;
	int N, P;

	for (unsigned int zz=1; zz<=numberOfCases; ++zz)
	{
		int pos1 = 1, pos2 = 1, t1 = 0, t2 = 0;

		fin >> N;
		for (int i=0; i<N; ++i)
		{
			fin >> R;
			fin >> P;
			if (R == 'O')
			{
				t1 = max(t2+1, t1 + dist(pos1, P) + 1);
				pos1 = P;
			}
			else
			{
				t2 = max(t1+1, t2 + dist(pos2, P) + 1);
				pos2 = P;
			}
		}

		int result = max(t1, t2);

		fout << "Case #" << zz << ": " <<result << endl;
	}

	return 0;
}
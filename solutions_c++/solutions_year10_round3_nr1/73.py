#include <fstream>
#include <algorithm>
#include <set>
#include <vector>
#include <string>
using namespace std;


int main()
{
	ifstream fin("A-large.in");
	ofstream fout("A-large.out");

	int T, N;
	fin >> T; 
	for (int z=1; z<=T; ++z)
	{
		fin >> N;
		vector<int> a(N), b(N);
		for (int j=0; j<N; ++j)
		{
			fin >> a[j] >> b[j];
		}

		unsigned int ans = 0;
		for (int i=0; i<N; ++i)
			for (int j=i+1; j<N; ++j)
				if ((a[i] < a[j]) == (b[i] > b[j]))
					++ans;
		
		fout << "Case #" << z << ": " << ans << endl;
	}

	return 0;
}
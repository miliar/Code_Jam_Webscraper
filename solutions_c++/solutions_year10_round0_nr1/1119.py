#include <fstream>

using namespace std;

int main()
{
	ifstream fin("a.in");
	ofstream fout("a.out");

	unsigned int t, n, k;

	fin >> t;

	for (int tc = 1; tc <= t; ++tc) {
		fin >> n >> k;
		fout << "Case #" << tc << ": " <<  ((((1<<n)-1)&k) == ((1<<n)-1) ? "ON" : "OFF") << endl;
	}

	fin.close();
	fout.close();

	return 0;
}
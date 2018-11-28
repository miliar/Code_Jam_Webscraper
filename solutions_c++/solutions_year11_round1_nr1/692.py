#include <fstream>

using namespace std;

bool solve(ifstream& ifs);

int main()
{
	ifstream ifs("input.txt");
	ofstream ofs("output.txt");
	
	int turns;
	ifs >> turns;
	for (int i = 1; i <= turns; ++i) {
		ofs << "Case #" << i << ": ";
		if (solve(ifs)) {
			ofs << "Possible" << endl;
		}
		else {
			ofs << "Broken" << endl;
		}
	}
	
	system("pause");
	return 0;
}

bool solve(ifstream& ifs)
{
	long long n;
	int percent_d;
	int percent_g;
	
	ifs >> n >> percent_d >> percent_g;
	if ((percent_d != 0 && percent_g == 0) || (percent_d != 100 && percent_g == 100)) {
		return false;
	}
	
	if (n < 100) {
		for (int i = 1; i <= n; ++i) {
			if ((i * percent_d) % 100 == 0) {
				return true;
			}
		}
		return false;
	}
	else {
		return true;
	}
}

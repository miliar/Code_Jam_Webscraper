#include <fstream>
#include <string>
#include <iomanip>
using namespace std;

const string s = "welcome to code jam";

string u;
int f[512][20];
int len;

int Count(int i, int j)
{
	if (j == len) return 1;
	if (i == u.size()) return 0;
	int& res = f[i][j];
	if (res != -1) return res;
	res = Count(i+1, j);
	if (u[i] == s[j])
	{
		res += Count(i+1, j+1);
	}
	res %= 10000;
	return res;
}

int main()
{
	len = s.size();
	ifstream ifs("c.in");
	ofstream ofs("c.out");
	getline(ifs, u);
	int t;
	sscanf(u.c_str(), "%d", &t);
	for (int test = 0; test < t; ++test)
	{
		memset(f, -1, sizeof(f));
		getline(ifs, u);
		int res = Count(0, 0);
		ofs << "Case #" << test+1 <<": " << setfill('0') << setw(4) << res << endl;
	}
	return 0;
}
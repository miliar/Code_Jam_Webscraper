#include <iostream>
#include <string>
#include <fstream>

using namespace std;

ifstream in("input.txt");
ofstream out("output.txt");

long long dd[40];

int main()
{
	dd[1] = 1;
	for (int i = 2; i <= 30; i++)
		dd[i] = dd[i - 1] * 2 + 1;
	int n;
	long long k;
	int T;
	in >> T;
	string ans;
	for (int t = 1; t <= T; t++)
	{
		in >> n >> k;
		if (dd[n] > k)
			ans = "OFF";
		else if (dd[n] == k)
			ans = "ON";
		else if (((k + 1) % (dd[n] + 1)) == 0)
			ans = "ON";
		else
			ans = "OFF";
		out << "Case #" << t << ": " << ans << endl;
	}
	return 0;
}
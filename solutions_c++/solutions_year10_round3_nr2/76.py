#include <iostream>
#include <map>
#include <set>
#include <vector>

using namespace std;

int main(int argc, char *argv[])
{
	int cases;
	cin >> cases;
	for(int ci = 0; ci < cases; ++ci)
	{
		long long L, P, C;
		cin >> L >> P >> C;
		int log = 0, res = 0;
		while((L *= C) < P)
			log++;
		while(log)
			(log >>= 1), ++res;
		cout << "Case #" << (ci + 1) << ": " << res << endl;
	}

	return 0;
}

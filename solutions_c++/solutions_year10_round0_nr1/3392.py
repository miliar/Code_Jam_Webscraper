//Sat May  8 04:19:33 CDT 2010
#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <queue>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <cctype>
#include <string>
#include <cstring>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>

using namespace std;

int main(int argc, char* argv[])
{
	freopen("input.in", "r", stdin);
	freopen("output.out", "w", stdout);
	int T;
	cin >> T;
	for(int ncase = 1; ncase <=T; ncase++)
	{
		int N;
		long long K;
		cin >> N >> K;
		cout << "Case #" << ncase << ": ";
		if((K+1) % (long long)(pow(2.0, N))==0 && K!=0)
			cout << "ON" << endl;
		else
			cout << "OFF" << endl;
	}
	fclose(stdin);
	fclose(stdout);
	return 0;
}

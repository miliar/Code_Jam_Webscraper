#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
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
#include <ctime>
using namespace std;

int main()
{
	int T;
	cin >> T;
	for(int i = 1; i <= T; i++)
	{
		int N;
		cin >> N;
		long long xorResult = 0;
		long long total = 0;
		int minNo = 1000001;
		vector<int> num(N);
		for(int j = 0; j < N; j++)
		{
			int no;
			cin >> no;
			xorResult ^= no;
			num[j] = no;
			total += no;
			minNo = min(minNo, no);
		}
		if(xorResult != 0)
		{
			cout << "Case #" << i << ": NO" << endl;
		}
		else
		{
			cout << "Case #" << i << ": " << total - minNo << endl;
		}
		
	}
	return 0;
}

#include <string>
#include <vector>
#include <deque>
#include <map>
#include <set>
#include <cstdio>
#include <cctype>
#include <cmath>
#include <cstdlib>
#include <algorithm>
#include <functional>
#include <numeric>
#include <iostream>
#include <fstream>
#include <utility>
#include <sstream>
#include <cstring>

#define AS(arr)  (sizeof(arr)/sizeof(arr[0]))
#define ALL(c) (c).begin(),(c).end() 
#define SIZE(a) int((a).size())
#define EACH(it,c) for(typeof((c).begin()) it=(c).begin();it!=(c).end();++it)
#define REP(I, T) for(int I=0;(I)<(T);++I)

using namespace std;


int main()
{
	int testcases;
	cin >> testcases;

	REP(testcase, testcases)
	{
		int P, K, L;
		//P一つのキーに割り当てられる数, Kキー数, L文字種数
		cin >> P >> K >> L;
		std::vector<int> ls;
		std::vector<int> keys(K);
		fill(ALL(keys), 0);


		ls.reserve(L);
		REP(i, L)
		{
			int tmp;
			cin >> tmp;
			ls.push_back(tmp);
		}

		sort(ALL(ls));
		reverse(ALL(ls));

		long long ret = 0;
		REP(i, L)
		{
			keys[0]++;
			ret += ls[i] * keys[0];
			sort(ALL(keys));
		}

		cout << "Case #" << testcase+1 << ": " << ret << endl;
		fflush(NULL);
		
	}
	return 0;
}



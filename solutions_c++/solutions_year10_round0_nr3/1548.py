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
		int R, k, N;
		cin >> R >> k >> N;
		vector <int> groups(N);
		for(int j = 0; j < N; j++)
			scanf("%d", &groups[j]);
			
		vector <int> prevIter(N, -1);
		vector <long long> sums;
		long long ret = 0;
		
		int iter = 0, start = 0;
		for(; iter < R; iter++)
		{
			int cur = start;
			if(prevIter[cur] != -1)
				break;
			prevIter[cur] = iter;
			
			long long fill = 0;
			while(fill + groups[cur] <= k)
			{
				fill += groups[cur];
				cur = (cur + 1) % N;
				if(cur == start)
					break;
			}
			sums.push_back(fill);
			ret += fill;
			start = cur;
		}
		
		int cycleLen = iter - prevIter[start];
		vector <long long> cycleSums(sums.end() - cycleLen, sums.end());
		
		/*for(int j = 0; j < cycleLen; j++)
			cout << cycleSums[j] << endl;
		*/
		int remR = R - iter;
		long long total = 0;
		for(int j = 0; j < cycleLen; j++)
			total += cycleSums[j];
		ret += (remR / cycleLen) * total;
		
		int rem = remR % cycleLen;
		for(int j = 0; j < rem; j++)
			ret += cycleSums[j];
			
		cout << "Case #" << i << ": " << ret << endl; 
	}
	return 0;
}

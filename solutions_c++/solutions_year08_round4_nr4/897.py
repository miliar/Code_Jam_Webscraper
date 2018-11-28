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
#include <iostream>
#include <utility>
#include <sstream>
#include <cstring>
using namespace std;
#define  AS(arr)  (sizeof(arr)/sizeof(arr[0]))
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
		int k;
		string S;

		cin >> k >> S;

		vector<int> perm;
		REP(i, k)
		{
			perm.push_back(i);
		}
		int size = S.length();
		int minLen = INT_MAX;
		
		do
		{
			int comp = 0;
			char prev = '\0';
			for(int j = 0; j < size; j+=k )
			{
				REP(m, k)
				{
					char c = S[j+perm[m]];
					if(c != prev)
					{
						comp++;
						prev = c; 
					}
				}
			}
				

			minLen = min(minLen, comp);
			

		} while (next_permutation(ALL(perm)));





		cout << "Case #" << testcase+1 << ": " << minLen << endl;
		fflush(NULL);
	}
	return 0;
}




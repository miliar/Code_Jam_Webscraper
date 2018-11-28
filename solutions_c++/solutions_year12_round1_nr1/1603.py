#define _CRT_SECURE_NO_WARNINGS
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
#include <bitset>
#include <iomanip>
using namespace std;
#define  AS(arr)  (sizeof(arr)/sizeof(arr[0]))
#define ALL(c) (c).begin(),(c).end() 
#define SIZE(a) int((a).size())
#define EACH(it,c) for(__typeof((c).begin()) it=(c).begin();it!=(c).end();++it)
#define REP(i,n) for(int i=0;i<(int)n;++i)
typedef vector<int> VI;
typedef vector<string> VS;
typedef long long LL;

int A;
int B;
double C[100000];

int main()
{
	int testcases;
	cin >> testcases;

	REP(testcase, testcases)
	{
		double ret = 0;
		cin >> A >> B;
		
		REP(i, A)
		{
			cin >> C[i];
		}

		//1
		double per = 1;
		REP(i, A)
		{
			per *= C[i];
		}
		int diff = B - A;
		double a1 = per * (diff + 1) + (1 - per) * (diff + B + 2); 

//		cerr << a1 << endl;


		//2
		per = 1;
		double a2 = 9999999999L;
		for(int bs = 1; bs <= A; bs++)
		{
			for(int i=0; i < A - bs; i++)
			{
				per *= C[i];
			}
			/*
				for(int i = A - bs; i<B; i++)
			{
				per *= C[i];
			}
			*/
			int diff = B - A;

			//cerr << diff + bs * 2 + 1 << endl;
			//cerr << (diff + bs * 2 + B + 2) << endl;


			double v = per * (diff + bs * 2 + 1);
			v += (1 - per) * (diff + bs * 2 + B + 2);

			a2 = min(a2, v);

		}

		//3
		double a3 = 2 + B;

		ret = min(a1, a2);
		ret = min(ret, a3);




		
		cout.setf(ios::showpoint);
		
		cout << "Case #" << testcase+1 << ": ";
		printf("%.6f\n", ret);
		
	}
	return 0;
}

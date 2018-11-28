//Sun May 23 03:59:58 CDT 2010
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
	for(int ncase=1; ncase<=T; ncase++)
	{
		int N;
		cin >> N;
		vector<int> A;
		vector<int> B;
		for(int i=0; i<N; i++)
		{
			int number1, number2;
			cin >> number1 >> number2;
			A.push_back(number1);
			B.push_back(number2);
		}
		int count = 0;
		for(int i=0; i<N; i++)
		{
			for(int j=0; j<N; j++)
			{
				if((A[i]>A[j]&&B[i]<B[j]) || (A[i]<A[j]&&B[i]>B[j]))
				{
					count++;
				}
			}
		}
		cout << "Case #" << ncase << ": ";
		cout << count/2 << endl;
	}
	fclose(stdin);
	fclose(stdout);
	return 0;
}

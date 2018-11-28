#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
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
	int num;
	cin >> num;
	for(int casenum=0;casenum<num;casenum++)
	{
		int count;
		cin >> count;
		vector<int> x(count),y(count);
		for(int i=0;i<count;i++)
		{
			cin >> x[i];
		}
		for(int i=0;i<count;i++)
		{
			cin >> y[i];
		}
		sort(x.begin(),x.end());
		sort(y.begin(),y.end(),greater<int>());

		int retval=0;
		for(int i=0;i<count;i++)
		{
			retval += (x[i]*y[i]);
		}


		cout << "Case #" << casenum+1 << ": " << retval << endl;
	}
	return 0;
}

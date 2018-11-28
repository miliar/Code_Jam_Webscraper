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
const int maxs = 10006;

int n,low,high;
int num[maxs];

void getAC()
{
	bool suc = false;
	int res ;
	for (int i=low;i<=high;i++)
	{
		bool flag = true;
		for (int j=0;j<n;j++)
		{
			if (num[j]==0 || i%num[j]==0 || num[j]%i==0)
			{
				
			}
			else {flag = false ;break;}
		}
		if (flag)
		{
			suc = true;res = i;break;
		}
	}
	if (!suc)
	{
		cout << "NO" << endl;
	}
	else cout << res << endl;
}
int main()
{
	freopen("C-small-attempt0.in","r",stdin);
	freopen("C-small-attempt0.out","w",stdout);
	int testcases;
	cin >> testcases;
	for (int caseid=1;caseid<=testcases;caseid++)
	{	
		cin >> n >> low >> high;
		for (int i=0;i<n;i++)
		{
			cin >> num[i];
		}
		cout << "Case #"<<caseid<<": " ;
		getAC();
	}
	return 0;
}
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
#include <cmath>
#include <ctime>
using namespace std;

long long ans = 0;
string digit;
string str;
int dsz;
void CalAns(int pos)
{
	if (pos == dsz)
	{
		long long sum = 0;
		long long tmp = 0;
		int op = 1;
		for (int i = 0; i < str.size(); ++i)
		{
			if (str[i] == '+')
			{
				sum += op*tmp;
				tmp = 0;
				op = 1;
			}
			else if ( str[i] == '-')
			{
				sum += op*tmp;
				tmp = 0;
				op = -1;
			}
			else
			{
				tmp = tmp * 10 + str[i] - '0';
			}
		}
		sum += op*tmp;
		if (sum < 0)
		{
			sum = -sum;
		}
		if (sum%2 == 0 || sum%3 == 0 || sum%5 == 0 || sum%7 == 0 )
		{
			++ans;
		}
	}
	else
	{
		string tmp = str;
		str += digit[pos];
		CalAns(pos + 1);
		str = tmp;

		str += '+';
		str += digit[pos];
		CalAns(pos + 1);
		str = tmp;

		str += '-';
		str += digit[pos];;
		CalAns(pos + 1);
		str = tmp;
	}
	
}
int main()
{
	int n;
	cin>>n;
	for (int i = 0; i < n; ++i)
	{
		cin>>digit;
		ans = 0;
		str.clear();
		dsz = digit.size();
		str += digit[0];
		CalAns(1);
		cout<<"Case #"<<i+1<<": "<<ans<<endl;
	}
	return 0;
}
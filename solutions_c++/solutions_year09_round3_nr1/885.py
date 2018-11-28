#include <iostream>
#include <vector>
#include <map>
#include <set>
#include <sstream>
#include <algorithm>
#include <cmath>
using namespace std;
typedef unsigned long long ull;

void normalize(string & num)
{
	int i,j,k,cur,last;
	int sz = num.size();
	int set = 0;
	vector<bool> flags(sz);
	map<int,int> reps;
	for (i=0,cur=0,last=1;i<sz;++i)
	{
		if (!reps[num[i]] && !flags[i])
		{
			reps[num[i]] = last;
			char ch  = num[i];
			num[i]=last;
			flags[i] = 1;
			for (j=i+1;j<sz;++j)
			{
				if (num[j] == ch)
				{
					num[j] = last;
					flags[j] = 1;
				}
			}
			if (last == 1)
				last = 0;
			else if (last == 0)
				last = 2;
			else
				++last;
		}
	}
	
	// for (i=0;i<sz;++i)
		// num[i]+=48;
		
	// cout << num << endl;
	// for (i=0;i<sz;++i)
		// num[i]-=48;
	
		
}

ull findmin(string num)
{
	int sz = num.size();
	int base = *max_element(num.begin(), num.begin()+sz) +1;\
	reverse(num.begin(), num.end());
	int i;
	ull res = 0;
	for (i=0;i<sz;++i)
	{
		res += (ull)num[i] * (ull)pow((double)base, i);
	}
	
	
	
	return res;
}

int main()
{
	int t;
	int i,j,k;
	ull res;
	string num;
	
	cin >> t;
	
	for (i=1;i<=t;++i)
	{
		cin >> num;
		normalize(num);
		res = findmin(num);
	
		cout << "Case #" << i << ": " << res << endl;
	}
	
	

}
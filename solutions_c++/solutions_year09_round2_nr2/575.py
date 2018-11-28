#include <fstream>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <string>
#include <algorithm>
#include <functional>
#include <queue>
#include <stack>
#include <ctime>
#include <cmath>
#include <vector>
#include <list>
#include <map>
#include <set>
#include <bitset>
#include <cassert>
#include <stack>
#include <limits>
#include <cstring>
using namespace std;


int main()
{
	int cas;
	cin>>cas;
	for(int i = 1; i <= cas; i++)
	{
		string s;
		cin>>s;
		s = '0' + s;
		int small;
		char ts[100];
		int j;
		for(j = 0; j< s.size(); j++)
		{
			ts[j] = s[j];
		}
		int t1, t2;
		int p = -1;
		for(j = 0; j < s.size(); j++)
		{
			for(small = j+1; small < s.size(); small++)
			{
				if(ts[j] < ts[small])
				{
					if(j > p)
					{
						p = j;
						t1 = j;
						t2 = small;
					}
					else if(j == p)
					{
						if(ts[small] < ts[t2])
						{
							t2 = small;
						}
					}
				}
			}
		}
		j = t1;
		small = t2;
		char t;
		t = ts[small];
		ts[small] = ts[j];
		ts[j] = t;
		sort(ts+j+1, ts+s.size());
		if(ts[0] == '0')
			j = 1;
		else
			j = 0;
		cout<<"Case #"<<i<<": ";
		for(; j < s.size(); j++)
			cout<<ts[j];
		cout<<endl;
	}
	return 0;
}
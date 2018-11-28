#include <vector>
#include <string>
#include <list>
#include <map>
#include <set>
#include <utility>
#include <cmath>
#include <algorithm>
#include <sstream>
#include <queue>
#include<iostream>
#define FALSE 0
#define TRUE 1
using namespace std;
typedef long long ll;
typedef pair<int,int> ipair;
#define SIZEARRAY(x) (sizeof(x)/sizeof(x[0]))

template <typename T>
string ToString(T var)
{
	ostringstream os;
	os << var;
	return os.str();
}

ll memory[10005][10005];
ll solve(int be,int en);
vector<int> poser;
int main()
{
	freopen("F:\\code\\topcoder\\compete\\compete\\C-small-attempt1.in","r",stdin);
	freopen("F:\\code\\topcoder\\compete\\compete\\test2.out","w",stdout);
	int testCase;
	cin >> testCase;
	for (int caseNum = 1;caseNum<=testCase;caseNum++)
	{
		int p,q;
		poser.clear();
		cin >> p >> q;
		memset(memory,-1,sizeof(memory));
		int qaddr;
		for (int i = 0;i<q;i++)
		{
			cin >> qaddr;
			poser.push_back(qaddr);
		}
		ll res;
		res = solve(1,p); 
		cout << "Case #"+ToString(caseNum)+": "+ToString(res)<<endl;
	}
}

ll solve(int be,int en)
{
	if(be>=en)
	{
		return 0;
	}
	if(memory[be][en] != -1)
	{
		return memory[be][en];
	}
	ll res = memory[be][en];
	ll tempRes = 0;
	
	for (int i = 0;i<poser.size();i++)
	{
		if(poser[i]>=be&&poser[i]<=en)
		{
			tempRes = solve(be,poser[i]-1)+solve(poser[i]+1,en);
			if(res == -1 || tempRes<res)
			{
				res = tempRes;
			}
		}
	}
	if(res == -1)
	{
		res = 0;
	}
	else
	{
		res+=en-be;
	}
	memory[be][en] = res;
	return res;
}

#include <iostream>
#include <algorithm>
#include <cmath>
#include <vector>
#include <queue>
#include <map>

using namespace std;

#define FOR(i,a,b) for(int i = a ; i <= b; i++)
#define REP(i,a) for(int i = 0; i < a; i++)

struct node
{
	int index;
	int cost;
	public:
		node(int i, int c)
	{
		index = i;
		cost = c;
	}

	friend bool operator < (node a,node b)
	{
		if(a.cost != b.cost)
			return a.cost > b.cost;
		return a.index > b.index;
	}
};

long long convert(string num, int base)
{
	int mule = 1;
	long long ret = 0;
	for(int i = num.length()-1; i >= 0; i--)
	{
		ret += (num[i]-'0')*mule;
		mule *=base;
	}
	return ret;
}

int main()
{
	int t;
	cin >> t;
	FOR(tt,1,t)
	{
		cout << "Case #" << tt << ": ";
		string x;
		cin >> x;
		bool used[1000];
		memset(used,false,sizeof(used));
		int base = 0;
		REP(i,x.length())
		{
			if(!used[x[i]])
			{
				used[x[i]] = true;
				base++;
			}
		}
		map<char,int> m;
		char c = '0';
		m[x[0]] = '1';
		x[0] = '1';
		FOR(i,1,x.length()-1)
		{
			if(!m[x[i]])
			{
				if(c == '1') c++;
				m[x[i]] = c;
				x[i] = c++;
			}
			else
			{
				x[i] = m[x[i]];
			}
		}
		base = max(2,base);
		//cout << x << " " << base << endl;
		cout << convert(x,base) << endl;
	}
	return 0;
}

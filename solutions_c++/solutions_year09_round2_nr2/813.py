#include <iostream>
#include <algorithm>
#include <cmath>
#include <vector>
#include <queue>

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

int main()
{
	int t;
	cin >> t;
	FOR(tt,1,t)
	{
		cout << "Case #" << tt << ": ";
		string n;
		cin >> n;
		/*
		bool dapat = false;
		for(int i = n.length()-2; i >= 0; i--)
		{
			bool flag = false;
			char greater = 'a';
			int index = -1;
			FOR(j,i+1,n.length()-1)
			{
				if(n[j] > n[i])
				{
					flag = true;
					if(!flag)
					{
						greater = n[j];
						index = j;
					}
					else if(n[j] < greater)
					{
						greater = n[j];
						index = j;
					}
				}
			}
			if(flag)
			{
				char temp = n[i];
				n[i] = greater;
				n[index] = temp;
				sort(&n[i+1],&n[n.length()]);
				cout << n << endl;
				dapat = true;
				break;
			}
		}
		if(!dapat)
		{
			n += "0";
			sort(&n[0],&n[n.length()]);
			int r = 0;
			while(n[r] == '0')
			{
				r++;
			}
			cout << n[r] << n.substr(0,r) << n.substr(r+1,n.length()) << endl;
		}
		*/
		if(next_permutation(&n[0],&n[n.length()]))
		{
			cout << n << endl;
		}
		else
		{
			n += "0";
			sort(&n[0],&n[n.length()]);
			int r = 0;
			while(n[r] == '0')
			{
				r++;
			}
			cout << n[r] << n.substr(0,r) << n.substr(r+1,n.length()) << endl;
		}
	}
	return 0;
}

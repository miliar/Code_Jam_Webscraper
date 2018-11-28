#include <iostream>
#include <queue>
#include <memory.h>
#include <vector>
#include <string>
#include <map>
#include <set>
#include <algorithm>
using namespace std;

int dp[102][102][102];
int d[] = {-1,0,1};

struct Q
{
	int i,j,k;
	Q(int a,int b,int c):i(a),j(b),k(c){}
};

int main()
{
	freopen("B-large.in", "r", stdin);
	freopen("res.txt", "w", stdout);
	int t;
	cin >> t;
	for (int tc = 1; tc <= t; tc ++)
	{
		int c,d,n;
		cin>> c;
		map <pair<char,char>, char> ac;
		for (int i= 0 ; i < c; i ++)
		{
			char x,y,z;
			cin >> x >> y >> z;
			ac[make_pair(x,y)] = z;
			ac[make_pair(y,x)] = z;
		}
		set <pair<char,char> > dn;
		cin >> d;
		for (int i= 0 ; i < d; i ++)
		{
			char x,y;
			cin >> x >> y;
			dn.insert(make_pair(x,y));
			dn.insert(make_pair(y,x));
		}
		cin >> n;
		string q;
		cin >> q;
		
		string res;

		for (int i =0 ; i < n; i ++)
		{
			res += q[i];
			while (res.size() > 1)
			{
				pair<char, char> p (res[res.length()-2],res[res.length()-1]);
				if (ac.count(p))
				{
					res.pop_back();
					res.pop_back();
					res += ac[p];
				}
				else
					break;
			}
			for (int j = 0; j < (int)res.size()-1; j ++)
			{
				pair<char, char> p (res[j],res[res.length()-1]);
				if (dn.count(p))
					res.clear();
			}
		}


		cout << "Case #" << tc <<": ";
		cout << '[';
		for (int i = 0; i < res.size(); i ++)
		{
			cout << res[i];
			if (i+1 < res.size())
				cout << ", ";
		}
		cout << "]" << endl;
	}

	return 0;
}

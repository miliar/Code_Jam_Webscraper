#include <algorithm>
#include <iostream>
#include <fstream> 
#include <iterator>
#include <vector>
#include <string>
#include <queue>
#include <map>
#include <set>

using namespace std;

typedef vector<int> vi ; 
typedef vector<string> vs ; 
typedef vector<double> vd ; 
#define PB push_back
#define big __int64
#define For(i,n) for (i = 0 ; i < n ; i ++)
#define bend(v) v.begin (), v.end ()
vs split (string s, string delim = " ") {vs res; string t; unsigned int i ; For (i, s.size ()) {if (delim.find (s [i]) != string::npos) {if (! t.empty ()) {res.PB (t); t = "" ;}} else {t += s [i] ; }} if (! t.empty ()) {res.PB (t) ;} return res ;}

class Customer
{
public:
	int flavors[10]; // 0 = don't want, 1 = want unmalted, 2 = want malted
	Customer()
	{
		memset(flavors, 0, sizeof(flavors));
	}
};

bool possible(int mask, vector<Customer> customers, int N)
{
	bool served[101];
	memset(served, false, sizeof(served));
	for (int i = 0; i < N; i++)
	{
		if (((mask >> i) & 1)== 1)
		{
			// Malted
			for (int j = 0; j < customers.size(); j++)
			{
				if (customers[j].flavors[i] == 2)
					served[j] = true;
			}
		}
		else
		{
			for (int j = 0; j < customers.size(); j++)
			{
				if (customers[j].flavors[i] == 1)
					served[j] = true;
			}
		}
	}
	for (int i = 0; i < customers.size(); i++)
		if (! served[i])
			return false;
	return true;
}

int ones(int mask, int N)
{
	int ret = 0;
	for (int i = 0; i < N; i++)
	{
		if (((mask >> i) & 1)== 1)
		{
			ret ++;
		}
	}
	return ret;
}

void display(int mask, int N)
{
	for (int i = 0; i < N; i++)
	{
		if (i != 0)
			cout << " ";
		cout << ((mask >> i) & 1);
	}
}

int main()
{
	freopen("B-small-attempt0(2).in","rt",stdin);
	freopen("result.out","wt",stdout);

	int testno;
	cin >> testno;

	for (int tno = 0; tno < testno; tno++)
	{
		int N;
		cin >> N;

		int M;
		cin >> M;

		vector<Customer> customers;

		for (int i = 0; i < M; i++)
		{
			int T;
			cin >> T;

			Customer c;
			
			for (int j = 0; j < T; j++)
			{
				int X, Y;
				cin >> X >> Y;

				c.flavors[X - 1] = Y == 0 ? 1 : 2;
			}

			customers.push_back(c);
		}

		int minOnes = 100000, fmask = -1;
		for (int mask = 0; mask < (1 << N); mask++)
		{
			if (possible(mask, customers, N))
			{
				int onec = ones(mask, N);
				if (onec < minOnes)
				{
					minOnes = onec;
					fmask = mask;
				}
			}
		}

		cout << "Case #" << tno + 1 << ": ";
		if (minOnes == 100000)
			cout << "IMPOSSIBLE";
		else
			display(fmask, N);
		cout << endl;
	}
	
	return 0;
}
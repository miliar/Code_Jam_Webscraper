#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

void addone(vector<bool> &v)
{
	for (unsigned int i=0; i<v.size(); ++i)
	{
		if (v[i])
		{
			v[i]=false;
		}
		else
		{
			v[i]=true;
			return;
		}
	}
}

int add(const vector<int> &v, const vector<bool> &b, bool bo)
{
	int sum=0;
	for (unsigned int i=0; i<v.size(); ++i)
	{
		if (b[i]==bo)
			sum+=v[i];
	}
	return sum;
}

int badadd(const vector<int> &v, const vector<bool> &b, bool bo)
{
	int sum=0;
	for (unsigned int i=0; i<v.size(); ++i)
	{
		if (b[i]==bo)
			sum^=v[i];
	}
	return sum;
}

int main()
{
	int n;
	cin >> n;
	for (int casenum=1; casenum<=n; ++casenum)
	{
		int j;
		cin >> j;
		vector<int> vals;
		while (j--)
		{
			int v;
			cin >> v;
			vals.push_back(v);
		}
		vector<bool> steals(vals.size(),false);
		addone(steals);
		int best=-1;
		while (!steals[steals.size()-1])
		{
			if (badadd(vals, steals, true)==badadd(vals, steals, false))
			{
				best=max(best,max(add(vals, steals, true),add(vals, steals, false)));
			}
			addone(steals);
		}
		cout << "Case #" << casenum << ": ";
		if (best==-1)
			cout << "NO";
		else
			cout << best;
		cout << endl;
	}
}

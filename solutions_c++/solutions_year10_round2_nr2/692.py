#include <iostream>
#include <vector>
#include <cstdio>
using namespace std;

struct T 
{
	double x;
	double v;
	bool valid;
};

int main()
{
	int i, j, k, c, t, b, n;
	int res, cnt, perskok;
	vector<T> data;
	double path, tim;
	freopen("in.txt", "r", stdin);
	freopen("out.txt", "w", stdout);
	cin>> c;

	for(i=1; i<=c; ++i)
	{
		cin >>n >>k >>b >>t;
		data.resize(n);
		for(j=0; j<n; ++j)
			cin >> data[j].x;
		for(j=0; j<n; ++j)
			cin >> data[j].v;
		
		for(j=0; j<n; ++j)
		{
			path= b-data[j].x;
			tim= path/data[j].v;
			data[j].valid= tim<=t;
		}
		res= 0;
		cnt= 0;
		perskok= 0;
		for(j=n-1; j>=0; --j)
		{
			if (cnt==k)
				break;
			if (data[j].valid)
			{
				cnt++;
				res+= perskok;
			}
			else
			{
				perskok++;
			}
		}
		cout << "Case #" <<i <<": ";
		if (cnt==k)
			cout <<res <<endl;
		else
			cout <<"IMPOSSIBLE" <<endl;
	}
	return 0;
}

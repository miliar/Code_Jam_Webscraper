#include <stdio.h>
#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

bool cmp(const long long &a, const long long &b)
{
	return a>b;
}

int main(int argc, char *argv[])
{
	int n;
	int p;
	int k;
	int l;
	long long ret;
	vector<long long> value;
	freopen("a.in","r",stdin);
	freopen("a.out","w",stdout);
	cin>>n;
	for (int i=0; i<n; i++)
	{
		value.clear();
		cin >> p;
		cin >> k;
		cin >> l;
		ret = 0;
		int w = -1;
		for (int j=0; j<l; j++)
		{
			long long v;
			cin>>v;
			value.push_back(v);
		}
		sort(value.begin(), value.end(), cmp);
		long long press;
		for (press = 1; press <= p; press++)
		{
			for (int place = 1; place <=k; place++)
			{
				w++;
				if (w == l)
					goto out;
				ret = ret + press * value[w];
			}
		}
		out:
		cout << "Case #"<<i+1<<": "<<ret<<endl;
	}	
	return 0;
}

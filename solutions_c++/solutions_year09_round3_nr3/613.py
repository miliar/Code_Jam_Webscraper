#include <iostream>
#include <vector>
#include <map>
#include <set>
#include <sstream>
#include <algorithm>
#include <cmath>
using namespace std;
typedef unsigned long long ull;

void sortprs(vector<int> & prs)
{
	int sz = prs.size();
	sort(prs.begin(), prs.begin()+sz);
}

ull getbribe(vector<int> prs, int count)
{
	ull b = 0;
	int sz = prs.size();
	
	
	
	do
	{
		vector<bool> isin(count, 1);
		int i;
		ull curb=0;
		for (i=0; i<sz; ++i)
		{
			int x;
			int cur = prs[i]-1;
			//cout << cur << endl;
			isin[cur] = 0;
			for (x=cur-1;isin[x]&&x>=0;--x)
			{
				++curb;
				//cout <<"n";
			}
			for (x=cur+1;isin[x]&&x<count;++x)
			{
				++curb;
				//cout << "p";
			}
		}
		
		if (b == 0 || curb < b)
			b = curb;
			
		//cout << curb << " " << b << "." << endl;
			
		
	} 
	while (next_permutation(prs.begin(), prs.begin()+sz));
	
	return b;

}

int main()
{
	int t;
	int i,j,k;
	ull res;
	string num;
	int p,q;
	int pr;
	vector<int> prs;
	
	cin >> t;
	
	for (i=1;i<=t;++i)
	{
		cin >> p >> q;
		prs.clear();
		for(j=0;j<q;++j)
		{
			cin >> pr;
			prs.push_back(pr);
		}
		sortprs(prs);
		res = getbribe(prs, p);
		cout << "Case #" << i << ": " << res << endl;
	}
	
	

}
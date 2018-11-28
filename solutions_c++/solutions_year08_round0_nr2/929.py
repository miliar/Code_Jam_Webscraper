#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>

using namespace std;
vector<int> ADept;
vector<int> AAri;
vector<int> BDept;
vector<int> BAri;
int T;

int func(vector<int> Dv, vector<int> Av)
{
	list<int> D(Dv.begin(), Dv.end());
	list<int> A(Av.begin(), Av.end());

	list<int>::iterator x = D.begin();
	list<int>::iterator y = A.begin();
	while(x != D.end() && y != A.end())
	{
		if ( *x >= (*y+T) )
		{
			list<int>::iterator z = x;
			x++;
			D.erase(z);
			y++;
		}
		else {
			x++;
		}
	}
	return D.size();
}

int main()
{
	freopen("t.txt", "w", stdout);
	int cases = 0;
	cin>>cases;
	for(int k=0;k<cases;k++)
	{
		AAri.clear();
		BAri.clear();
		ADept.clear();
		BDept.clear();
		cin>>T;
		int na,nb;
		cin>>na>>nb;
		char t[10];
		for(int l=0;l<na;l++)
		{
			cin>>t;
			int a = ((t[0]-'0')*10+(t[1]-'0'))*60 +
					((t[3]-'0')*10+(t[4]-'0'));
			ADept.push_back(a);
			cin>>t;
			a = ((t[0]-'0')*10+(t[1]-'0'))*60 +
				((t[3]-'0')*10+(t[4]-'0'));
			BAri.push_back(a);
		}
		for(int l=0;l<nb;l++)
		{
			cin>>t;
			int a = ((t[0]-'0')*10+(t[1]-'0'))*60 +
					((t[3]-'0')*10+(t[4]-'0'));
			BDept.push_back(a);
			cin>>t;
			a = ((t[0]-'0')*10+(t[1]-'0'))*60 +
				((t[3]-'0')*10+(t[4]-'0'));
			AAri.push_back(a);
		}
		sort(AAri.begin(),AAri.end());
		sort(BAri.begin(),BAri.end());
		sort(ADept.begin(),ADept.end());
		sort(BDept.begin(),BDept.end());
		cout<<"Case #"<<k+1<<": "<<func(ADept, AAri)<<" "<<func(BDept, BAri)<<endl;
	}
	return 0;
}

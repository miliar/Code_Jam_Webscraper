#include <algorithm>
#include <bitset>
#include <cctype>
#include <cmath>
#include <cmath>
#include <cstdio>
#include <cstdio>
#include <cstdlib>
#include <cstdlib>
#include <cstring>
#include <deque>
#include <functional>
#include <iomanip>
#include <iostream>
#include <list>
#include <map>
#include <numeric>
#include <queue>
#include <set>
#include <sstream>
#include <stack>
#include <string>
#include <utility>
#include <vector>

#define sz(X) ((int)(X.size()))
#define ln(X) ((int)(X.length()))
#define pb push_back 
#define all(c) (c).begin(),(c).end() 
#define tr(c,i) for(typeof((c).begin()) i = (c).begin(); i != (c).end(); i++) 
#define rep(i,s,n) for(int i=s; i<n; i++)
#define rrep(i,s,n) for(int i=n-1; i>=s; i--)
#define present(c,x) ((c).find(x) != (c).end()) 
#define cpresent(c,x) (find(all(c),x) != (c).end())
#define err 1E-15

using namespace std;

struct Time
{
	int h, m;
	Time(int h,int m) : h(h), m(m) {}
	bool operator <(const Time& rhs) const
	{
		if(h != rhs.h) return h < rhs.h;
		return m < rhs.m;
	}
	bool operator <= (const Time& rhs) const
	{
		if(*this < rhs) return true;
		if(h == rhs.h && m == rhs.m) return true;
		return false;
	}
	void add(int mins)
	{
		m += mins;
		if(m >= 60)
		{
			m -= 60;
			h++;
		}		
	}
};

int calc(vector<Time> &arr, vector<Time> &dept)
{
	sort(all(arr));
	sort(all(dept));
	int ret = 0;
	int i,j;
	for(i = 0,j = 0; i < sz(arr) && j < sz(dept);)
	{
		if(arr[i] <= dept[j])
		{
			i++;
			j++;
		}
		else
		{
			ret++;
			j++;
		}
	}
	for(;j < sz(dept); j++)
		ret++;
	return ret;	
}

int main()
{
	int runs;
	cin>>runs;
	for(int k = 1; k <= runs; k++)
	{
		vector<Time> adept, aarr, bdept, barr;
		int h,m;
		int t,na,nb;
		cin>>t>>na>>nb;
		char d;
		for(int i = 0; i < na; i++)
		{
			cin>>h>>d>>m;
			adept.pb(Time(h,m));
			cin>>h>>d>>m;
			barr.pb(Time(h,m));
			barr[i].add(t);
		}
		for(int i = 0; i < nb; i++)
		{
			cin>>h>>d>>m;
			bdept.pb(Time(h,m));
			cin>>h>>d>>m;
			aarr.pb(Time(h,m));
			aarr[i].add(t);
		}
		cout<<"Case #"<<k<<": "<<calc(aarr,adept)<<" "<<calc(barr,bdept)<<endl;
	}
	return 0;
		
		
}

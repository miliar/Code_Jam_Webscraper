#include <iostream> 
#include <string>
#include <vector>
#include <sstream>
#include <queue>
#include <algorithm>
#include <iomanip>
#include <map>
#include <set>
#include <math.h>
#include <stack>
#include <deque>
#include <numeric>
using namespace std;
typedef long long ll;
typedef long double ld;
const ld epsylon = 1e-9;
int to_mins(string u)
{
	int hrs = 0;
	hrs += (u[0]-'0')*10 + (u[1]-'0');
	int res = 0;
	res = hrs*60 + (u[3]-'0')*10 + (u[4]-'0');
	return res;
}

int main()
{
	freopen("B-large.in","r",stdin);
	freopen("B-large.out","w",stdout);
	int nt;
	cin>>nt;
	for(int it=0;it<nt;it++)
	{
		int t;
		cin>>t;
		int n,m;
		cin>>n>>m;
		vector<pair<int,int> > a(n),b(m);
		string dep,arr;
		for (int i = 0; i < n; i++)
		{
			cin>>dep>>arr;
			a[i].first = to_mins(dep);
			a[i].second = to_mins(arr) + t;
		}
		for (int i = 0; i < m; i++)
		{
			cin>>dep>>arr;
			b[i].first = to_mins(dep);
			b[i].second = to_mins(arr) + t;
		}
		int a_cnt = 140,a_end  = -1;
		vector<int> mov_a(n);
		for(int i=0;i<n;i++)
		{
			mov_a[i] = 0;
			for(int j = 0;j<m;j++)
				if(b[j].second <= a[i].first)
					mov_a[i]++;
			for(int j =0 ; j<n;j++)
				if(a[j].first < a[i].first || (a[j].first == a[i].first && j < i))
					mov_a[i]--;
		}
		vector<int> mov_b(m);
		for(int i=0;i<m;i++)
		{
			mov_b[i] = 0;
			for(int j = 0;j<n;j++)
				if(a[j].second <= b[i].first)
					mov_b[i]++;
			for(int j =0 ; j<m;j++)
				if(b[j].first < b[i].first || (b[j].first == b[i].first && j < i))
					mov_b[i]--;
		}
		int min_a = 10200;
		for(int i=0;i<n;i++)
			if(mov_a[i] < min_a)
				min_a = mov_a[i];
		a_cnt = max(0,-min_a + 1);
		int min_b = 10200;
		for(int i=0;i<m;i++)
			if(mov_b[i] < min_b)
				min_b = mov_b[i];
		int b_cnt;
		b_cnt = max(0 , -min_b +1);
		cout<<"Case #"<<it+1<<": "<<a_cnt<<" "<<b_cnt<<endl;
	}
	return 0;
}

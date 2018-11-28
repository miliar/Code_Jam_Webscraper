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
vector<int> a;
int s;
int mem[128][1024];
int solve(int num,int idx)
{
	if(idx == a.size())
	{
		mem[num][idx] = 0;
		return 0;
	}
	int bst = -1;
	int cur;
	for(int i=0;i<s;i++)
	{
		if(a[idx] == i)
			continue;
		if(mem[i][idx+1] == -1)
			cur = solve(i,idx+1);
		else
			cur = mem[i][idx+1];
		if(i != num)
			cur++;
		if(cur < bst || bst < 0)
			bst = cur;
	}
	mem[num][idx] = bst;
	return mem[num][idx];
}
int main()
{
	freopen("A-large.in","r",stdin);
	freopen("A-large.out","w",stdout);
	int nt;
	cin>> nt;
	for(int it=1;it<=nt;it++)
	{
		cin>>s;
		map<string,int> names;
		string tmp;
		cin.get();
		for(int i =0;i<s;i++)
		{
			getline(cin,tmp);
			names.insert(make_pair(tmp,i));
		}
		int q;
		cin>>q;
		vector<int> y;
		cin.get();
		for(int i=0;i<q;i++)
		{
			getline(cin,tmp);
			y.push_back(names[tmp]);
		}
		a = y;
		for (int i = 0; i < 128; i++)
		{
			for (int j = 0; j < 1024; j++)
			{
				mem[i][j] = -1;
			}
		}
		int ans = -1;
		int cur;
		for(int i=0;i<s;i++)
		{
			cur = solve(i,0);
			if(cur < ans || ans < 0)
				ans = cur;
		}
		cout<<"Case #"<<it<<": "<<ans<<endl;
	}
	return 0;
}

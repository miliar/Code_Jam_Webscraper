
#define _CRT_SECURE_NO_DEPRECATE
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
#define all(x) x.begin(),x.end()
#define mpair make_pair
using namespace std;
typedef unsigned long long ll;
typedef long double ld;
const ld epsylon = 1e-9;
vector<char> get_digs(string s)
{
	vector<char> res(s.size());
	for(int i = 0;i<s.size();i++)
		res[i] = s[i];
	return res;
}
string get_res(vector<char> o)
{
	string res;
	for(int i=0;i<o.size();i++)
		res+=o[i];
	return res;
}
ll number;
int main()
{
	freopen("B-large.in","r",stdin);
	freopen("B-large.out","w",stdout);
	int nt;
	cin>>nt;
	for(int it=1;it<=nt;it++)
	{
		string u;
		cin>>u;
		vector<char> digs;
		digs = get_digs(u);
		string qna;
		if(next_permutation(all(digs)))
		{
			qna = get_res(digs);
		}
		else{
			reverse(all(digs));
			int mi = 0;
			for(int i=0;i<digs.size();i++)
			{
				if(digs[i] != '0' && digs[i] < digs[mi])
				{
					mi = i;
				}
			}
			swap(digs[0],digs[mi]);
			digs.push_back('0');
			sort(digs.begin()+1,digs.end());
			qna = get_res(digs);
		}
		cout<<"Case #"<<it<<": "<<qna<<endl;
	}
	return 0;
}

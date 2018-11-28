#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <queue>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <fstream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>

using namespace std;
string c(string s, vector<int> v)
{
	int i, j, n=s.size();
	string res=s;
	for (j=0;j<n/v.size();j++)
		for (i=0;i<v.size();i++)
			res[j*v.size()+i]=s[j*v.size()+v[i]];
	return res;
}
int calc(string s)
{
	int i, res=1, n=s.size();
	for (i=1;i<n;i++)
		if (s[i]!=s[i-1])
			res++;
	return res;
}
int main()
{
	ifstream fin("a.in");
	ofstream fout("a.out");
	int res, i, j, n, k, l, m, t, T;
	fin>>T;
	string s;
	for (t=1;t<=T;t++)
	{
		res=1e9;
		fin>>k;
		fin>>s;
		n=s.size();
		vector<int> v;
		for (i=0;i<k;i++)
			v.push_back(i);
		do{
			string ss=c(s,v);
			res=min(res, calc(ss));
		}while(next_permutation(v.begin(),v.end()));
		fout<<"Case #"<<t<<": "<<res<<endl;
	}
	fin.close();
	fout.close();
	return 0;
}
#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <fstream>
#include <fstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <complex>
using namespace std;


string s[10000];
int a[40][50];
vector<string> v;
int main()
{
	int i, j, k, n, m, l, d, res;
	string h, p;
	ifstream fin("a.in");
	ofstream fout("a.out");
	fin>>l>>d>>n;
	for (i=0;i<d;i++)
		fin>>s[i];
	for (k=1;k<=n;k++)
	{
		memset(a,0,sizeof(a));
		fin>>h;
		v.clear();
		p="";
		m=0;
		for (i=0;i<h.size();i++)
		{
			if (h[i]=='(')
				m=1;
			if (h[i]==')')
			{
				m=0;
				v.push_back(p);
				p="";
			}
			if (h[i]>='a' && h[i]<='z')
			{
				p+=h[i];
				if (m==0)
				{
					v.push_back(p);
					p="";
				}
			}
		}		
		m=0;
		for (j=0;j<v.size();j++)
		{
			p=v[j];
			for (i=0;i<p.size();i++)
				a[p[i]-'a'][m]=1;
			m++;
		}
		res=0;
		for (i=0;i<d;i++)
		{
			m=1;
			for (j=0;j<s[i].size();j++)
				if (a[s[i][j]-'a'][j]==0)
				{
					m=0;
					break;
				}
			if (m)
				res++;
		}
		fout<<"Case #"<<k<<": "<<res<<endl;
	}
	fin.close();
	fout.close();
	return 0;
}

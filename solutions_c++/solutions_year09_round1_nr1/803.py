#include "stdafx.h"
#include <vector>
#include <string>
#include <set>
#include <iostream>
#include <map>
#include <algorithm>
#include <sstream>
using namespace std;

typedef vector<int> lnum;
const int NMAX=100000;

lnum mult(const lnum &a,const lnum &b,int base)
{
	lnum c (a.size()+b.size());
for (size_t i=0; i<a.size(); ++i)
	for (int j=0, carry=0; j<(int)b.size() || carry; ++j) {
		long long cur = c[i+j] + a[i] * 1ll * (j < (int)b.size() ? b[j] : 0) + carry;
		c[i+j] = int (cur % base);
		carry = int (cur / base);
	}
while (c.size() > 1 && c.back() == 0)
	c.pop_back();
return c;
}

void add(lnum &a,const lnum &b,int base)
{
	int carry = 0;
for (size_t i=0; i<max(a.size(),b.size()) || carry; ++i) {
	if (i == a.size())
		a.push_back (0);
	a[i] += carry + (i < b.size() ? b[i] : 0);
	carry = a[i] >= base;
	if (carry)  a[i] -= base;
}
}

bool used[NMAX];

bool good(lnum a,int base)
{
	if ( (a.size()==1) && (a[0]==1) )
		return 1;
	int dec=0;
	for(int i=a.size()-1;i>=0;i--)
		dec=dec*base+a[i];
	if (used[dec])
		return 0;
	used[dec]=1;
	lnum next,cur;
	for(int i=0;i<a.size();i++)
	{
		int z=a[i]*a[i];
		cur.clear();
		cur.push_back(z%base);
		if (z/base>0)
			cur.push_back(z/base);
		add(next,cur,base);
	}
	if (a==next)
		return 0;
	return good(next,base);
}

lnum tob(int a,int base)
{
	lnum res;
	while (a)
	{
		res.push_back(a%base);
		a/=base;
	}
	return res;
}

int main(){

	freopen("As.in","rt",stdin);
	freopen("A.out","wt",stdout);
	
	int T;
	scanf("%d\n",&T);
	for(int i=0;i<T;i++)
	{
		vector<int> bases;
		string X;
		getline(cin,X);
		istringstream xx(X);
		int a;
		while (xx>>a)
		{
			bases.push_back(a);
		}
		int ans=1;
		vector<lnum> gg(11);
		for(int j=0;j<bases.size();j++)
			gg[bases[j]]=tob(1,bases[j]);
		vector<int> uno;
		uno.push_back(1);
		while (1)
		{			
			ans++;
			for(int j=0;j<bases.size();j++)
				add(gg[bases[j]],uno,bases[j]);
			bool yes=1;
			for(int j=0;j<bases.size();j++)
			{
				memset(used,0,sizeof(used));
				if (!good(gg[bases[j]],bases[j]))
				{
					yes=0;
					break;
				}
			}
			if (yes)
			{
				printf("Case #%d: %d\n",i+1,ans);
				break;
			}
		}
	}
	
	return 0;
}
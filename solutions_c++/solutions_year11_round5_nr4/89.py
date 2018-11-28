#include <iostream>
#include <algorithm>
#include <cstdio>
#include <cmath>
#include <cstring>
#include <string>
#include <vector>
#include <utility>
#include <set>
#include <sstream>
#include <map>
#include <ctime>
#include <cstdlib>
#define fr(a,b,c) for (a=b;a<=c;a++)
#define frr(a,b,c) for (a=b;a>=c;a--)
#define pb push_back
#define mp make_pair
#define pii pair<int,int>
#define F first
#define S second
#define oo 1000111222
using namespace std;
typedef long long ll;
const int dx[]={-1,0,1,0,-1,1,1,-1};
      int dy[]={0,1,0,-1,1,1,-1,-1};

string a,re;
int n;
long long s;

void att(int i)
{
	//cout << i << " " << a << " " << s << endl;
	if (i<0)
	{
		long long k=ll(sqrt(s));
		if (k*k==s) re=a;
		return;
	}
	if (a[i]=='?')
	{
		a[i]='0';
		att(i-1);
		a[i]='1';
		s+=(1LL<<(n-1-i));
		att(i-1);
		s-=(1LL<<(n-1-i));
		a[i]='?';
	}
	else
	{
		if (a[i]=='1') s+=(1LL<<(n-1-i));
		att(i-1);
		if (a[i]=='1') s-=(1LL<<(n-1-i));
	}
}

int main()
{
	freopen("dsmall.in","r",stdin); freopen("dsmall.out","w",stdout);
	int test,it;
	cin >> test;
	fr(it,1,test)
	{
		cout << "Case #" << it << ": ";
		cin >> a;
		n=a.length();
		s=0;
		att(n-1);
		cout << re << endl;
	}
   return 0;
}

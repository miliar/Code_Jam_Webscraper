#include <map>
#include <set>
#include <queue>
#include <bitset>
#include <vector>
#include <numeric>
#include <sstream>
#include <iomanip>
#include <iostream>
#include <algorithm>
#include <cctype>
#include <cmath>
#include <cstdio>
#include <cstring>
using namespace std;

const int MAXN=2000001;

int n,m,ca;
string astring[MAXN];

void init()
{
	cin>>n>>m;
}

string ItoA(int n)
{
	string ret="";
	if (n==0) ret+='0';
	while (n)
	{
		ret=(char)('0'+n%10)+ret;
		n/=10;
	}
	return ret;
}

int check(int n)
{
	string st=astring[n];
	int len=st.size(); 
	st+=st;
	int p=1,tmp=0;
	for (int i=1; i<len; i++) p*=10;
	for (int i=1; i<=len; i++) tmp=tmp*10+(st[i]-'0');
	set<int> ret;
	if (tmp>n && tmp<=m) ret.insert(tmp);
	for (int i=2; i<=len; i++)
	{
		tmp=(tmp-(st[i-1]-'0')*p)*10+(st[i+len-1]-'0');
		if (tmp>n && tmp<=m) ret.insert(tmp);
	}
	return ret.size();
}

void solve()
{
	int ans=0;
	for (int i=n; i<=m; i++) ans+=check(i);
	cout<<ans<<endl;
}

int main()
{
	freopen("C.in","r",stdin);
	freopen("C.out","w",stdout);
	cin>>ca;
	for (int i=1; i<=2000000; i++)
	{
		astring[i]=ItoA(i);
	}
	for (int i=0; i<ca; i++)
	{
		cout<<"Case #"<<i+1<<": ";
		init();
		solve();
	}
	return 0;
}

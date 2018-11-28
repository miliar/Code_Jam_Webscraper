#include <set>
#include <cstdio>
#include <string>
#include <iostream>
#include <algorithm>
using namespace std;

int l,d,n,e,ans;
string x;

int m[75000][27],mm;

void f1 (int i,int j)
{
	if(j==l)
		return ;
	if(m[i][x[j]-'a']!=-1)
	{
		f1 (m[i][x[j]-'a'],j+1);
		return ;
	}
	m[i][x[j]-'a']=mm++;
	f1 (m[i][x[j]-'a'],j+1);
	return ;
}	
	
void f2 (int i,int j)
{
	if(j==e)
	{
		ans++;
		return ;
	}
	if(x[j]!='(')
	{
		if(m[i][x[j]-'a']!=-1)
			f2 (m[i][x[j]-'a'],j+1);
		return ;
	}
	int k,e;
	for(k=j+1;x[k]!=')';k++);
	e=k;
	for(k=j+1;k<e;k++)
	{
		if(m[i][x[k]-'a']!=-1)
			f2 (m[i][x[k]-'a'],e+1);
	}
	return ;
}

int main ()
{
	freopen ("Alien Language.in","r",stdin);
	freopen ("Alien Language.out","w",stdout);
	
	cin>>l>>d>>n;
	
	int i;
	mm=1;
	memset (m,-1,sizeof m);
	for(i=0;i<d;i++)
	{
		cin>>x;
		f1 (0,0);
	}
	
	for(i=1;i<=n;i++)
	{
		cin>>x;
		e=x.size ();
		ans=0;
		f2 (0,0);
		cout<<"Case #"<<i<<": "<<ans<<endl;
	}
	//scanf ("%d",&n);
	return 0;
}

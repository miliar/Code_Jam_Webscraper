#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <string>
#include <stack>
using namespace std;
int mymax(int a,int b){
	return a>b?a:b;
}
stack<int> h;
int add(int a,int b)
{
	int ta,tb,t,s=0;
	while (a || b)
	{
	
		ta=a%2;
	    tb=b%2;
		t=ta+tb;
		h.push(t%2);
		a/=2;
		b/=2;
	}
	while (!h.empty())
	{
		s=s*2+h.top();
		h.pop();
	}
	return s;	
}
int main()
{
	freopen("C-small-attempt3.in","r",stdin);
	freopen("ret.out","w",stdout);
	int i,ii,T,cases=1,n,s,a[20],k,suma,sumb,sa,sb,maxn;
	cin >>T;
	while (T--)
	{
		maxn=-99;
		cin >>n;
		s=1<<n;
		for(i=0;i<n;i++)
			cin >>a[i];
		for (i=1;i<s-1;i++)
		{
			ii=i;
			k=n-1;
			sa=sb=suma=sumb=0;
			while (ii)
			{
				if(ii%2)
					suma+=a[k],sa=add(sa,a[k]);
				else
					sumb+=a[k],sb=add(sb,a[k]);
				k--;
				ii/=2;
			}
			for(int j=0;j<=k;j++)
				sumb+=a[j],sb=add(sb,a[j]);
			if(sa==sb)
				maxn=mymax(maxn,suma);			
		}
		if(maxn<=0)
			cout <<"Case #"<<cases++<<": NO"<<endl;
		else
			cout <<"Case #"<<cases++<<": "<<maxn<<endl;
	}
	return 0;
}
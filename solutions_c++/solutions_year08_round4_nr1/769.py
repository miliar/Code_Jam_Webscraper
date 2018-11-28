
#include<stdio.h> 
#include<math.h> 
#include<string.h> 
#include<stdlib.h> 
#include<iostream>

using namespace std;

const int Maxn=10000;
int m;
bool v,value[Maxn],g[Maxn],c[Maxn];
int go(int x,bool v)
{
	int l,r;
	if (x>(m-1)/2)
	{
		if (value[x]==v)
			return 0;
		else return Maxn;
	}
		
	if (c[x])
	{
		if (value[2*x]!=value[2*x+1])
			return 1;
		l=go(2*x,!value[2*x]);
		r=go(2*x+1,!value[2*x+1]);
		if (g[x]==value[2*x]) return min(r,l);
		else return min(r,l)+1;
	}
	else
	{	
		l=go(2*x,!value[2*x]);
		r=go(2*x+1,!value[2*x+1]);
		
		if (value[2*x]==value[2*x+1])
		{
			if (value[2*x]==g[x])
				return min(r,l);
			else return r+l;
		}
		else if (value[2*x]!=g[x])
		return l;
		else return r;
	}
}
	
	
		

int main() 
{ 
	int rn,i,ans;
	cin >> rn;
	for (int ri=1;ri<=rn;++ri)
	{
		cout << "Case #" << ri << ": ";
		cin >> m >> v;
		for (i=1;i<=(m-1)/2;++i)
			cin >> g[i] >> c[i];
		for (i=(m-1)/2+1;i<=m;++i)
			cin >> value[i];
		for (i=(m-1)/2;i>0;i--)
		 if (g[i]) value[i]=value[2*i] && value[2*i+1];
		 else value[i]=value[2*i] || value[2*i+1];
		if (v==value[1])
		{
			cout << 0 << endl;
			continue;
		}
		ans=go(1,v);
		if (ans<Maxn) cout << ans << endl;
		else cout << "IMPOSSIBLE" << endl;
	}

//	system("PAUSE");
	return 0;
	
} 



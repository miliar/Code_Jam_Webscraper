#include <iostream>
#include <fstream>
#include <cstdlib>
#include <cmath>
#include <ctime>
#include <vector>
#include <algorithm>
#include <string>
#include <cstdio> 
#include <deque>  
#include <queue>
#include <stack> 
#include <iomanip>
#include <cctype>

#define rep(i,n) for(i=0; i<n; i++)
#define ALL(c) (c).begin(), (c).end()
#define SORT(c) sort(ALL(c))
#define REVERSE(c) reverse(ALL(c))
#define INF 1000000000
#define X first
#define Y second
#define pb push_back
#define sz(c) (c).size()

using namespace std;




int main()
{
	int i,j,k,N,n,T;
	ifstream in("input.txt");
	ofstream out("output.txt");
	in>>T;
	string s;
	rep(i,T)
	{
		in>>s;
		vector<int> v;
		n=sz(s);
		rep(j,n)
			v.push_back(-1);
		for(k=0;k<n;k++)
			if (s[k]==s[0])
				v[k]=1;
		int c=0;
		for(j=1;j<n;j++)
		{
			if (c==1) c++;
			if (v[j]<0)
			{
				for(k=j;k<n;k++)
					if (s[k]==s[j])
						v[k]=c;
				c++;
			}
		}
		if (c<2) c=2;
		string r="0";
		rep(j,n)
		{
			int b=v[j];
			int buf=0;
			rep(k,sz(r))
			{
				int q=(r[k]-'0')*c+buf;
				r[k]=q%10+'0';
				//cout<<"("<<q<<") "<<r[k]<<" ";
				buf=q/10;
			}
			if (buf>0){ r.pb(buf+'0'); /*cout<<" : "<<(buf)<<" ";*/ }
			cout<<r<<endl;//<<r<<endl<<"- ";
			buf=0;
			k=0;
			while (b>0)
			{
				int q=(r[k]-'0')+buf+b%10;
				r[k]=q%10+'0';
				buf=q/10;
				b/=10;
				//cout<<r[k]<<" ";
				k++;
			}
			if ((buf>0)&&(k<sz(r))) r[k]+=buf;
			else if (buf>0) r.pb(buf+'0');
		}
		REVERSE(r);
		out<<"Case #"<<(i+1)<<": "<<r<<endl;
		cout<<"Case #"<<(i+1)<<" "<<s<<" : "<<r<<endl;
		rep(j,n)
			cout<<v[j];
	}
	return 0;
}


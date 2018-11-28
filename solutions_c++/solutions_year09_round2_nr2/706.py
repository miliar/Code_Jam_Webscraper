#include<cstdio>
#include<cstring>
#include<cstdlib>
#include<cctype>

#include<cmath>
#include<iostream>
#include<fstream>

#include<string>
#include<vector>
#include<queue>
#include<map>
#include<algorithm>
#include<set>
#include<sstream>
#include<stack>
using namespace std;

#define max(a,b) ((a)>(b)?(a):(b))
#define min(a,b) ((a)<(b)?(a):(b))
#define pi acos(-1.0)
#define inf (1<<30)
#define clr(a,b) memset(a,b,sizeof(a))
#define pb push_back

int main()
{
	freopen("B-large.in","r",stdin);
	freopen("out.txt","w",stdout);

	int cs,t=1,n,i,tmp,j;
	string a,s,r;
	cin>>cs;
	while(cs--)
	{
		cin>>a;
		s=a;
		next_permutation(a.begin(),a.end());
		r=a;
		if(r<=s)
		{
			int l=r.size();
			for(i=0;i<r.size();i++)
			{
				if(r[i]!='0')
					break;
			}
			s=r.substr(i,r.size());
			r="";
			r+=s[0];
			for(i=0;i<=l-s.size();i++)
				r+='0';
			r+=s.substr(1,s.size());
		}
		cout<<"Case #"<<t++<<": "<<r<<endl;
	}
	return 0;
}



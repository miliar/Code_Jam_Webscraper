#include<cstdio>
#include<cmath>
#include<iostream>
#include<cstdlib>
#include<cstring>
#include<algorithm>
using namespace std;
typedef long long ll;
int main()
{
	int _;scanf("%d",&_);
	for(int __=1;__<=_;__++)
	{
		string s;
		cin>>s;
		int S=0,n=s.length();
		for(int i=0;i<n;i++)S+=s[i]=='?';
		if(S==0)S=1;
		for(int i=0;i<(1<<S);i++)
		{
			string t=s;
			for(int j=0,w=0;j<n;j++)
				if(t[j]=='?'){t[j]='0'+((i>>w)&1);w++;}
			ll T=0;
			for(int i=0;i<n;i++)
				T*=2,T+=t[i]=='1';
			ll W=(ll)sqrt(T);
			if(W*W==T){cout<<"Case #"<<__<<": "<<t<<endl;;break;}
		}
	}
	return 0;
}

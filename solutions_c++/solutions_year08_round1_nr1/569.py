#include <iostream>
#include <string>
#include <vector>
#include <map>
#include <cstdio>
#include <algorithm>

using namespace std;

typedef long long ll;
typedef vector < string > vs;
typedef vector <int> vi;
#define FOREACH(it,c) for(typeof((c).begin()) it=(c).begin();it!=(c).end();++it)
#define deb(x) cout << #x << ": " << x << endl;
#define debv(x) for(int i = 0; i < (x).size(); i++) cout << x[i] << ' '; cout << endl;
typedef pair<ll, ll> pll;

int main()
{
	int num=0,nt;
	scanf("%d",&nt);
	while (num++<nt)
	{
		int n,v1[802],v2[802];
		ll res=1e+15,tmp;
		memset(v1,0,sizeof(v1));
		memset(v2,0,sizeof(v2));
		cin>>n;
		for(int i=0;i<n;i++)
			cin>>v1[i];
		for(int i=0;i<n;i++)
			cin>>v2[i];
		sort(v1,v1+n);
		sort(v2,v2+n);
/*
		for(int i=0;i<n;i++)
			cout<<v1[i]<<" ";
		cout<<endl;
		*/
		tmp=0;
		for(int i=0;i<n;i++)
			tmp+=(ll)v1[i]*v2[i];
		res=tmp;
		tmp=0;
		for(int i=0;i<n;i++)
			tmp+=(ll)v1[i]*v2[n-i-1];
		if(tmp<res)res=tmp;

		cout<<"Case #"<<num<<": "<<res<<endl;
	}
	return 0;	
}

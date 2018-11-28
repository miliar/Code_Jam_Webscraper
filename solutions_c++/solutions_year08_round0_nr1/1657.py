#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
using namespace std;
string v[110],vv[1010];
int a[110][1010];
int n,s,q;
int f(int i,int j)
{
	if(j==q)return 0;
	if(a[i][j]!=-1)return a[i][j];
	int r1=2000000000;
	if(v[i]==vv[j]){
		for(int k=0;k<s;k++)
			if(k!=i)
				r1=min(r1,f(k,j+1)+1);
		return a[i][j]=r1;
	}
	return a[i][j]=f(i,j+1);
}
int main()
{
	freopen("A-large.in","r",stdin);
	freopen("A-small.out","w",stdout);
	cin>>n;
	for(int i=0;i<n;i++)
	{
		memset(a,-1,sizeof(a));
		cin>>s;
		string ss;
		cin.get();
		for(int j=0;j<s;j++)
		{
			getline(cin,ss);
			v[j]=ss;
		}
		cin>>q;
		cin.get();
		for(int k=0;k<q;k++)
		{
			getline(cin,ss);
			vv[k]=ss;
		}
		int min=2000000000,t;
		for(int l=0;l<s;l++)
			if((t=f(l,0))<min)min=t;
		cout<<"Case #"<<i+1<<": "<<min<<endl;
	}
	return 0;
}
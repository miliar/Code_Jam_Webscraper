#include<iostream>
#include<cstdio>
#include<cstring>
#include<string>
#include<algorithm>
#include<map>
using namespace std;
map<int,int> a;
int n,ans;

void solve(int x)
{
	ans++;
	a[x-1]++;	a[x+1]++;
	a[x]-=2;
	if (a[x]>1) solve(x);
	if (a[x-1]>1) solve(x-1);
	if (a[x+1]>1) solve(x+1);
}

int work()
{
	int x,y;
	a.clear();
	ans=0;
	cin>>n;
	for (int i=1;i<=n;i++)
	{
		cin>>x>>y;
		a[x]+=y;
		if (a[x]>1) solve(x);
	}
	return ans;
}

int main()
{
	freopen("C-small-attempt0.in","r",stdin);
	freopen("c.out","w",stdout);
	int Test;
	cin>>Test;
	for (int t=1;t<=Test;t++)
		cout<<"Case #"<<t<<": "<<work()<<endl;
	fclose(stdin);	fclose(stdout);
	return 0;
}






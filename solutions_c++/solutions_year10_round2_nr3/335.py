#include <stdio.h>
#include <string>
#include <map>
#include <iostream>
using namespace std;

int N;
int a[30],cnt,res;

void check()
{
	int cur=1;
	while (a[cur]!=N&&cur<cnt) cur=a[cur];
	if (a[cur]==N&&cur<cnt) res++;
	return;
};

void dfs(int pos)
{
	if (pos==N)
	{
		a[cnt++]=N;
		check();
		cnt--;
		return;
	}
	else
	{
		a[cnt++]=pos;
		dfs(pos+1);
		cnt--;
		dfs(pos+1);
		return;
	}
}

int main()
{
	freopen("D://in.txt","r",stdin);
	freopen("D://out.txt","w",stdout);

	int T,cas,i;

	cin>>T;
	for (cas=1;cas<=T;cas++)
	{
		cin>>N;
		res=0;
		cnt=1;
		a[0]=0;
		dfs(2);
		cout<<"Case #"<<cas<<": "<<res%100003<<endl;
	}
	return 0;
}
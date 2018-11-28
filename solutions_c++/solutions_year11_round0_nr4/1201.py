//In the name of Allah
//
//
#include <iostream>
#include <iomanip>
#include <cstring>
using namespace std;
const int MN=1000+10;
bool mark[MN];
int n,t;
int list[MN];
int tg=0;
void dfs(int a)
{
	mark[a]=1;
	tg++;
	if (!mark[list[a]])
		dfs(list[a]);
}
int main()
{
	ios::sync_with_stdio(false);
	cin>>t;
	for (int c=0;c<t;c++)
	{
		memset(mark,0,sizeof(mark));
		cin>>n;
		for (int i=0;i<n;i++)
		{
			int a;
			cin>>a; a--;
			list[i]=a;
		}
		int res=0;
		for (int i=0;i<n;i++) if (!mark[i])
		{
			tg=0;
			dfs(i);
			if (tg!=1)
				res+=tg;
		}
		cout<<"Case #"<<c+1<<": "<<fixed<<setprecision(8)<<double(res)<<endl;
	}
	return 0;
}

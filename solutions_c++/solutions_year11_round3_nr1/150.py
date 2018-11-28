//In the name of Allah
//
//
#include <iostream>
#include <set>
#include <cstring>
using namespace std;
const int MN=50+10;
bool map[MN][MN];
int av[MN][MN];
struct pie
{
	int x,y;
	pie() {}
	pie(int _x,int _y)
	{
		x=_x;y=_y;
	}
};
bool operator < (const pie & a,const pie & b)
{
	if (a.x!=b.x)
		return a.x<b.x;
	return a.y<b.y;
}
set <pie> me;
int n,m,t;
bool tr(int x,int y)
{
	if (x+1<n && y+1<m && !av[x][y+1] && !av[x+1][y] && !av[x+1][y+1] && map[x][y+1] && map[x+1][y] && map[x+1][y+1])
		return 1;
	return 0;
}
void print(int a)
{
	if (a==0)
		cout<<".";
	else if (a==1 || a==4)
		cout<<"/";
	else
		cout<<"\\";
}
int main()
{
	ios::sync_with_stdio(false);
	cin>>t;
	for (int c=1;c<=t;c++)
	{
		cin>>n>>m;
		memset(map,0,sizeof(map));
		memset(av,0,sizeof(av));
		me.clear();
		for (int i=0;i<n;i++)
			for (int j=0;j<m;j++)
			{
				char ca;
				cin>>ca;
				if (ca=='#')
				{
					map[i][j]=1;
					me.insert(pie(i,j));
				}
			}
		cout<<"Case #"<<c<<":"<<endl;
		bool f=true;
		while (!me.empty())
		{
			pie now=*me.begin();
			me.erase(me.begin());
			if (!tr(now.x,now.y))
			{
				cout<<"Impossible"<<endl;
				f=false;
				break;
			}
			int x=now.x,y=now.y;
			av[x][y]=1;
			av[x][y+1]=2;
			av[x+1][y]=3;
			av[x+1][y+1]=4;
			me.erase(pie(x,y+1));
			me.erase(pie(x+1,y));
			me.erase(pie(x+1,y+1));
		}
		if (!f)
			continue;
		for (int i=0;i<n;i++)
		{
			for (int j=0;j<m;j++)
				print(av[i][j]);
			cout<<endl;
		}
	}
	return 0;
}

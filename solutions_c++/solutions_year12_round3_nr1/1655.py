#include <iostream>
using std::cout;
using std::cin;

int cases,n,m,temp;
bool d,newpath,p[1010][1010],path[1010][1010],found;
int main()
{
	
	cin>>cases;
	for(int kase=1;kase<=cases;kase++)
	{
		cin>>n;
		for(int i=1;i<=n;i++)
		{
			for(int j=1;j<=n;j++)
			{
				p[i][j]=false;
				path[i][j]=false;
			}
		}
		for(int i=1;i<=n;i++)
		{
			cin>>m;
			for(int j=1;j<=m;j++)
			{
				cin>>temp;
				p[i][temp]=true;
				path[i][temp]=true;
			}
		}
		d=false;
		for(int x=1;x<=n;x++)
		{
			newpath=false;
			for(int i=1;i<=n;i++)
			{
				for(int j=1;j<=n;j++)
				{
					if(j==i)continue;
					found=false;
					if(p[i][j])found=true;
					for(int k=1;k<=n;k++)
					{
						if(k==j || k==i)continue;
						if(path[i][k]&&p[k][j])
						{
							newpath=true;
							if(found)
							{
								d=true;
								break;
							}
							else
							{
								found=true;
								path[i][j]=true;
							}
						}
					}
					if(d)break;
				}
				if(d)break;
			}
			if(!newpath || d)break;
		}
		cout<<"Case #"<<kase<<": ";
		if(d)cout<<"Yes\n";
		else cout<<"No\n";
	}
	return 0;
}
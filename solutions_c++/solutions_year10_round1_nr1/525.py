#include <iostream>
#include <string>
#define maxn 100
using namespace std;
int tn,n,k;
string map[maxn];
string anstype[4]={"Neither","Blue","Red","Both"};

int find_horizon(char ch)
{
	int i,j,ans=0;
	for (i=0;i<n;i++)
	{
		int res=0;
		for (j=0;j<=n;j++)
			if (map[i][j]==ch)
				res++;
			else
			{
				ans=max(ans,res);
				res=0;
			}
	}
	return ans;
}

int find_vertical(char ch)
{
	int i,j,ans=0;
	for (j=0;j<n;j++)
	{
		int res=0;
		for (i=0;i<=n;i++)
			if (map[i][j]==ch)
				res++;
			else
			{
				ans=max(ans,res);
				res=0;
			}
	}
	return ans;
}

int find_diagonal(char ch)
{
	int i,j,ans=0;
	for (i=0;i<n;i++)
	{
		int res=0;
		int tx=i,ty=0;
		while (tx<=n && ty<=n)
		{
			if (map[tx][ty]==ch)
			{
				res++;
				ans=max(ans,res);
			}
			else
			{
				ans=max(ans,res);
				res=0;
			}
			tx++;ty++;
		}
	}
	for (j=0;j<n;j++)
	{
		int res=0;
		int tx=0,ty=j;
		while (tx<=n && ty<=n)
		{
			if (map[tx][ty]==ch)
			{
				res++;
				ans=max(ans,res);
			}
			else
			{
				ans=max(ans,res);
				res=0;
			}
			tx++;ty++;
		}
	}
	for (i=0;i<n;i++)
	{
		int res=0;
		int tx=i,ty=n-1;
		while (tx<=n && ty>=0)
		{
			if (map[tx][ty]==ch)
			{
				res++;
				ans=max(ans,res);
			}
			else
			{
				ans=max(ans,res);
				res=0;
			}
			tx++;ty--;
		}
	}
	for (j=0;j<n;j++)
	{
		int res=0;
		int tx=0,ty=j;
		while (tx<=n && ty>=0)
		{
			if (map[tx][ty]==ch)
			{
				res++;
				ans=max(ans,res);
			}
			else
			{
				ans=max(ans,res);
				res=0;
			}
			tx++;ty--;
		}
	}
	return ans;
}

void Go_right()
{
	int i,j;
	map[n].insert(0,n+1,'X');
	for (i=0;i<n;i++)
		map[i]+='X';
	for (j=n-1;j>=0;j--)
		for (i=0;i<n;i++)
			if (map[i][j]!='.')
			{
				int t=j;
				while (map[i][t+1]=='.')
				{
					map[i][t+1]=map[i][t];
					map[i][t++]='.';
				}
			}
}

int main()
{
	freopen("A2-large.in","r",stdin);
	freopen("A2_large.out","w",stdout);
	int i;
	cin >> tn;
	for (int t=1;t<=tn;t++)
	{
		cin >> n >> k;
		cin.ignore(255,'\n');
		memset(map,0,sizeof map);
		for (i=0;i<n;i++)
			getline(cin,map[i]);
		Go_right();
		int maxr=0,maxb=0;
		maxr=max(find_horizon('R'),find_vertical('R'));
		maxr=max(maxr,find_diagonal('R'));
		maxb=max(find_horizon('B'),find_vertical('B'));
		maxb=max(maxb,find_diagonal('B'));
		int ans=0;
		if (maxr>=k) ans+=2;
		if (maxb>=k) ans+=1;
		cout << "Case #" << t << ": " << anstype[ans] << endl;
	}
}
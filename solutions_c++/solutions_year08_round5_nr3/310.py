#include <iostream>
#include <vector>
#include <string>

using namespace std;

vector <string> cl;
int sum,M,N;

int mx(int a, int b)
{
	return a>b?a:b;
}

int back (int x, int y)
{
	if (x>=N)
	{
		return sum;
	}
	if (cl[y][x]!='.')
	{
		y++;
		if (y>=M)
		{
			y=0;
			x++;
		}
		return back(x,y);
	}
	int max=-1;
	int y2;
	for (y2=y+1;y2<M and cl[y2][x]=='.';y2++);
	if (y2==M)
	{
		max=back(x+1,0);
	}
	else
	{
		max=back(x,y2);
	}
	bool ojo=false;
	if (x<N-1)
	{
		for (int i=y-1;i<=y2;i++)
		{
			if (i>=0 and i<M)
			{
				if (i==y-1 and cl[i][x+1]=='o')
					ojo=true;
				if (cl[i][x+1]=='.')
					cl[i][x+1]='o';
			}
		}
	}
	sum+=y2-y;
	int m2=-1;
	if (y2==M)
	{
		m2=back(x+1,0);
	}
	else
		m2=back(x,y2);
	sum-=y2-y;
	if (x<N-1)
	{
		for (int i=y-1;i<=y2;i++)
		{
			if (i>=0 and i<M)
			{
				if (i!=y-1 or not ojo)
				{
					if (cl[i][x+1]=='o')
						cl[i][x+1]='.';
				}
			}
		}
	}
	return mx(max,m2);
}

int main()
{
	int C;
	cin >> C;
	for (int caso=1;caso<=C;caso++)
	{
		cin >> M >> N;
		cl=vector <string> (M);
		for (int i=0;i<M;i++)
		{
			cin >> cl[i];
		}
		sum=0;
		int res=back(0,0);
		cout << "Case #" << caso << ": " << res << endl;
	}
}

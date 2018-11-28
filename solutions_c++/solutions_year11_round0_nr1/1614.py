#include <iostream>
#include <fstream>

using namespace std;

struct node
{
	int p;
	char c;
}a[101];
int n;

int MinSec();
int abs(int x)
{
	return x>0?x:-x;
}
int main()
{
	freopen("A-large.in", "r",stdin);
	int cas;
	cin >> cas;
	ofstream os("out.txt");
	for(int i = 1; i <= cas ; i++)
	{
		cin >> n;
		for(int j = 0; j < n ;j++)
			cin >> a[j].c >> a[j].p;

		os << "Case #"<< i<<": "<<MinSec()<<endl;
	}
	return 0;
}

int MinSec()
{
	int dt = 0, tt, sum = 0;
	char pre = ' ';
	int op = 1, bp = 1;

	for(int i = 0; i<n; i++)
	{
		if( a[i].c == 'O' &&( a[i].c == pre|| pre == ' '))
		{
			tt = abs(a[i].p - op) + 1;
			sum += tt;
			dt += tt;
			pre = 'O';
			op = a[i].p;
		}
		else if(a[i].c == 'B' && ( a[i].c == pre|| pre == ' '))
		{
			tt = abs(a[i].p - bp) + 1;
			dt += tt;
			sum += tt;
			pre = 'B';
			bp = a[i].p;
		}
		else if(a[i].c == 'O')
		{
			tt = abs(a[i].p - op) + 1;
			if(tt > dt)
			{
				sum += tt - dt;
				dt = tt -dt;
			}
			else
			{
				sum += 1;				
				dt = 1;
			}
			op = a[i].p;
			pre = 'O';
		}
		else
		{
			tt = abs(a[i].p -bp) + 1;
			if(tt > dt)
			{
				sum += tt -dt;
				dt = tt - dt;				
			}
			else
			{
				sum += 1;
				dt = 1;
			}
			pre = 'B';
			bp = a[i].p;
		}
	}
	return sum;
}

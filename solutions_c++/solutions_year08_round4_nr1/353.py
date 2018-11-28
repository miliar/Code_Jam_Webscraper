#include <iostream>
#include <fstream>

using namespace std;
ifstream fin("A-large.in");
ofstream fout("p1.out");

//#define fout cout
#define NEG -100000

bool v[11000], change[1100];
int f[11000][2];
int n, ans;

void init()
{
	fin>>n>>ans;
	for (int i=1;i<=(n-1)/2;i++)
	{
		fin>>v[i]>>change[i];
	}
	for (int i=(n-1)/2+1;i<=n;i++)
	{
		fin>>v[i];
		change[i]=false;
	}
}
int get_and_false(int a[], int b[])
{
	if (a[0]<0) return b[0];
	else if (b[0]<0) return a[0];
	else return min(a[0],b[0]);
}
int get_and_true(int a[], int b[])
{
	if (a[1]>=0&&b[1]>=0) return a[1]+b[1];
	else return -1;
}
int get_or_false(int a[], int b[])
{
	if (a[0]>=0&&b[0]>=0) return a[0]+b[0];
	else return -1;
}
int get_or_true(int a[], int b[])
{
	if (a[1]<0) return b[1];
	else if (b[1]<0) return a[1];
	else return min(a[1],b[1]);
}

void calc()
{
	int leaf = (n-1)/2;
	for (int i=n;i>=1;i--)
	{
		if (i>leaf)
		{
			f[i][v[i]] = 0;
			f[i][!v[i]] = NEG;
		}
		else if (v[i]) // and
		{
			int l=2*i, r=l+1;
			f[i][0] = get_and_false(f[l],f[r]);
			f[i][1] = get_and_true(f[l],f[r]);

			if (change[i])
			{
				int x = get_or_false(f[l],f[r]);
				if (x>=0)
					if (f[i][0]<0) f[i][0] = x+1;
					else f[i][0]=min(f[i][0],x+1);

				x=get_or_true(f[l],f[r]);
				if (x>=0)
					if (f[i][1]<0) f[i][1] =x+1;
					else f[i][1]=min(f[i][1],x+1);
			}
		} else // or 
		{
			int l=2*i, r=2*i+1;

			f[i][0]=get_or_false(f[l],f[r]);
			f[i][1]=get_or_true(f[l],f[r]);

			if (change[i])
			{
				int x=get_and_false(f[l],f[r]);
				if (x>=0)
					if (f[i][0]<0) f[i][0]=x+1;
					else f[i][0] = min(f[i][0],x+1);

				x=get_and_true(f[l],f[r]);
				if (x>=0)
					if (f[i][1]<0) f[i][1]=x+1;
					else f[i][1]=min(f[i][1],x+1);
			}
		}
	}
	if (f[1][ans]<0) fout<<"IMPOSSIBLE\n";
	else fout<<f[1][ans]<<endl;
}
int main()
{
	int t;
	fin>>t;
	for (int i=1;i<=t;i++)
	{
		init();
		fout<<"Case #"<<i<<": ";
		calc();
	}
}
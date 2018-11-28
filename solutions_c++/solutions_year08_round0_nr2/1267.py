#include <iostream>
#include <fstream>

using namespace std;
//ifstream fin("B-small-attempt0.in");
ifstream fin("B-large.in");
ofstream fout("b.out");

int a[2][110], b[2][110];
int na, nb;
int n;

void init()
{
	int x, y;
	char ch;

	fin>>n>>na>>nb;
	int i, j;
	for (i=0;i<na;i++)
		for (j=0;j<2;j++)
		{
			fin>>x>>ch>>y;
			a[j][i]=x*60+y;
		}
	for (i=0;i<nb;i++)
		for (j=0;j<2;j++)
		{
			fin>>x>>ch>>y;
			b[j][i]=x*60+y;
		}
}
void my_sort(int a[2][110], int n, int k)
{
	int i, j;
	for (i=0;i<n;i++)
		for (j=i+1;j<n;j++)
			if (a[k][j]<a[k][i])
			{
				swap(a[k][j],a[k][i]);
				swap(a[k^1][j],a[k^1][i]);
			}
}
void calc()
{
	int i, j, ans=0;
	my_sort(a,na,0);
	my_sort(b,nb,1);
	for (i=0, j=0;i<na;i++)
	{
		if (j<nb && b[1][j]+n<=a[0][i])
		{
			j++;
		}
		else ans++;
	}
	fout<<ans<<' ';
	cout<<ans<<' ';
	ans=0;
	my_sort(a,na,1);
	my_sort(b,nb,0);
	for (i=0, j=0;i<nb;i++)
	{
		if (j<na && a[1][j]+n<=b[0][i])
		{
			j++;
		}
		else ans++;
	}
	fout<<ans<<endl;
	cout<<ans<<endl;
}
int main()
{
	int t;
	fin>>t;
	for (int i=1;i<=t;i++)
	{
		fout<<"Case #"<<i<<": ";
		init();
		calc();
	}
}
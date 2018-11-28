// ag.cpp : Defines the entry point for the console application.
//

#include <fstream>
using namespace std;
int t,n,k;
char a[50][50];
char b[50][50];
int f1,f2;

int main()
{
	ifstream in("A-small-attempt0.in");
	ofstream out("output.txt");
	in >> t;
	for (int p=0;p<t;p++)
	{
		in >> n >> k;
		f1=0;
		f2=0;
		for (int i=0;i<n;i++) for (int j=0;j<n;j++) in >> a[i][j];
		for (int i=0;i<n;i++) for (int j=0;j<n;j++) b[j][n-1-i]=a[i][j];
		for (int j=0;j<n;j++)
		{
			int i=n-1;
			int l=n-1;
			while ((i>=0) && (l>=0))
			{
				if (i>l) i=l-1;
				if (b[l][j]!='.')
				{
					l=l-1;
					if (b[i][j]=='.')
					{
						i=i-1;
					}
				}
				else
				{
					if (b[i][j]=='.')
					{
						i=i-1;
					}
					else
					{
						swap(b[l][j],b[i][j]);
						l=l-1;
						i=i-1;
					}
				}
			}
		}
		for (int i=0;i<n;i++) for (int j=0;j<=n-k;j++)
		{
			if (b[i][j]=='R')
			{
				int z=1;
				for (int x=0;x<k-1;x++)
				{
					if (b[i][j+x]!=b[i][j+x+1]) z=-1;
				}
				if (z==1) f1=1;
			}
			if (b[i][j]=='B')
			{
				int z=1;
				for (int x=0;x<k-1;x++)
				{
					if (b[i][j+x]!=b[i][j+x+1]) z=-1;
				}
				if (z==1) f2=1;
			}
		}
		for (int i=0;i<=n-k;i++) for (int j=0;j<n;j++)
		{
			if (b[i][j]=='R')
			{
				int z=1;
				for (int x=0;x<k-1;x++)
				{
					if (b[i+x][j]!=b[i+x+1][j]) z=-1;
				}
				if (z==1) f1=1;
			}
			if (b[i][j]=='B')
			{
				int z=1;
				for (int x=0;x<k-1;x++)
				{
					if (b[i+x][j]!=b[i+x+1][j]) z=-1;
				}
				if (z==1) f2=1;
			}
		}
		for (int i=0;i<=n-k;i++) for (int j=0;j<=n-k;j++)
		{
			if (b[i][j]=='R')
			{
				int z=1;
				for (int x=0;x<k-1;x++)
				{
					if (b[i+x][j+x]!=b[i+x+1][j+x+1]) z=-1;
				}
				if (z==1) f1=1;
			}
			if (b[i][j]=='B')
			{
				int z=1;
				for (int x=0;x<k-1;x++)
				{
					if (b[i+x][j+x]!=b[i+x+1][j+x+1]) z=-1;
				}
				if (z==1) f2=1;
			}
		}
		if (f1==1)
		{
			if (f2==1) out << "Case #" << p+1 << ": Both" << '\n';
			else out << "Case #" << p+1 << ": Red" << '\n';
		}
		else
		{
			if (f2==1) out << "Case #" << p+1 << ": Blue" << '\n';
			else out << "Case #" << p+1 << ": Neither" << '\n';
		}
	}
	return 0;
}


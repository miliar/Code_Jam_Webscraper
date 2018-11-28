// g2c.cpp : Defines the entry point for the console application.
//

#include <fstream>
using namespace std;
ifstream in("C-small-attempt1.in");
ofstream out("output.txt");
int c,r;
int x1[1000],y1[1000],x2[1000],y2[1000];
int a[100][100];
int g;
int s;
int main()
{
	in >> c;
	for (int i=0;i<c;i++)
	{
		in >> r;
		g=0;
		s=0;
		for (int j=0;j<r;j++) in >> x1[j] >> y1[j] >> x2[j] >> y2[j];
		for (int j=0;j<100;j++) for (int k=0;k<100;k++) a[j][k]=0;
		for (int j=0;j<r;j++)
		{
			for (int k=x1[j]-1;k<=x2[j]-1;k++) for (int l=y1[j]-1;l<=y2[j]-1;l++)
			{
				if (a[k][l]==0)
				{
					g=g+1;
					a[k][l]=1;
				}
			}
		}
		while (g>0)
		{
			s=s+1;
			for (int j=99;j>0;j--) for (int k=99;k>0;k--)
			{
				if ((a[j][k]==1) && (a[j-1][k]==0) && (a[j][k-1]==0))
				{
					a[j][k]=0;
					g=g-1;
				}
				else if ((a[j][k]==0) && (a[j-1][k]==1) && (a[j][k-1]==1))
				{
					a[j][k]=1;
					g=g+1;
				}
			}
			for (int j=99;j>0;j--)
			{
				if ((a[j][0]==1) && (a[j-1][0]==0))
				{
					a[j][0]=0;
					g=g-1;
				}
				if ((a[0][j]==1) && (a[0][j-1]==0))
				{
					a[0][j]=0;
					g=g-1;
				}
			}
			if (a[0][0]==1)
			{
				a[0][0]=0;
				g=g-1;
			}
		}
		out << "Case #" << i+1 << ": " << s << '\n';
	}
	return 0;
}


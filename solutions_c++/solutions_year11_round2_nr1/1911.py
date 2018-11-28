#include<iostream>
#include<fstream>
#include<iomanip>
using namespace std;

char a[200][200];
double b[102][2];
double ans[101];
int main()
{
	ofstream fout("ans");
	int t;
	cin >> t ;
	int n;
	double wp,owp,oowp;
	int g;
	for(int x = 1;x<=t;x++)
	{
		wp = owp = oowp = 0;
		cin >> n;
		for(int i=0;i<n;i++)
			cin >> a[i];

		for(int z=0;z<n;z++)
		{
			int w,to;
			w = to= 0;
			for(int i=0;i<n;i++)
				if(a[z][i]!='.')
				{
					if( a[z][i]=='1')
					{w++,to++;}
					else
						to++;
				}
			wp = (double)w/(double)to;
			////
			b[z][0] = wp;
			b[z][1] = 0;
			g = 0;
			for(int i=0;i<n;i++)
			{	
				if(a[z][i]!='.')
				{
					g++;
					int w,to;
					w = to= 0;
					for(int j=0;j<n;j++)
						if(a[i][j]!='.' && j!=z)
						{
							if( a[i][j]=='1')
							{w++,to++;}
							else
								to++;
						}
					owp = (double)w/(double)to;
					b[z][1] += owp;
				}
			}
			b[z][1] /= g;
		}
		for(int z = 0;z<n;z++)
		{
			double tmp= 0;
			g = 0;
			for(int i=0;i<n;i++)
			{
				if(a[z][i]!='.')
				{	tmp += b[i][1];g++;}
			}
			ans[z] = 0.25*b[z][0]+0.5*b[z][1]+0.25*(tmp/g);
		}
		fout << "Case #" << x << ": "<< endl;
		for(int i=0;i<	n;i++)
			fout << setprecision(12) << ans[i] << endl;
	}
}
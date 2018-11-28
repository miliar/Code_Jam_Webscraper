#include <fstream>
#include <cstdio>
#include <algorithm>
#include <iomanip>
#include <list>
#include <vector>
#include <map>
#include <math.h>
#define ms(a,b) memset(a,b,sizeof(a))
#define fori(i,a,b) for(int i=a;i<=b;i++)
using namespace std;
char m[100][100];
int mas[100][2];
double wp[100];
double owp[100];
double oowp[100];
int main()
{
	ifstream in("A-large.in");
	ofstream out("A-large.out");
	int T,n;
	in>>T;
	fori(i,1,T)
	{
		ms(mas,0);
		ms(wp,0);
		ms(owp,0);
		ms(owp,0);
		in>>n;
		fori(g,0,n-1)
			in>>m[g];
		fori(g,0,n-1)
		{
			int w=0;
			int c=0;
			fori(h,0,n-1)
			{
				if(m[g][h]!='.')
				{	c++;
					if(m[g][h]=='1')
						w++;
				}
			}
			mas[g][0]=w;
			mas[g][1]=c;
			wp[g]=(double)w/c;
		}
		fori(g,0,n-1)
		{
			double sum=0;
			int k=0;
			fori(h,0,n-1)
				if(m[g][h]!='.')
				{
					k++;
					int c=mas[h][1];
					int w=mas[h][0];
					if(m[g][h]=='0')
						c--,w--;
					else
						c--;
					sum+=(double)w/c;
				}
			owp[g]=(double)sum/k;
		}
		fori(g,0,n-1)
		{
			double sum=0;
			int k=0;
			fori(h,0,n-1)
			{
				if(m[g][h]!='.')
					sum+=owp[h],k++;
			}
			oowp[g]=(double)sum/k;
		}
		out<<"Case #"<<i<<": "<<endl;
		/*fori(g,0,n-1)
			out<<setprecision(8)<<wp[g]<<endl;
		out<<"/----------------------------"<<endl;
		fori(g,0,n-1)
			out<<setprecision(8)<<owp[g]<<endl;
		out<<"/----------------------------"<<endl;
		fori(g,0,n-1)
			out<<setprecision(8)<<oowp[g]<<endl;
		out<<"/----------------------------"<<endl;*/
		fori(g,0,n-1)
			out<<setprecision(10)<<(double)(0.25*wp[g]+0.5*owp[g]+0.25*oowp[g])<<endl;
		//out<<"/----------------------------"<<endl;
	}
	return 0;
}
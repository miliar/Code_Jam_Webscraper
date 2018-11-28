#include<iostream.h>
#include<fstream.h>
#include<conio.h>
#include<iomanip.h>
#include<math.h>
void main()
{
	int t,c;
	long int n,k,r,*g,j,cost,sum,i;
	ifstream fi("C-small-attempt0.in",ios::binary|ios::in);
	ofstream fo("test.out",ios::out);
	fi>>t;
	for(int t_c=0;t_c<t;t_c++)
	{
		fi>>r>>k>>n;
		cost=0;
		g=new long int[n];
		for(i=0;i<n;i++)
	  		fi>>g[i];
      i=0;
		for(j=0;j<r;j++)
		{
			sum=c=0;
			while((sum+g[i])<=k&&c<n)
			{
				sum+=g[i];
				i++;
				i=i%n;
            c++;
			}
			cost+=sum;
		}
		fo<<"Case #"<<(t_c+1)<<": "<<cost<<endl;
		cout<<t_c<<endl;
	}
	fi.close();
	fo.close();
	getch();
}


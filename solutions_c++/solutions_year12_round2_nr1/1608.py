#include <iostream>
using namespace std;
void main()
{
	freopen("A-small-attempt2.in","r",stdin);
	freopen("A-small-attempt2.out","w",stdout);
	double s[200];       //ji
	double m[50][200];     //mi
	int T = 0;
	cin>>T;
	for(int i=1;i<=T;i++)
	{
		int N = 0;
		cin>>N;
		for(int j=0;j<N;j++)
		{
			//s[j]=0;
			cin>>s[j];
		}
		double X = 0.000000;
		for(int j=0;j<N;j++)
		{
			X = X+s[j];
		}
		double t=0;
		int n=N;
		for(int j=0;j<N;j++)
		{
			m[i][j]=(double)(2*X*100-s[j]*N*100)/(N*X);
			if(m[i][j]<0)
			{
				n=n-1;
				s[j]=-1;
				t=t+m[i][j];
			}
		}
	    t=t/n;
		for(int j=0;j<N;j++)
		{
			
	        m[i][j]=m[i][j]+t;
			if(s[j]<0)
			{
				m[i][j]=0;
			}
		}
		
		/*for(int k=0;k<N;k++)
		{
			m[i][k]=m[i][k]+t;
		}*/
		
		cout<<"Case #"<<i<<": ";
		for(int j=0;j<N;j++)
		{
			printf("%.6lf ",m[i][j]);
		}
		cout<<endl;
	}
	
}
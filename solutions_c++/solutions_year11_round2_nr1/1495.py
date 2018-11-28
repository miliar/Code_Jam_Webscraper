# include <iostream>
# include <string>
using namespace std;

int main()
{
	freopen("A-large.in","r",stdin);
	freopen("out.txt","w",stdout);
	int cas,t,N;
	string bd [101];
	double wp[101],owp[101],oowp[101],win[101],play[101];
	cin>>t;
	for(cas=1;cas<=t;cas++)
	{
		cin>>N;
		for(int i=0;i<N;i++)
		{
			cin>>bd[i];
			wp[i]=0;
			owp[i]=0;
			oowp[i]=0;
			
		}

		for(int i=0;i<N;i++)
		{
			double w=0,m=0;
			for(int j=0;j<bd[i].size();j++)
			{
				if(bd[i][j] == '.')	continue;
				if(bd[i][j] == '1') w++;
				m++;
			}
			wp[i] = w/m;
			win[i] = w;
			play[i] = m;
		}
		

		for(int i=0;i<N;i++)
		{
			double m=0,cnt=0;
			for(int j=0;j<bd[i].size();j++)
			{
				if(bd[i][j] == '.')	continue;
				if(bd[i][j] == '0')
				{
					cnt+= (win[j]-1)/(play[j]-1);
				}
				else
				{
					cnt+= (win[j])/(play[j]-1);
				}
				m++;
			}
			owp[i] = cnt/m;
		}

		for(int i=0;i<N;i++)
		{
			double m=0,cnt=0;
			for(int j=0;j<bd[i].size();j++)
			{
				if(bd[i][j] == '.')	continue;
				cnt+=owp[j];
				m++;
			}
			oowp[i] = cnt/m;
		}
		printf("Case #%d:\n",cas);
		for(int i=0;i<N;i++)
		{
			printf("%lf\n",0.25*wp[i]+0.5*owp[i]+0.25*oowp[i]);
		}
	}

	return 0;
}
#include <iostream>
#include <algorithm>
#include <string>
#include <vector>
#include <set>
#include <cstdio>
#include <climits>
#include <cmath>
using namespace std;

int main()
{
	int T; cin>>T;
	for(int ds=1;ds<=T;ds++)
	{
		int N; cin>>N;
		
		char field[101][101]={0};
		for(int n=0;n<N;n++)
		for(int i=0;i<N;i++)
			cin>>field[n][i];
		
		vector<int> total(N,0);
		vector<int> win(N,0);
		
		vector<double> WP(N,0.0);
		vector<double> OWP(N,0.0);
		vector<double> OOWP(N,0.0);
		
		for(int n=0;n<N;n++)
		{
			for(int i=0;i<N;i++)
			{
				switch(field[n][i])
				{
				case '.': break;
				case '0': total[n]++; break;
				case '1': total[n]++; win[n]++; break;
				}
			}
			WP[n]=(double)win[n]/total[n];
		}
		
		for(int n=0;n<N;n++)
		{
			double owpsum=0.0;
			for(int i=0;i<N;i++)
			{
				if(field[n][i]=='.')
					continue;
				
				switch(field[i][n])
				{
				case '0': owpsum+=(double)(win[i]-0)/(total[i]-1); break;
				case '1': owpsum+=(double)(win[i]-1)/(total[i]-1); break;
				}
			}
			OWP[n]=(double)owpsum/total[n];
		}
		
		for(int n=0;n<N;n++)
		{
			double oowpsum=0.0;
			for(int i=0;i<N;i++)
			{
				if(field[n][i]=='.')
					continue;
				
				switch(field[i][n])
				{
				case '0': oowpsum+=OWP[i]; break;
				case '1': oowpsum+=OWP[i]; break;
				}
			}
			OOWP[n]=(double)oowpsum/total[n];
		}
		
		printf("Case #%d:\n",ds);
		for(int n=0;n<N;n++)
		{
			double RPI=0.25*WP[n]+0.50*OWP[n]+0.25*OOWP[n];
			fprintf(stderr,"%3d: WP=%f OWP=%f OOWP=%f : %lf\n",n,WP[n],OWP[n],OOWP[n],RPI);
			printf("%.9lf\n",RPI);
		}
	}
	return 0;
}

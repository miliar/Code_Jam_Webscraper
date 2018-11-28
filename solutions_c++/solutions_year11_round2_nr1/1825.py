#include <cstdio>
#include <iostream>
#include <cstring>

using namespace std;

int TC = 1, T, NC = 1, N;
int vs[100][100],sum[100];
double wp[100], oowp[100], rpi[100];
double owp[100][100], owpf[100],tmp[100];

int main ()
{
	freopen("A-large.in", "r", stdin);
	freopen("A-large.out", "w", stdout);
	for (cin>>T, TC = 1; TC <= T; TC++)
    {
		cout<<"Case #"<<TC<<": "<<endl;
		int k = 0;
		char ch;
		memset(vs, 0 , 10000*sizeof(int));
		memset(sum, 0 , 100*sizeof(int));
		memset(wp, 0 , 100*sizeof(double));
		memset(owpf, 0 , 100*sizeof(double));
		memset(oowp, 0 , 100*sizeof(double));
		memset(rpi, 0 , 100*sizeof(double));
		memset(owp, 0 , 10000*sizeof(double));
		for (cin>>N, NC = 0; NC < N; NC++)
		{

			int total = 0, win = 0;
			for (k = 0; k<N; k++)
			{
					cin>>ch;
					vs[NC][k] = ch - '0';
					if (ch == '0')
					{	total++; sum[NC]++;}
					else if (ch == '1')
					{	total++; win++; sum[NC]++;}
			}
	/*		for (k = 0; k<N; k++)		//delete matches again k th, NC's win rate
			{
				if (vs[NC][k] == 0)
					owp[NC][k] = (win)/(total - 1.0);
				else if (vs[NC][k] == 1)
					owp[NC][k] = (win-1.0)/(total);
			}*/
			wp[NC] = 1.0*win/total;			
		}
		for (k = 0; k<N; k++)
		{
			memset(tmp, 0 , 100*sizeof(double));

			for (int i = 0; i < N; i++)
			{
				int total = 0, win = 0;
				if (i!=k)
					for (int j = 0; j < N; j++)
					{
						if (j!=k)
						{
							if (vs[i][j] == 0)
							total++;
							else if (vs[i][j] == 1)
							{	total++; win++;}
						}			
					}
				tmp[i] = win*1.0/total;
			}
			for (int i = 0; i < N; i++)
			{
				if (i!=k && vs[k][i] >= 0)
				owpf[k]+= tmp[i];
			}
			owpf[k] /= (sum[k]*1.0);
		}
		for (k = 0; k<N; k++)
		{	oowp[k] = 0	;
			for (NC = 0; NC < N; NC++)
			{
				if (k != NC && vs[NC][k] >= 0)
					oowp[k] += owpf[NC];
			}
			oowp[k] = oowp[k]/ (sum[k]*1.0);
		}
		for (k = 0; k<N; k++)
		{
			rpi[k] = 0.25 * wp[k] + 0.50 * owpf[k] + 0.25 * oowp[k];
			cout<<rpi[k]<<endl;
		}
    }
	fclose(stdin);
	fclose(stdout);
    return 0;
}



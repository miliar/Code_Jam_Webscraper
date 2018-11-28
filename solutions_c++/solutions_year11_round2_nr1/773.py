#include <iostream>
#include <cmath>
#include <vector>
using namespace std;

#define INP_FILE "A-large.in"
#define OUT_FILE "A-large.in.txt"

int main()
{
	freopen( INP_FILE , "r" , stdin );
	freopen( OUT_FILE , "w" , stdout );
	int tstCnt;
	cin>>tstCnt;

	int win[110],game[110];
	char data[110][110];
	double wp[110],owp[110],oowp[110];

	for(int tst=1;tst<=tstCnt;tst++)
	{
		int n;
		char c;
		cin>>n;

		for(int i=0;i<n;i++)
		{
			win[i]=game[i]=0;
			for(int j=0;j<n;j++)
			{
				cin>>data[i][j];
				switch (data[i][j])
				{
					case '.':break;
					case '1': win[i]++; game[i]++; break;
					case '0': game[i]++; break;
				}
			}
		}

		int t; 
		for(int i=0;i<n;i++)
		{
			wp[i]=((double)win[i])/game[i];
			owp[i]=0;
			 t=0;
			for(int j=0;j<n;j++)
				if ( data[i][j]!='.')
				{
					t++;
					if ( data[i][j]=='1')
						owp[i] +=((double)win[j])/(game[j]-1);
					else
						owp[i] +=((double)win[j]-1)/(game[j]-1);
				}
			owp[i] = owp[i]/t;
		}
		for(int i=0;i<n;i++)
		{
			oowp[i]=0;
			 t=0;
			for(int j=0;j<n;j++)
				if ( data[i][j]!='.')
				{ 
					oowp[i] +=owp[j]; 
					t++;
				}
			oowp[i] = oowp[i]/t;
		}
		printf("Case #%d:\n",tst);
		for(int i=0;i<n;i++)
		{
			printf("%f\n",0.25 * wp[i] + 0.50 * owp[i] + 0.25 * oowp[i]);
		}
		

	}
	return 0;
}
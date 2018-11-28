#include <iostream>

using namespace std;

int main()
{
//	freopen("m:/input.txt", "rt", stdin);

	int T;
	cin>>T;

	int N;
	char a[100][101];
	double wp[100];
	double owp[100];
	double oowp[100];
	double rpi[100];
	int op[100];

	for(int t=1; t<=T; t++)
	{
		scanf("%d", &N);

		for(int i=0; i<N; i++)
		{
			scanf("%s", a[i]);
		}

		for(int i=0; i<N; i++)		
		{
			wp[i] = 0.0;
			op[i] = 0;
			for(int j=0; j<N; j++)
			{
				if(a[i][j]=='1')wp[i]+=1.0;
				if(a[i][j]!='.')op[i]++;
			}
		}
			
		for(int i=0; i<N; i++)
		{
			owp[i] = 0.0;
			for(int j=0; j<N; j++)
			{
				if(a[i][j]!='.')
				{
					double wpj = (wp[j] - ((a[i][j]=='1')?0:1))/(op[j]-1);
					owp[i] += wpj;
				}
			}
		}

		for(int i=0; i<N; i++)wp[i]/=op[i];

		for(int j=0; j<N; j++)owp[j]/=op[j];

		for(int i=0; i<N; i++)
		{
			oowp[i] = 0.0;
			for(int j=0; j<N; j++)
			{
				if(a[i][j]!='.')oowp[i] += owp[j];
			}
		}

		for(int j=0; j<N; j++)oowp[j]/=op[j];

		for(int i=0; i<N; i++)
		{
			rpi[i] = wp[i]*0.25 + owp[i]*0.5 + oowp[i]*0.25;
		}
	
		printf("Case #%d: \n", t);
		for(int i=0; i<N; i++)
			printf("%lg\n", rpi[i]);
	}


	return 0;
}
#include <iostream>
using namespace std;

char win[100][100];
double WP[100];
double tempWP[100][100];
double OWP[100];
double OOWP[100];
double score[100];

int main()
{
	int T;
	cin >> T;
	for(int i=1;i<=T;i++)
	{
		cout << "Case #" << i << ":" << endl;
		int N;
		cin >> N;
		for(int j=0;j<N;j++)
		{
			for(int k=0;k<N;k++)
			{
				cin >> win[j][k];
			}
		}
		for(int j=0;j<N;j++)
		{
			int num = 0;
			int winc = 0;
			for(int k=0;k<N;k++)
			{
				if(win[j][k]=='1')
				{
					num++;
					winc++;
				}
				else if(win[j][k]=='0')
				{
					num++;
				}
			}
			WP[j] = winc*1.0/num;
			for(int k=0;k<N;k++)
			{
				tempWP[j][k] = -1;
				if(win[j][k]=='1')
				{
					tempWP[j][k] = (winc-1.0)/(num-1.0);
				}
				else if(win[j][k]=='0')
				{
					tempWP[j][k] = winc / (num-1.0);
				}
			}
		}
		for(int j=0;j<N;j++)
		{
			double tempOWP = 0;
			int num = 0;
			for(int k=0;k<N;k++)
			{
				if(win[j][k]=='1'||win[j][k]=='0')
				{
					tempOWP += tempWP[k][j];
					num++;
				}
			}
			OWP[j] = tempOWP / num;
		}
		for(int j=0;j<N;j++)
		{
			double tempOOWP = 0;
			int num = 0;
			for(int k=0;k<N;k++)
			{
				if(win[j][k]=='1'||win[j][k]=='0')
				{
					tempOOWP += OWP[k];
					num++;
				}
			}
			OOWP[j] = tempOOWP / num;
		}
		for(int j=0;j<N;j++)
		{
			score[j] = 0.25 * WP[j] + 0.5 * OWP[j] + 0.25 * OOWP[j];
			printf("%.7lf\n",score[j]);
		}
	}
}

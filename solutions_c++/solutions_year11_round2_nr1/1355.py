#include <iostream>
#include <fstream>

using namespace std;

int main()
{
	int cases;
	ofstream fout;
	fout.open("output.txt");
	cin>>cases;
	char c[101][101];
	int WPn[101];
	int WPd[101];
	double OWP[101];
	double OOWP[101];
	for (int h=0;h<cases;h++)
	{
		int teams;
		cin>>teams;
		for (int i=0;i<teams;i++) 
		{
			cin>>c[i];
			WPn[i]=WPd[i]=0;
			OWP[i]=0;
			OOWP[i]=0;
		}

		//Calculate WP for each team;
		for (int i=0;i<teams;i++)
		{
			for (int j=0;j<teams;j++)
			{
				if (c[i][j]=='1')
				{
					WPn[i]++;
					WPd[i]++;
				}
				if (c[i][j]=='0')
				{
					WPd[i]++;
				}
			}
		}

		//Calculate OWP for each team
		for (int i=0;i<teams;i++)
		{
			int cnt=0;
			for (int j=0;j<teams;j++)
			{
				if (c[i][j]=='1')
				{
					OWP[i]+=double(WPn[j])/double(WPd[j]-1);
					cnt++;
				}
				if (c[i][j]=='0')
				{
					OWP[i]+=double(WPn[j]-1)/double(WPd[j]-1);
					cnt++;
				}
			}
			OWP[i]=OWP[i]/double(cnt);
		}

		//Calculate OOWP for eact team

		for (int i=0;i<teams;i++)
		{
			int cnt=0;
			for (int j=0;j<teams;j++)
			{
				if (c[i][j]!='.')
				{
					OOWP[i]+=OWP[j];
					cnt++;
				}
			}
			OOWP[i]=OOWP[i]/double(cnt);
		}

		fout<<"Case #"<<h+1<<":"<<endl;
		fout.precision(9);
		for (int i=0;i<teams;i++) fout<<(double(WPn[i])/double(WPd[i])+OWP[i]*2+OOWP[i])/4.<<endl;
	}
	return 0;
}
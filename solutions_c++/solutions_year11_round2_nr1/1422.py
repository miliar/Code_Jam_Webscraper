#include <iostream>
#include <fstream>
#include <string>
#include <cstring>

using namespace std;

int T,N;
double WP[110][2],OWP[110],OOWP[110];
string s[110];

int main()
{
	int i,j,k,win,lose;
	double result;
	ifstream cin("A-large.in");
	ofstream cout("A-large.out");
	cin >> T;
	for (i=0;i<T;i++)
	{
		memset(WP,0,sizeof(WP));
		memset(OWP,0,sizeof(OWP));
		memset(OOWP,0,sizeof(OOWP));
		cin >> N;
		for (j=0;j<N;j++)
		{
			cin >> s[j];
			win=0;
			lose=0;
			for (k=0;k<N;k++)
			{
				if (s[j][k]=='0')
					lose++;
				else if (s[j][k]=='1')
					win++;
			}
			WP[j][0]=win;
			WP[j][1]=win+lose;
		}
		for (j=0;j<N;j++)
		{
			for (k=0;k<N;k++)
			{
				if (s[j][k]=='.')
					continue;
				if (s[j][k]=='1')
					OWP[j]+=double(WP[k][0])/(WP[k][1]-1);
				else
					OWP[j]+=double(WP[k][0]-1)/(WP[k][1]-1);
			}
			OWP[j]/=WP[j][1];
		}
		for (j=0;j<N;j++)
		{
			for (k=0;k<N;k++)
			{
				if (s[j][k]=='.')
					continue;
				else
				{
					OOWP[j]+=OWP[k];
				}
			}
			OOWP[j]/=WP[j][1];
		}/**/

		cout << "Case #" << i+1 << ":" << endl;
		cout.precision(12);
		for (j=0;j<N;j++)
		{
			result=0.25*WP[j][0]/WP[j][1]+0.5*OWP[j]+0.25*OOWP[j];
			cout << result << endl;
		}
	}
	return 0;
}
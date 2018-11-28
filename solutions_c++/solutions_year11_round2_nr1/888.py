#include<iostream>
int t,n;
double wp[110];
double owp[110];
double oowp[110];
double win[110], total[110];
char s[110][110];
double ans[110];
using namespace std;
int main()
{
	freopen("a.in","r",stdin);
	freopen("a.out","w",stdout);
	cin >> t;
	for (int l = 1 ; l <= t; ++l)
	{
		cin >> n;
		memset(wp, 0 ,sizeof(wp));
		memset(owp, 0 , sizeof(owp));
		memset(oowp, 0 , sizeof(oowp));
		memset(win, 0 , sizeof(win));
		memset(total, 0 , sizeof(total));
		for (int i = 0 ; i < n; ++i)
		{
			scanf("%s",s[i]);
			for (int j = 0 ; j < n ; ++j)
			{
				if (s[i][j] == '.')
				{
					continue;
				}
				if (s[i][j] == '1')
				{
					win[i] = win[i]+1;
				}
				total[i] += 1;
			}
			wp[i] = win[i] / total[i];
			
		}
		double temp;
		double team;
		for (int i = 0; i < n ; ++i)
		{
			temp = 0;
			team = 0;
			for (int j = 0 ; j < n; ++j)
			{
				if (s[i][j] != '.')
				{
					if (s[i][j] == '0')
					{
						temp += (win[j] - 1) / (total[j] -1);
					}
					else
					{
						temp += win[j] / (total[j] - 1);
					}
					team += 1;
				}	
			}
			owp[i] = temp / team;
		
			
		}
		for (int i = 0; i < n ; ++i)
		{
			temp = 0;
			team = 0;
			for (int j = 0 ; j < n; ++j)
			{
				if (s[i][j] != '.')
				{
					temp += owp[j];
					team += 1;
				}	
			}
			oowp[i] = temp  / team;
		}
		cout << "Case #"<<l<<":"<<endl;
		for (int i = 0 ; i < n ; ++i)
		{
			ans[i] = 0.25*wp[i] + 0.5*owp[i] + 0.25*oowp[i];
			printf("%.8lf\n",ans[i]);
		}
		
	}
}

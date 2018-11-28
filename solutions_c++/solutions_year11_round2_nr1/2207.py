#include "../common.h"

using namespace std;
int N,T;
char s[200][200];
double r[200];
double wp[200];
double wp1[200][200];
double owp[200];
double oowp[200];

int main()
{
	FILE *fp = NULL;
	fp = freopen("A-large.in","r",stdin);
	fp = freopen("a1.out","w",stdout);
	int testcase;
	cin>>T;
	for (testcase = 1;testcase<=T;testcase++)
	{
		cin>>N;
		memset(s,0,sizeof s);
		memset(r,0,sizeof r);
		memset(wp,0,sizeof wp);
		memset(wp1,0,sizeof wp1);
		memset(owp,0,sizeof owp);
		memset(oowp,0,sizeof oowp);
		for (int i=0;i<N;i++)
		{
			cin>>s[i];
		}
		for (int i =0;i<N;i++)
		{
			int w =0,l = 0;
			for (int j= 0;j<N;j++)
			{
				if(s[i][j] == '1')w++;
				if(s[i][j] == '0')l++;
			}
			wp[i] = w;
			wp[i] /= (w+l);
			for (int j=0;j<N;j++)
			{
				if(s[i][j] == '1') {wp1[i][j] = w-1;wp1[i][j] /= (w+l-1);}
				if (s[i][j] == '0'){wp1[i][j] = w;wp1[i][j] /= (w+l-1);}
			}
		}
		for (int i = 0;i<N;i++)
		{
			int t = 0;
			for (int j=0;j<N;j++)
			{
				if (s[i][j] == '1' || s[i][j] == '0')
				{
					owp[i] += wp1[j][i]; 
					t++;
				}
			}
			owp[i] /= t;
		}
		for (int i = 0;i<N;i++)
		{
			int t =0;
			for (int j=0;j<N;j++)
			{
				if (s[i][j] == '1' || s[i][j] == '0')
				{
					oowp[i] += owp[j]; 
					t++;
				}
			}
			oowp[i] /= t;
		}
		for (int i =0;i<N;i++)
		{
			r[i] = 0.25*wp[i] + 0.50*owp[i]+0.25*oowp[i];
		}
		cout<<"Case #"<<testcase<<":"<<endl;
		for (int i=0;i<N;i++)
		{
		//	cout<<r[i]<<endl;
			printf("%.8f\r\n",r[i]);
		}
	}
	


	return 0;
}
#include "iostream"
#include "string.h"
#include "math.h"
#include "algorithm"
#include "stdio.h"
using namespace std;


int n;
char play[110][110];
double res[110];
double wp[110],owp[110],oowp[110];

void input()
{
	cin>>n;
	for(int i=0;i<n;++i)
	{
		res[i]=0;
		wp[i]=owp[i]=oowp[i]=0;
		for(int j=0;j<n;++j)
		{
			cin>>play[i][j];
		}
	}
}
void solve()
{
	input();
	for(int i=0;i<n;++i)
	{
		int win=0,total=0;
		for(int j=0;j<n;++j)
		{
			if(play[i][j]=='1')
				win++;
			if(play[i][j]!='.')
				total++;
		}
		wp[i]=double(win)/double(total);
	}

	for(int i=0;i<n;++i)
	{
		int opn=0;
		owp[i]=0;
		for(int j=0;j<n;++j)
		{
			if(play[i][j]!='.')
			{
				opn++;
				int win=0,tot=0;
				for(int k=0;k<n;++k)
				{
					if(k==i)
						continue;
					if(play[j][k]=='1')
						win++;
					if(play[j][k]!='.')
						tot++;
				}
				owp[i]+=double(win)/double(tot);
			}
		}
		owp[i]/=double(opn);
	}

	for(int i=0;i<n;++i)
	{
		int opn=0;
		oowp[i]=0;
		for(int j=0;j<n;++j)
		{
			if(play[i][j]!='.')
			{
				opn++;
				
				oowp[i]+=owp[j];
			}
		}
		oowp[i]/=double(opn);
	}

	cout<<endl;

	for(int i=0;i<n;++i)
	{
		printf("%.14f\n",0.25*wp[i]+0.5*owp[i]+0.25*oowp[i]);
	}
}

int main()
{
	freopen("a.txt","r",stdin);
	freopen("a.out.txt","w",stdout);
	int cs;
	cin>>cs;

	for(int i=1;i<=cs;++i)
	{
		cout<<"Case #"<<i<<": ";
		solve();
	}
}
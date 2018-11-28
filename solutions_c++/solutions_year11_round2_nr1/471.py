#include <iostream>
#include <iomanip>
using namespace std;

#define MAXN 100

int T, N;
char g[MAXN][MAXN];
int W[MAXN], P[MAXN];
double WP[MAXN], OWP[MAXN], OOWP[MAXN];

void read_case()
{
	cin>>N;
	for (int i=0; i<N; i++)
		for (int j=0; j<N; j++)
			cin>>g[i][j];
}

void solve()
{
	for (int i=0; i<N; i++)
	{
		W[i] = 0;
		P[i] = 0;
		WP[i] = 0.0;
		OWP[i] = 0.0;
		OOWP[i] = 0.0;
	}
	
	for (int i=0; i<N; i++)
		for (int j=0; j<N; j++)
		{
			W[i] += g[i][j]=='1';
			P[i] += g[i][j]!='.';
		}
	
//	cout<<"WP : "<<endl;
	for (int i=0; i<N; i++)
	{
		WP[i] = (1.0*W[i])/P[i];
//		cout<<WP[i]<<endl;
	}
		
	//cout<<"OWP : "<<endl;
	for (int i=0; i<N; i++)
	{
		int opp(0);
		for (int j=0; j<N; j++)
			if (g[i][j]!='.')
			{
				OWP[i] += (1.0*(W[j]-(g[i][j]=='0'))) / (P[j]-1);
				opp++;
			}
		OWP[i] /= opp;
	//	cout<<OWP[i]<<endl;
	}
	
	//cout<<"OOWP :"<<endl;
	for (int i=0; i<N; i++)
	{
		int opp(0);
		for (int j=0; j<N; j++)
			if (g[i][j]!='.')
			{
				OOWP[i] += OWP[j];
				opp++;
			}
		OOWP[i] /= opp;
	//	cout<<OOWP[i]<<endl;
	}
}
	

int main()
{
	cin>>T;
	for (int i=0; i<T; i++)
	{
		read_case();
		solve();
		cout<<"Case #"<<i+1<<":"<<endl;
		for (int i=0; i<N; i++)
			cout<<setprecision(10)<<WP[i]/4+OWP[i]/2+OOWP[i]/4<<endl;
	}
	return 0;
}

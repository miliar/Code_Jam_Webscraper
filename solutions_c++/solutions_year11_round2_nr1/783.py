#include <iostream>
#define MAX 110

using namespace std;
typedef long double LD;

int T[MAX][MAX];
int Won[MAX],Played[MAX];
LD WP[MAX],OWP[MAX],OOWP[MAX],RPI[MAX];

int main()
{
	ios_base::sync_with_stdio(0);

	int Testow; cin>>Testow;
	for (int test=1; test<=Testow; ++test)
	{
		int N; cin>>N;
		for (int i=1; i<=N; ++i)
		{
			Won[i]=Played[i]=0;
			for (int j=1; j<=N; ++j)
			{
				char zn; cin>>zn;
				if (zn!='.') ++Played[i];
				if (zn=='1')
				{
					++Won[i];
					T[i][j]=1;
				}
				else if (zn=='0') T[i][j]=-1;
				else T[i][j]=0;
			}	
		}

		for (int a=1; a<=N; ++a)
		{
			WP[a]=Won[a];
			WP[a]/=Played[a];

			int oponents=0;

			OWP[a]=0;
			for (int b=1; b<=N; ++b)
			{
				if (b==a) continue;
				if (T[a][b]==0) continue;

				++oponents;

				LD w=Won[b];
				int numPl=Played[b];
				if (T[b][a]!=0) --numPl;
				if (T[b][a]==1) --w;
				
				OWP[a]+=w/numPl;
			}
			OWP[a]/=oponents;
		}

		for (int a=1; a<=N; ++a)
		{
			OOWP[a]=0;
			int opon=0;
			for (int b=1; b<=N; ++b)
			{
				if (b==a) continue;
				if (T[a][b]==0) continue;
				OOWP[a]+=OWP[b];
				++opon;
			}
			OOWP[a]/=opon;

			RPI[a]=0.25*WP[a]+0.5*OWP[a]+0.25*OOWP[a];
			
		}
		cout.setf(ios::fixed);
		cout.precision(12);

		cout<<"Case #"<<test<<":"<<endl;
		for (int a=1; a<=N; ++a) cout<<RPI[a]<<endl;
	}

	return 0;
}
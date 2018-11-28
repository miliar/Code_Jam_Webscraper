#include <stdio.h>
#include <iostream>
#include <string>
#include <vector>
using namespace std;
vector<int> G[1001];
int tab[101][101];
double OWP_A[101];
double ans_m[101];
int main()
{
	int Z,N;
	scanf("%d",&Z);
	for(int r = 0; r < Z; r++)
	{
		scanf("%d",&N);
		string a;
	
		for(int i = 1; i <= N; i++) for(int j = 1; j <= N; j++) tab[i][j] = -1;
		for(int i = 0; i <= N; i++)
		{
			 OWP_A[i] = ans_m[i] = 0;
			G[i].clear();
		}		
		for(int i = 0; i < N; i++)
		{	
			cin>>a;
			for(int j = 0; j < N; j++)
			{
				if(a[j] != '.') G[i + 1].push_back(j + 1);
				if(a[j] == '1') tab[i + 1][j + 1] = 1;
				if(a[j] == '0') tab[i + 1][j + 1] = 0;
			}
		}	
		for(int i = 1; i <= N; i++)
		{
			double ans = 0;
			int licz = 0;
			int v = 0;
			for(int j = 1; j <= N; j++)
			{

				if(tab[i][j] == 1) v++;
				if(tab[i][j] != - 1) licz++;
			}
			double av = 0;
			
			av = v;
			if(licz != 0) av /= licz;
		
			ans += (av * 0.25);
			
			double OWP = 0;
			for(int j = 0; j < G[i].size(); j++)
			{
					licz = v = 0;
					int neigh = G[i][j];
					for(int l = 1; l <= N; l++)
					{
						if(l != i)
						{
							if(tab[neigh][l] == 1) v++;
							if(tab[neigh][l] != -1) licz++;
						}
					}
					av = 0;
					av = v;
					if(licz != 0) av /= licz;
					OWP += av;
			}
			OWP /=  G[i].size();
			
			ans +=	(0.5 * OWP);
			
			OWP_A[i] = OWP;
			ans_m[i] = ans;
		
		}
		cout<<"Case #"<<r + 1<<":"<<endl;
		for(int i = 1; i <= N; i++)
		{
			double av_owp = 0;
			for(int j = 0; j < G[i].size(); j++)
			{
				av_owp += OWP_A[G[i][j]];
			}
			av_owp /= G[i].size();
			
			ans_m[i] += av_owp * 0.25;
			printf("%.7lf\n",ans_m[i]);
		}
	}	
	return 0;
}

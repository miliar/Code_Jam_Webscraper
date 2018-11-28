#include <iostream>
#include <string>
#include <vector>
#include <set>
#include <stdio.h>
using namespace std;

int main()
{
  int T; cin >> T;
	int num_case = 1;
	while(T--)
	{
	  int N; cin >> N;
		vector<string> games(N);
		for(int i=0;i<N;i++){string s; cin >> s; games[i] = s;}
		vector<double> wins(N,0), loses(N,0);
		vector<double> total(N,0);
		vector<set<int> > opponents(N);
		for(int i=0;i<N;i++){set<int> temp; opponents[i] = temp;}
		for(int i=0;i<N;i++)
		{
			for(int j=0;j<N;j++)
			{
				if(games[i][j] == '1') {wins[i]++; total[i]++; opponents[i].insert(j);}
				if(games[i][j] == '0') {loses[i]++; total[i]++; opponents[i].insert(j);}
			}
		}
		vector<double> WP(N);
		for(int i=0;i<N;i++) WP[i] = wins[i]/total[i];
		
		vector<double> OWP(N,0);
		for(int i=0;i<N;i++)
		{
		  for(set<int>::iterator it = opponents[i].begin(); it != opponents[i].end(); it++)
			{
			  if(games[i][*it] == '1') OWP[i] += wins[*it]/(total[*it]-1);
				if(games[i][*it] == '0') OWP[i] += (wins[*it]-1) / (total[*it] -1);
			}
			OWP[i] /= opponents[i].size();
		}
		
		vector<double> OOWP(N,0);
		for(int i=0;i<N;i++)
		{
		  for(set<int>::iterator it = opponents[i].begin(); it != opponents[i].end();it++)
			{
			  OOWP[i] += OWP[*it]; 
			}
			OOWP[i] /= opponents[i].size();
		}
		
		vector<double> RPI(N);
		for(int i=0;i<N;i++) RPI[i] = 0.25 * WP[i] + 0.50 * OWP[i] + 0.25 * OOWP[i];
		cout << "Case #" << num_case << ": " << endl;
		for(int i=0;i<N;i++) printf("%.12f\n", RPI[i]); //cout << RPI[i] << endl;
	
		num_case++;
	}

  return 0;
}

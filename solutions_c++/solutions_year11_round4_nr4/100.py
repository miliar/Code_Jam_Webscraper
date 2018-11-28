#include <iostream>
#include <cmath>
#include <cstring>
#include <fstream>
#include <cstdlib>
#include <set>
#include <map>
#include <vector>
#include <cstdio>
#include <algorithm>
#include <deque>

using namespace std;

#define MSG(a) cout << #a << " = " << a << endl;
#define FOR(a,start,end) for(int a = int(start); a < int(end); a++)
#define PB push_back

const double PI = 3.14159265358979;
const double EPS = 1e-12;

bool G[401][401];
vector<int> V[401];

int dist[401];

int dpMIN[401][401];

int main()
{
	ifstream fin("D-large.in");
	ofstream fout("D-large.out");
	
	int T;
	fin >> T;
	for(int ta = 0; ta < T; ta++)
	{
		fout << "Case #" << ta+1 << ": ";
		memset(G,0,sizeof G);
		int N;
		fin >> N;
		FOR(i,0,N)
			V[i].clear();
		
		int M;
		fin >> M;
		FOR(i,0,M)
		{
			string s;
			fin >> s;
			int k = atoi(s.substr(0,s.find(',')).c_str());
			int l = atoi(s.substr(s.find(',')+1).c_str());
			G[k][l] = G[l][k] = 1;
			V[k].PB(l);
			V[l].PB(k);
		}
		
		MSG(G[0][1]);
		
		FOR(i,0,N)
			sort(V[i].begin(),V[i].end());
	
		FOR(i,0,N)
			dist[i] = 999999;
		deque<int> Q;
		Q.PB(0);
		dist[0] = 0;
		while(Q.empty() == 0)
		{
			int k = Q[0];
			Q.pop_front();
			FOR(t,0,V[k].size())
			if(dist[V[k][t]] == 999999)
			{
				dist[V[k][t]] = dist[k]+1;
				Q.PB(V[k][t]);
			}
		}
		
		MSG(dist[1]);
		fout << dist[1] - 1 << " ";
		
		FOR(i,0,401)
		FOR(j,0,401)
			dpMIN[i][j] = -1;
		
		FOR(i,0,N)
		if(dist[i] == 1)
			dpMIN[i][0] = 1;
				
		vector<int> nodesByDist[N+1];
		
		FOR(i,0,N)
		if(dist[i] < 999999)
			nodesByDist[dist[i]].PB(i);
			
		FOR(i,2,dist[1]+1)
		FOR(s,0,nodesByDist[i].size())
		{
			int currNode = nodesByDist[i][s];
			FOR(k,0,nodesByDist[i-1].size())
			if(G[nodesByDist[i-1][k]][currNode])
			FOR(l,0,nodesByDist[i-2].size())
			if(G[nodesByDist[i-2][l]][nodesByDist[i-1][k]])
			{				
				int prevNode = nodesByDist[i-1][k];
				int prevprevNode = nodesByDist[i-2][l];
				int aboveMe = dpMIN[prevNode][prevprevNode];
				
				int targetDist = dist[prevNode];
				
				//add aboveMe to prevprevNode forward connections, prevNode same-level connections, and currNode prev-level connections
				set<int> S;
				FOR(m,0,V[prevprevNode].size())
					if(dist[V[prevprevNode][m]] == targetDist)
						S.insert(V[prevprevNode][m]);
				FOR(m,0,V[prevNode].size())
					if(dist[V[prevNode][m]] == targetDist)
						S.insert(V[prevNode][m]);
				if(currNode != 1)
				{
					FOR(m,0,V[currNode].size())
						if(dist[V[currNode][m]] == targetDist)
							S.insert(V[currNode][m]);	
				}
				dpMIN[currNode][prevNode] = max(dpMIN[currNode][prevNode], aboveMe + (int)S.size());
			}
		}
		
	//	FOR(i,0,N)
	//	FOR(j,0,N)
	//		if(dpMIN[i][j] != 999999)
	//			cout << i << " " << j << " " << dpMIN[i][j] << endl;
				
		int ANS = -1;
		FOR(i,0,N)
		if(G[i][1] && dist[i] == dist[1] - 1)
		{
			//what does i threaten in the dist[1]-row? This includes '1'.
			int prevNode = i;
			int CNT = 0;
			FOR(m,0,V[prevNode].size())
				if(dist[V[prevNode][m]] == dist[1])
					CNT++;
				
			ANS = max(ANS, dpMIN[1][i] + CNT - dist[1]);
		}
		fout << ANS << endl;	

	}
	return 0;
}







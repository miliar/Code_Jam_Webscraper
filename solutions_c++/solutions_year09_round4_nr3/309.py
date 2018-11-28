#include <math.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <iostream>
#include <algorithm>
#include <vector>
#include <queue>
#include <map>
#include <sstream>
#include <iomanip>

using namespace std;
#define c first
#define na second.first
#define g second.second
#define INF 1000000

typedef pair<int,vector<vector<int> > > PIV;
typedef pair<int,PIV> PIIV;
	
int main(){
	int Tc;
	cin >> Tc;
	for(int tc=1;tc<=Tc;tc++){
		int N,K;
		cin >> N >> K;
		vector<vector<int> > p(N,vector<int>(K));
		for(int i=0;i<N;i++) for(int j=0;j<K;j++) cin >> p[i][j];

		vector<vector<bool> > C(N,vector<bool>(N,1));
		for(int i=0;i<N;i++) for(int j=0;j<N;j++) if(i!=j){
			for(int k=1;k<K;k++){
				if(p[i][k-1] == p[j][k-1]) C[i][j]=0;
				else if(p[i][k] == p[j][k]) C[i][j]=0;
				else if(p[i][k-1] > p[j][k-1] && p[i][k] < p[j][k]) C[i][j]=0;
				else if(p[i][k-1] < p[j][k-1] && p[i][k] > p[j][k]) C[i][j]=0;
			}
		}


		vector<vector<int> > g0;
		priority_queue<PIIV> pq;
		pq.push(PIIV(0,PIV(0,g0)));
		PIIV a;
		while(!pq.empty()){
			a = pq.top();
			pq.pop();
			vector<vector<int> > vg = a.g;
			int n = a.na;
			if(n == N) break;
			for(int i=0;i<a.g.size();i++){
				bool v=1;
				for(int j=0;j<a.g[i].size();j++) if(C[a.g[i][j]][n] == 0) v = 0;
				if(v){
					a.g[i].push_back(n);
					pq.push(PIIV(a.c,PIV(n+1,a.g)));
					a.g = vg;
				}
			}
			a.g.push_back(vector<int>(1,n));
			pq.push(PIIV(a.c-1,PIV(n+1,a.g)));
		}


		cout << "Case #" << tc << ": " << -a.c << endl;
	}
}

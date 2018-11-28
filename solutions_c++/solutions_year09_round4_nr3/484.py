#include <cstdio>
#include <cstdlib>
#include <iostream>
#include <string>
#include <cstring>
#include <algorithm>
#include <vector>
#include <map>
#include <set>
#include <cmath>
#include <cctype>
#include <stack>
#include <queue>
#include <sstream>

using namespace std;

#define REP(i, T) for(int (i)=0; (i) < T; (i) ++)
#define FOR(i, L, R) for(int (i)=L; (i) < R; (i) ++)
#define PB push_back
#define ERS(v, i) (v).erase((v).begin()+(i))
#define ALL(v) v.begin(), v.end()
#define SORT(v) sort(ALL(v))
#define SZ(v) (int)v.size()
#define FILL(a, i) memset((a), (i), sizeof(a))
#define MAX(a, b) (((a)>(b))?(a):(b))
#define MIN(a, b) (((a)<(b))?(a):(b))

#define vi vector<int>
#define vs vector<string>
#define ll long long
#define pii pair<int, int>
#define pis pair<int, string>
#define psi pair<string, int>

#define INF 999999999
#define PI 3.141592654

int n;
int adj[20][20];
int mem[(1<<20)];

int go(int msk) {
// 	cout << msk << endl;
	if(msk==(1<<n)-1) return 0;
	if(mem[msk] < 0) {
		int aux=INF;
		/*
		for(int m=1; m<(1<<n); m++) {
			int f=1;
			for(int i=0; f && i<n; i++) if((m&(1<<i)) && (msk&(1<<i))) f=0;
			if(!f) continue;
			
			f=1;
			for(int i=0; f && i<n; i++) if(m&(1<<i)) {
				for(int j=i+1; f && j<n; j++) if(m&(1<<j)) {
					if(!adj[i][j]) f=0;
				}
			}
			if(!f) continue;
			
			aux = min(aux, 1+go(msk|m));
			
		}
		
		*/
		
		int id=0;
		while(msk&(1<<id)) id++;
		vi cand;
		int jj=id+1;
		while(jj<n) {
			if((!(msk&(1<<jj))) && adj[id][jj]) cand.PB(jj);
			jj++;
		}
		
		int k=SZ(cand);
		REP(m, (1<<k)) {
			int f=1;
			for(int i=0; i<k && f; i++) {
				if(m&(1<<i)) {
					for(int j=i+1; j<k && f; j++) {
						if(m&(1<<j)) {
							if(!adj[cand[i]][cand[j]]) f=0;
						}
					}
				}
			}
			if(f) {
				int t = msk|(1<<id);
				for(int j=0; j<k; j++) if(m&(1<<j)) t |= (1<<(cand[j]));
				aux = min(aux, 1+go(t));
			}
		}
		
		mem[msk]=aux;
	}
	return mem[msk];
}


int main(void)
{
	int T, i, j, K;
	cin >> T;
	for(int caso=1; caso<=T; caso++) {
		FILL(mem, -1);
		int pr[110][110];
		cin >> n >> K;
		REP(i, n) REP(j, K) {
			cin >> pr[i][j];
		}
		
		REP(i, n) REP(j, n) adj[i][j]=adj[j][i]=1;
		
		REP(i, n) FOR(j, i+1, n) REP(q, K-1) {
			if(pr[i][q] == pr[j][q]) adj[i][j]=adj[j][i]=0;
			if(pr[i][q+1] == pr[j][q+1]) adj[i][j]=adj[j][i]=0;
			if(pr[i][q]>pr[j][q] && pr[i][q+1]<pr[j][q+1]) adj[i][j]=adj[j][i]=0;
			if(pr[i][q]<pr[j][q] && pr[i][q+1]>pr[j][q+1]) adj[i][j]=adj[j][i]=0;
		}
		
		cout << "Case #" << caso <<": " << go(0)<<endl;
		
	}

	return 0;
}

#include <iostream>
#include <sstream>
#include <cstring>
#include <cstdio>
#include <cassert>
#include <vector>
#include <queue>
using namespace std;

vector<vector<int> > words;
#define fu(i,m,n) for(int i=m; i<n; i++)
typedef long long i64;

i64 S[100][100];
i64 W[100][100];
i64 T[100][100];
i64 dist[100][100];
int seen[100][100];

#define doit(r2,c2,t2) if(0) cout << "Moving from " << r << " " << c << " " << t << " to " << r2 << " " << c2 << " " << t2 << endl; \
	if(r2<=2*N-1 && c2<=2*M-1 && r2>=0 && c2>=0 && !seen[r2][c2] && t2<dist[r2][c2]) q.push( make_pair(-t2, make_pair(r2,c2) ) )

int main(void) {
	int TT;
	cin >> TT;
	fu(ct,0,TT) {
		int N,M;
		cin >> N >> M;
		memset(dist,10,sizeof(dist));
		memset(seen,0,sizeof(seen));
		fu(n,0,N) fu(m,0,M) cin >> S[N-n-1][m] >> W[N-n-1][m] >> T[N-n-1][m];
		priority_queue<pair<i64,pair<int,int> > > q;
		q.push(make_pair(-0LL,make_pair(0,0)));
		while(!q.empty()) {
			//cout << "!" << endl;
			i64 t = -q.top().first;
			int r = q.top().second.first;
			int c = q.top().second.second;
			q.pop();
			if(seen[r][c]) continue;
			//cout << r << " " << c << " " << t  << endl;
			seen[r][c]=true;

			if(r==2*N-1 && c==2*M-1) {
				cout << "Case #" << ct+1 << ": " << t << endl;
				break;
			}

			if(r%2==0) {
				i64 dt=S[r/2][c/2]+W[r/2][c/2];
				i64 tt=((t-T[r/2][c/2])%dt + dt)%dt;
				i64 t2 = tt<S[r/2][c/2] ? t : t + S[r/2][c/2]+W[r/2][c/2]-tt;
				int r2=r+1;
				int c2=c;
				t2++;
				doit(r2,c2,t2);
			} else {
				i64 t2 = t + 2;
				int r2 = r+1;
				int c2 = c;
				doit(r2,c2,t2);
			}

			if(r%2==1) {
				i64 dt=S[r/2][c/2]+W[r/2][c/2];
				i64 tt=((t-T[r/2][c/2])%dt + dt)%dt;
				i64 t2 = tt<S[r/2][c/2] ? t : t + S[r/2][c/2]+W[r/2][c/2]-tt;
				int r2=r-1;
				int c2=c;
				t2++;
				doit(r2,c2,t2);
			} else {
				i64 t2 = t + 2;
				int r2 = r-1;
				int c2 = c;
				doit(r2,c2,t2);
			}


			if(c%2==1) {
				i64 dt=S[r/2][c/2]+W[r/2][c/2];
				i64 tt=((t-T[r/2][c/2])%dt + dt)%dt;
				int t2 = tt<S[r/2][c/2] ? t + S[r/2][c/2]-tt : t;
				i64 r2=r;
				int c2=c-1;
				t2++;
				doit(r2,c2,t2);
			} else {
				i64 t2 = t + 2;
				int r2 = r;
				int c2 = c-1;
				doit(r2,c2,t2);
			}

			if(c%2==0) {
				i64 dt=S[r/2][c/2]+W[r/2][c/2];
				i64 tt=((t-T[r/2][c/2])%dt + dt)%dt;
				int t2 = tt<S[r/2][c/2] ? t + S[r/2][c/2]-tt : t;
				i64 r2=r;
				int c2=c+1;
				t2++;
				doit(r2,c2,t2);
			} else {
				i64 t2 = t + 2;
				int r2 = r;
				int c2 = c+1;
				doit(r2,c2,t2);
			}

		}
	}
}

#define _CRT_SECURE_NO_DEPRECATE
#include<vector>
#include<deque>
#include<list>
#include<set>
#include<map>
#include<numeric>
#include<iostream>
#include<sstream>
using namespace std;

#define sz(X) ((int)(X).size())
#define pb push_back
#define mp make_pair
#define X first
#define Y second
#define all(X) (X).begin(),(X).end()
#define FOR(I,S,N) for(int I=(S);I<(N);++I)
#define REP(I,N) FOR(I,0,N)
#define PR(X) cout<<#X<<" = "<<(X)<<" "
#define PRL cout<<endl
#define PRV(X) {cout<<#X<<" = {";int __prv;REP(__prv,sz(X)-1) cout<<(X)[__prv]<<",";cout<<(X).back()<<"}"<<endl;}

typedef long long lint;
typedef vector<int> VI;
typedef pair<int,int> PII;

#define SS stringstream
template<typename T> string tos(T q,int w=0){SS A;A.flags(ios::fixed);A.precision(w);A<<q;string s;A>>s;return s;}
template<typename T> T sto(string s){SS A(s);T t;A>>t;return t;}
template<typename T> vector<T > s2v(string s){SS A(s);vector<T > ans;while(A&&!A.eof()){T t;A>>t;ans.pb(t);}return ans;}
	
// end of pre-inserted code

#define CODE(i, j) ((i)*w + (j))
#define GOOD(i, j) ((i) >= 0 && (i) < h && (j) >= 0 && (j) < w)


int h, w;
int dx[4] = {-1, 0, 0, 1};
int dy[4] = {0, -1, 1, 0};

void decode(int x, int &i, int &j) {
	i = x / w;
	j = x % w;
}

#define DIM 128
int a[DIM][DIM], t[DIM][DIM];
VI e[DIM*DIM], et[DIM*DIM];

int getsink(int i, int j) {
	int mn = 1000000000;
	REP(k, 4) if(GOOD(i+dx[k], j+dy[k])) {
		mn = min(mn, a[i+dx[k]][j+dy[k]]);
	}
	if(mn >= a[i][j]) return -1;
	REP(k, 4) if(GOOD(i+dx[k], j+dy[k])) {
		if(a[i+dx[k]][j+dy[k]] == mn) {
			return k;
		}
	}
	cerr << "wtf?";
	return 100;
}

int main() {
	freopen("B-large.in","r",stdin);
	freopen("B-large.out","w",stdout);

	int tc;
	scanf("%d",&tc);
	REP(ttt, tc) {
		scanf("%d %d",&h,&w);
		REP(i,h) REP(j,w) scanf("%d",&a[i][j]);
		REP(i,w*h) {
			e[i].clear();
			et[i].clear();
		}
		
		REP(i,h) REP(j,w) {
			int k = getsink(i, j);
			if(k != -1) {
				e[CODE(i,j)].pb(CODE(i+dx[k],j+dy[k]));
				et[CODE(i+dx[k],j+dy[k])].pb(CODE(i,j));
			}
		}
		memset(t,-1,sizeof(t));
		int mk = 'a';
		REP(i,h) REP(j,w) if(t[i][j] == -1) {
			int ii = i, jj = j;
			while(sz(e[CODE(ii,jj)]) > 0) {
				int r = e[CODE(ii,jj)][0], i2, j2;
				decode(r, i2, j2);
				ii = i2;
				jj = j2;
			}
			t[ii][jj] = mk;
			deque<int> q;
			q.pb(CODE(ii, jj));
			while(!q.empty()) {
				int u = q.front();
				q.pop_front();
				REP(k, sz(et[u])) {
					int i2, j2;
					decode(et[u][k], i2, j2);
					t[i2][j2] = mk;
					q.pb(et[u][k]);
				}
			}
			++mk;
		}
		printf("Case #%d:\n",ttt+1);
		REP(i,h) {
			REP(j,w) printf(" %c"+(!j),char(t[i][j]));
			printf("\n");
		}
	}

	fclose(stdout);
	return 0;
}
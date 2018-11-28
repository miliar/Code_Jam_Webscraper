#include <iostream>
#include <vector>
#include <cstring>
using namespace std;
int R,C;
char area[1024][1024];

vector<int> conn[1<<20];

int dx[4] = {0,1,1,1};
int dy[4] = {1,0,-1,1};

int type[256];

int vnum(int x, int y, bool a) {
	x = (x+C)%C;
	y = (y+R)%R;
	return a*R*C + y*C + x;
}

const int MN = 1<<20;

const int Z = 1000003;

bool tested[MN][2];
int used[MN];
int T;

int dfs(int n) {
	cout<<"dfs "<<n<<'\n';
	used[n]=T;
	int r=0;
	for(size_t i=0; i<conn[n].size(); ++i) {
		if (tested[n][i]) continue;
		int t = conn[n][i];
		cout<<"tt "<<t<<' '<<used[t]<<' '<<T<<'\n';
		if (used[t]==T) continue;
		used[t]=T;
		bool ok=1;
		for(size_t j=0; j<conn[t].size(); ++j) {
			int a = conn[t][j];
			if (used[a]==T) continue;
			if (!dfs(a)) {
				ok=0;
			}
		}
		r += ok;
	}
	return r;
}

int main()
{
	type['|'] = 0;
	type['-'] = 1;
	type['/'] = 2;
	type['\\'] = 3;
	int t;cin>>t;
	for(int a=1; a<=t; ++a) {
		for(int i=0; i<1<<20; ++i) conn[i].clear();

		cin>>R>>C;
		for(int i=0; i<R; ++i) {
			cin>>area[i];
			for(int j=0; j<C; ++j) {
				int c = area[i][j];
				int num = type[c];
				for(int k=0; k<2; ++k) {
					int z = k==0 ? -1 : 1;
					int x = j + z*dx[num];
					int y = i + z*dy[num];
					int a = vnum(j,i,0);
					int b = vnum(x,y,1);
					conn[a].push_back(b);
					conn[b].push_back(a);
//					cout<<"conn "<<i<<' '<<j<<" - "<<y<<' '<<x<<'\n';
				}
			}
		}
#if 0
		memset(tested,0,sizeof(tested));
		int r=1;
		for(int i=0; i<R*C; ++i) {
			++T;
			cout<<"k "<<i<<'\n';
			if (!tested[i][0] && !tested[i][1]) {
				r *= dfs(i);
				r %= Z;
			} else if (!tested[i][0] || !tested[i][1]) {
				int a = 1+dfs(i);
				r *= a;
			}
			r %= Z;
		}
#else
		int N = R*C;
		int r=0;
		for(int i=0; i<1<<N; ++i) {
			memset(used,0,8*R*C);
			T=1;
			bool ok=1;
			for(int j=0; j<N; ++j) {
				int a = 1&(i>>j);
				int t = conn[j][a];
				if (used[t]==T) ok=0;
				used[conn[j][a]] = T;
			}
			if (ok) ++r;
			r %= Z;
		}
#endif
		cout<<"Case #"<<a<<": "<<r<<'\n';
	}
}

#include <iostream>
#include <vector>
#include <map>
using namespace std;
#define fu(i,m,n) for(int i=m; i<n; i++)
typedef long long i64;

int trav[1003][1003];
const int MOD=10007;

i64 binom(i64 m, i64 n) {
	if(n<0 || n>m) return 0;
	if(m==0) return n==0;
	if(m<0) return 0;
	if(n==0) return 1;
	return binom(m-1,n-1)*m/n;
}

int binomm(int m, int n, int mod) {
	if(n<0 || n>m) return 0;
	if(m==0) return n==0;
	if(m<0) return 0;
	if(n==0) return 1;
	int vals[m+2];
	memset(vals,0,sizeof(vals));
	vals[0]=1;
	fu(i,1,m+1) for(int j=i; j>0; j--)
		vals[j]=(vals[j]+vals[j-1])%mod;
	return vals[n];
}

int binommod(int m, int n, int mod) {
	if(n<0 || n>m) return 0;
	if(m==0) return n==0;
	if(m<0) return 0;
	if(n==0) return 1;
	//cout << "(" << m << " " << n << ")" << endl;
	if(m<mod) {
		return binomm(m,n,mod);
	}
	//cout << "(" << m << " " << n << ")" << endl;
	return (binommod(m%mod, n%mod, mod)*binommod(m/mod, n/mod, mod))%mod;
}

int trave(int r, int c) {
	if(r<0 || c<0) return 0;
	//cout << "[" << r << " " << c << "]" << endl;
	if((2*r-c)%3) return 0;
	if((2*c-r)%3) return 0;
	//cout << "[" << r << " " << c << "]" << endl;
	return binommod((2*r-c)/3+(2*c-r)/3, (2*c-r)/3, MOD);
}

int tab[200][200];

int rock[200][200];

int main(void) {
	//trav[0][0]=1;
	//fu(i,0,10) {
		//fu(j,0,10) cout << binomm(i,j,10) << " ";
		//cout << endl;
	//}
	/*fu(i,0,300) fu(j,0,300) {
		trav[i+2][j+1] = (trav[i][j]+trav[i+2][j+1])%MOD;
		trav[i+1][j+2] = (trav[i][j]+trav[i+1][j+2])%MOD;
	}
	fu(i,0,300) fu(j,0,300) {
		if(trav[i][j]!=trave(i,j)) {
			cout << i << " " << j << " " << trav[i][j] << " " << trave(i,j) << endl;
		}
	}*/
	//cout << trave(1000,1001) << endl;;
	/*fu(i,0,10) {
		fu(j,0,10) cout << trav[i][j] << " ";
		cout << endl;
	}
	cout << endl;
	fu(i,0,10) {
		fu(j,0,10) cout << trave(i,j) << " ";
		cout << endl;
	}
	fu(i,0,30) fu(j,0,30)
		if(binommod(i,j,3)!=binom(i,j)%3) {
			cout << i << " " << j << " " << binommod(i,j,3)
				<< " " << binom(i,j) << endl;
			return 0;
		}
	return 0;*/
	int N;
	cin >> N;
	fu(ts,1,N+1) {
		cout << "Case #" << ts << ": ";
		int H,W,R;
		cin >> H >> W >> R;
		vector<pair<int,int> > rocks;
		memset(rock,0,sizeof(rock));
		memset(trav,0,sizeof(trav));
		trav[0][0]=1;
		fu(i,0,R) {
			int r,c;
			cin >> r >> c;
			rocks.push_back(make_pair(r,c));
			rock[r-1][c-1]=1;
		}
		sort(rocks.begin(),rocks.end());
		fu(i,0,H) fu(j,0,W) if(!rock[i][j]) {
			trav[i+2][j+1] = (trav[i][j]+trav[i+2][j+1])%MOD;
			trav[i+1][j+2] = (trav[i][j]+trav[i+1][j+2])%MOD;
		}
		/*int ret=0;
		fu(i,0,(1<<R)) {
			int pa=1;
			fu(j,0,R) if(i&(1<<j)) pa=-pa;
			int cu=1;
			int r=0, c=0;
			fu(j,0,R) if(i&(1<<j)){
				cu=(cu*trave(rocks[j].first-1-r, rocks[j].second-1-c))%MOD;
				r=rocks[j].first-1;
				c=rocks[j].second-1;
			}
			cu=(cu*trave(H-1-r, W-1-c))%MOD;
			ret = (ret+pa*cu+MOD)%MOD;
		}*/
		cout << trav[H-1][W-1] << endl;
		//cout << ret << " " << trav[H-1][W-1] << endl;
	}
}

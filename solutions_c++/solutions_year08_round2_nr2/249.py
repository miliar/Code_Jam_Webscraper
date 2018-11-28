#include<cstdio>
#include<cstring>
#include<cmath>
#include<vector>

using namespace std;

int par[1001], rank[1001];
void make(int n){
	for (int i = 1 ; i <= n ; ++i) par[i] = i, rank[i] = 0;
}
int find(int x){ return (par[x] == x)?x:(par[x]=find(par[x]));}
int sameset(int x, int y){
	return find(x) == find(y);
}
void U(int x, int y){
	int rx=find(x), ry=find(y);
	if (rank[rx] > rank[ry]){
		par[ry] = rx;
	}else{
		par[rx] = ry;
		rank[ry] += rank[rx]==rank[ry];
	}
}

int main(){
	int T;
	scanf("%d", &T);
	int isprime[10001];
	vector<int> PL;
	memset(isprime, 0, sizeof(isprime));
	for (int i = 2; i < 1001; ++i){
		bool is = 1;
		for (int j = 2; j <= sqrt(i) && is; ++j)
			if (!(i%j)) is  = 0;
		if (is) PL.push_back(i);
	}
	int pn = PL.size();
	for (int cc = 1; cc <= T; ++cc){
		printf("Case #%d: ", cc);
		int A, B, P;
		scanf("%d%d%d", &A, &B, &P);
		int sp = 0;
		make(B);
		for (sp = 0 ; PL[sp] < P && sp < pn; ++sp);
		for (int i = A; i < B; ++i)
			for (int k = i+1; k <= B; ++k)
			for (int j = sp; j < pn; ++j)
				if ((i%PL[j] == 0) && ((k)%PL[j] == 0)){
					//printf("%d %d shares %d\n", i, k, PL[j]);
					if (!sameset(i, k)){
						U(i, k);
						break;
					}
				}
		int gp[B+1], ans=0;
		memset(gp, 0, sizeof(gp));
		for (int i = A; i <= B; ++i){
			//printf("%d: %d\n", i, find(i));
			if (!gp[find(i)]){
				gp[find(i)] = 1;
				ans++;
			}
		}
		printf("%d\n", ans);
	}
}

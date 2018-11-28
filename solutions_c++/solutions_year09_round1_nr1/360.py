#include<cstdio>
#include<cstring>
#include<vector>
#include<map>
#include<algorithm>

using namespace std;

map<int, bool> vis;
map<vector<int>, int> anspool;
int bl[20], bc=0, Lim;
vector<int> L;

void go(int lv){
	if (lv == Lim){
		for (int i = 0 ; i < lv; ++i) fprintf(stderr, "%d ", L[i]);
		if (lv == 9){
			anspool[L] = 11814485;
			return ;
		}
		int x = 2;
		for (int i = 1 ; i < (1<<lv); ++i){
			vector<int> P;
			for (int j = i, k=0 ; j ; j/=2, k++)
				if (j&1) P.push_back(L[k]);
			x = max(x, anspool[P]);
		}
		for (;/*some number*/;x++){
			bool ok = 1;
			for (int i = 0 ; ok && i < lv; ++i){
				int y = x;
				//printf("Try %d (%d)\n", x, bl[i]);
				vis.clear();
				while (1){
					vis[y] = 1;
					int s = 0;
					//printf("%d->", y);
					for (;y; y/=L[i]) s += (y%L[i])*(y%L[i]); 
					//printf("%d\n", s);
					if (s == 1){break;}
					if (vis[s]){ ok = 0; break;}
					y = s;
				}
			}
			if (ok){ anspool[L] = x; break;}
		}
		fprintf(stderr, " --> %d\n", anspool[L]);
	}
	for (int i = lv?(L.back()+1):2; i < 11; ++i){
		L.push_back(i);
		go(lv+1);
		L.pop_back();
	}
}

int main(){
	anspool.clear();
	for (Lim = 1; Lim < 10; ++Lim)
		go(0);
	int T;
	scanf("%d", &T);
	char line[2000];
	gets(line);
	int ca=0;
	while (T--){
		gets(line);
		int dum = 0;
		bool base[20];
		memset(base, 0, sizeof(base));
		while (1){
			int p, k;
			if (sscanf(line+dum, "%d%n", &p, &k)!=1) break;
			dum += k;
			base[p] = 1;
		}
		bc = 0;
		vector<int> F;
		vis.clear();
		for (int i = 1 ; i < 11; ++i)
			if (base[i]) F.push_back(i);
		printf("Case #%d: %d\n", ++ca, anspool[F]);
	}
	return 0;
}

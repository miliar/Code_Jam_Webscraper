#include <cstdio>
#include <set>

using namespace std;

const int MAXN = 2100;
const int MAXM = 2100;

class custumer{
public:
	set<int> malted;
	set<int> unmalted;
	bool sat;
};

custumer c[MAXM];
int ncas=0, t, n, m;
int malted[MAXN];

int main(){
	scanf("%d", &t);
	while (t--){
		scanf("%d", &n);
		scanf("%d", &m);
		for (int i = 0, j; i < m; ++i){
			scanf("%d", &j);
			c[i].malted.clear();
			c[i].unmalted.clear();
			c[i].sat = false;
			for (int a, b; j > 0; --j){
				scanf("%d %d", &a, &b);
				if (b == 1)
					c[i].malted.insert(a-1);
				else
					c[i].unmalted.insert(a-1);
			}
		}
		for (int i = 0; i < n; ++i)
			malted[i] = 0;
		int nsat = 0;
		while (nsat < m){
			int domalt = -1;
			for (int i = 0; i < m; ++i)
				if (c[i].sat == false)
					if (c[i].malted.empty() == false && c[i].unmalted.empty() == true){
						int a = *c[i].malted.begin();
						c[i].sat = true;
						nsat++;
						if (malted[a] == 0){
							domalt = a;
							malted[a] = 1;
							break;
						}
					}
			if (domalt >= 0)
				for (int i = 0; i < m; ++i)
					c[i].unmalted.erase(domalt);
			else{
				for (int i = 0; i < m; ++i){
					if (c[i].sat == true)
						continue;
					else if (c[i].unmalted.empty() == true)
						break;
					else
						nsat++;
				}
				break;
			}
		}
		if (nsat == m){
			printf("Case #%d:", ++ncas);
			for (int i = 0; i < n; ++i)
				printf(" %d", malted[i]);
			printf("\n");
		}
		else
			printf("Case #%d: IMPOSSIBLE\n", ++ncas);
	}
}

#include <cstdio>
#include <cstring>
#include <vector>
#include <algorithm>
#include <map>

using namespace std;

typedef long long ll;
typedef pair<int, int> pii;

vector<int> X1, X2, Y1, Y2;

vector<vector<int> > next;

char tab[300][300];

int main(){
	int lz;
	scanf("%d", &lz);
	for(int cnt = 1; cnt <= lz; cnt++){
		int r;
		scanf("%d", &r);
		X1 = X2 = Y1 = Y2 = vector<int>(r);
		
		vector<pii> alive;
		memset(tab, '0', sizeof(tab));
		for(int i = 0; i < r; i++){
			scanf("%d%d%d%d", &X1[i], &Y1[i], &X2[i], &Y2[i]);
			X1[i]+= 125;
			X2[i]+= 125;
			Y1[i]+= 125;
			Y2[i]+= 125;
			for(int a = X1[i]; a <= X2[i]; a++){
				for(int b = Y1[i]; b <= Y2[i]; b++){
					alive.push_back(pii(a,b));
					tab[a][b] = '1';
				}
			}
		}
		
		int res = 0;
		while(!alive.empty()){
			res++;
			vector<pii> tak, nie;
			for(int i = 0; i < alive.size(); i++){
				int x = alive[i].first, y = alive[i].second;
				if(tab[x-1][y] == '1' || tab[x][y-1] == '1') tak.push_back(alive[i]);
				else nie.push_back(alive[i]);
				int px = x+1, py = y;
				if(tab[px][py] == '0' && tab[px-1][py] == '1' && tab[px][py-1] == '1') tak.push_back(pii(px,py));
			}
			
			for(int i = 0; i < tak.size(); i++){
				tab[tak[i].first][tak[i].second] = '1';
			}
			for(int i = 0; i < nie.size(); i++){
				tab[nie[i].first][nie[i].second] = '0';
			}
			alive = tak;
		}		printf("Case #%d: %d\n",cnt , res);
	}
	return 0;
}

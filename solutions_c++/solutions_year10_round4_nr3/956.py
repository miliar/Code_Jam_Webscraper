#include <cstdio>
#include <cstdlib>
#include <algorithm>
#include <vector>
#include <string>
#include <cstring>
#include <sstream>
#include <fstream>
#include <iostream>
#include <set>
#include <map>
#include <queue>
#include <list>
#include <cmath>
#include <deque>
#include <stack>
#include <functional>
#include <numeric>
#include <utility>
#include <iomanip>
#include <ctime>

using namespace std;

#define maxn 210
#define datat int
#define ansdatat int

int n;

int mp[2][maxn][maxn];
int sx = 50,
	sy = 50;

void init_deal(){
	memset(mp,0,sizeof(mp));

}

int main(){
	
	int tttt;
	scanf("%d", &tttt);
	for(int ttt = 1;ttt<=tttt;ttt++){
		init_deal();

		scanf("%d", &n);

		for(int i = 1;i<=n;i++){
			int a,b,c,d;
			scanf("%d%d%d%d", &a, &b, &c, &d);
			for(int j = a;j<=c;j++)
				for(int k = b;k<=d;k++)
					mp[0][sx+j][sy+k] = 1;
		}

		int ans = 0;
		int bj = 0, bi;
		while(true){
			bj = 1-bj;bi = 1-bj;
			ans++;
			int tot = 0;
			for(int i = 1;i<maxn;i++)
				for(int j = 1;j<maxn;j++){
					if(mp[bi][i][j] == 1){
						mp[bj][i][j] = 1;
						if(mp[bi][i-1][j]+mp[bi][i][j-1] == 0)
							mp[bj][i][j] = 0;

						

					}
					else{
						mp[bj][i][j] = 0;
						if(mp[bi][i-1][j]*mp[bi][i][j-1] == 1)
							mp[bj][i][j] = 1;

					}
					tot+=mp[bj][i][j];
				}
			if(tot == 0){
				break;
			}
		}
		
		
		printf("Case #%d: ",ttt);
		printf("%d", ans);
		printf("\n");
	}
	

	return 0;
};


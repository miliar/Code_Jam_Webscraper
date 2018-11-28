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

#define maxn 1010
#define datat int
#define ansdatat int

int n, k, f[maxn][maxn];

void init_deal(){
}

int main(){

	int ttt;
	scanf("%d", &ttt);
	for(int tt = 1;tt<=ttt;tt++){
		printf("Case #%d: ",tt);
		scanf("%d%d", &n, &k);
		/*
		for(int i = 0;i<=n;i++)f[0][i] = 0;
		f[0][0] = 1;

		for(int i = 1;i<=k;i++){
			f[i][0] = 1;
			for(int j = 1;j<=n;j++)
				f[i][j] = f[i-1][j] ^ f[i-1][j-1];

		}
		*/
		int rr = 1<<n;



		int ans;
		if(k % rr == rr-1)
			ans = 1;
		else
			ans = 0;
		if(ans == 0){
			printf("OFF\n");
		}
		else{
			printf("ON\n");
		}


	}
	

	

	return 0;
};


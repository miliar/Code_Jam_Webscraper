
#include <cstdlib>  
#include <cctype>  
#include <cstring>  
#include <cstdio>  
#include <cmath>  
#include <algorithm>  
#include <vector>  
#include <string>  
#include <iostream>  
#include <sstream>  
#include <map>  
#include <set>  
#include <queue>  
#include <stack>  
#include <fstream>  
#include <numeric>  
#include <iomanip>  
#include <bitset>  
#include <list>  
#include <stdexcept>  
#include <functional>  
#include <utility>  
#include <ctime>  
using namespace std;  

int T;
int cases;

int n;
int vins[20000][2];
int totaldis;

int dis[20000];

int main()
{
	freopen("A-large.in", "r",stdin);
	//freopen("in.txt", "r",stdin);
	freopen("out.txt", "w",stdout);

	cases = 1;
	scanf("%d",&T);

	while(cases <= T){
		scanf("%d",&n);
		for(int i=0; i<n;i++){
			scanf("%d%d",&vins[i][0], &vins[i][1]);
		}
		scanf("%d",&totaldis);

		memset(dis,0,sizeof(dis));
		dis[0] = vins[0][0] + min(vins[0][1], vins[0][0]);
		int maxl = dis[0];
		for(int i=1; i<n; i++){
			int tmp = 0;
			for(int j=0; j<i; j++){
				if(dis[j] >= vins[i][0] && (vins[i][0] + min(vins[i][1], vins[i][0] - vins[j][0])) > tmp)
					tmp = vins[i][0] + min(vins[i][1], vins[i][0] - vins[j][0]);
			}
			dis[i] = tmp;

			if(tmp >maxl)
				maxl = tmp;
		}

// 		if(cases == 23){
// 			printf("%d\n",n);
// 			for(int i=0; i<n;i++){
// 				printf("%d %d\n",&vins[i][0], &vins[i][1]);
// 			}
// 			printf("%d\n", totaldis);
// 		}

		printf("Case #%d: ", cases);
		if(maxl >= totaldis)
			printf("YES\n");
		else
			printf("NO\n");

		cases ++;
	}
}
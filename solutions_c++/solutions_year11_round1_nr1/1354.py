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

#define maxn 110
#define datat int
#define ansdatat int


datat n;
int pd, pg;

void init_deal(){
}

int main(){
	
	int tttt;
	scanf("%d", &tttt);
	for(int ttt = 1;ttt<=tttt;ttt++){
		printf("Case #%d: ",ttt);
		cin>>n>>pd>>pg;
		//cout<<n<<" "<<pd<<" "<<pg<<endl;
		bool yes = false;

		int st_d = 1;
		while(st_d<=n){
			if(st_d * pd % 100 == 0){
				int win_d = st_d*pd/100;
				if(win_d >0 && pg == 0){
				}
				else{
					int limit = 10000;
					int g = __gcd(pg, 100);
					int delta = 100/g;
					int st_g = ((st_d-1)/delta+1)*delta;
					int tot = 0;
					while(tot++<limit){
						int win_g = st_g*pg/100;
						if(win_g-win_d<=st_g-st_d){
							yes = true;
							break;
						}
						st_g+=delta;
					}
				}
				
			}
			st_d++;
		}

		if(yes)
			printf("Possible\n");
		else
			printf("Broken\n");


	}
	

	return 0;
};


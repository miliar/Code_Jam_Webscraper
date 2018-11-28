#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <climits>
using namespace std;

int T,N;

int main(){
	freopen("A-large.in","r",stdin);
	freopen("a.out","w",stdout);
	scanf("%d\n",&T);
	for(int k=1;k<=T;k++){
		scanf("%d ",&N);
		char play; int topos;
		int op = 1, bp = 1, ctime = 0, bt = 0, ot = 0;
		for(int i=1;i<=N;i++) {
			scanf("%c %d ",&play,&topos);
			//printf("%c %d: ",play,topos);
			int ltime = 0;
			if(play == 'O'){
				ltime += abs(op - topos) + 1;
				//printf(" %d %d %d",op,ltime,ot);
				if(ltime - ot <= 0)ltime = 1;
				else ltime -= ot;
				ot = 0;
				op = topos;
				bt += ltime;
				ctime += ltime;
				//printf(" %d %d %d\n",ltime,bt,ctime);
			}
			else{
				ltime += abs(bp - topos) + 1;
				//printf(" %d %d %d",bp,ltime,bt);
				if(ltime - bt <= 0)ltime = 1;
				else ltime -= bt;
				bt = 0;
				bp = topos;
				ot += ltime;
				ctime += ltime;
				//printf(" %d %d %d\n",ltime,ot,ctime);
			}
		}
		printf("Case #%d: %d\n",k,ctime);
	}
	return 0;
}

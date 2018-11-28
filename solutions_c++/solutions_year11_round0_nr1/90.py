#include <vector>
#include <list>
#include <map>
#include <set>
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

using namespace std;


int main(){
	freopen("A-large.in","r",stdin);
	freopen("A-large.out","w",stdout);
	int Te=1,cas; scanf("%d",&cas);
	while( cas-- ){
		int N; scanf("%d",&N);
		int OT=0,OP=1, BT=0,BP=1, cur=0;
		for(int i=0;i<N;i++){
			char op; int pos;
			scanf(" %c %d",&op,&pos);
			cur++;
			if( op=='O' ){
				cur=max(cur,OT+abs(pos-OP)+1);
				OT=cur, OP=pos;
			}else{
				cur=max(cur,BT+abs(pos-BP)+1);
				BT=cur, BP=pos;
			}
		}
		printf("Case #%d: %d\n",Te++,cur);
	}
}
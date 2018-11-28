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
	freopen("C-large.in","r",stdin);
	freopen("C-large.out","w",stdout);
	int Te=1,cas; scanf("%d",&cas);
	while( cas-- ){
		int N; scanf("%d",&N);
		int xor=0,sum=0,small=10000005;
		for(int i=0;i<N;i++){
			int val; scanf("%d",&val);
			xor^=val;
			sum+=val;
			small=min(small,val);
		}
		printf("Case #%d: ",Te++);
		if( xor==0 ) printf("%d\n",sum-small);
		else printf("NO\n");
	}
}
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

using namespace std;

#define REP(i,a,b) for(i=a;i<b;i++) 
#define rep(i,n) REP(i,0,n) 

int main(){
	int tc;
	int pd, pg;
	long long int n;
	scanf("%d",&tc);
	for(int t=0;t<tc;t++){
		bool f=true;
		int x=100, y=100, a, b;
		scanf("%lld%d%d",&n,&pd,&pg);
		a=pd;
		b=pg;
		for(int i=0;i<2;i++){
			if(pd%2==0){
				pd/=2;
				x/=2;
			}
			if(pd%5==0){
				pd/=5;
				x/=5;
			}
		}
		if(n<x)f=false;
		else if(pg==100||pg==0)f=false;
		if(a==b)f=true;
		printf("Case #%d: ",t+1);
		if(f)puts("Possible");
		else puts("Broken");
	}
 	return 0;
}

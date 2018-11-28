/*
	RosyIsh's code!
	
*/


#include<iostream>
#include <algorithm>
#include <bitset>
#include <cassert>
#include <cctype>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <ctime>
#include <deque>
#include <functional>
#include <iomanip>
#include <iostream>
#include <list>
#include <map>
#include <numeric>
#include <queue>
#include <set>
#include <sstream>
#include <stack>
#include <string>
#include <utility>
#include <vector>
#define VI vector<int>
#define PI pair<int,int>
#define PB(x) push_back(x)
#define MP(x,y) make_pair(x,y)
#define fill(a,b) memset((a),(b),sizeof((a)))

typedef long long LL;

#define SI ({int x;scanf("%d",&x);x;})
#define SL ({LL x;scanf("%lld",&x);x;})
using namespace std;

#define MX 1000005

int X,S,R,t,N;
int sp[MX];

void doit(){

	int cases = SI;

	for(int j=1;j<=cases;j++){

		X = SI;
		S = SI;
		R = SI;
		t = SI;
		N = SI;
		

		
		for(int i=1;i<=X;i++)sp[i]=S;

		for(int i=0;i<N;i++){
			int z= SI;
			int y = SI;
			int w = SI;
			for(int j=z+1;j<=y;j++) sp[j]+=w;
			
		}
		sort(sp+1,sp+X+1);
		
		double cur = 1.0*t;
		double ans = 0.0;
		for(int i=1;i<=X;i++){
			
			if(fabs(cur)>1.0e-9){
				double dis = min(1.0,cur*(sp[i]+R-S));
				ans+=(dis/(sp[i]+R-S));
				if(dis<1.0 && fabs(1.0-dis)>1.0e-9)ans+=((1.0-dis)/sp[i]);
				cur-=(dis/(sp[i]+R-S));
				
			}
			else{
				ans+=(1.0/sp[i]);
			}
		}		

		printf("Case #%d: %.10lf\n",j,ans);
	}
	
}

int main(int argc,char * argv[] ){

	if(argc>1){
		if(argv[1][0]=='s' || argv[1][0]=='S'){
			freopen("../A-small-attempt0.in","r",stdin);
			//freopen("../A-small-practice.in","r",stdin);
			freopen("../A-small-attempt0-output.out","w",stdout);
		}
		else{
			
			//freopen("../A-large-practice.in","r",stdin);
			freopen("../A-large.in","r",stdin);
			freopen("../A-large-output.out","w",stdout);
		}
	}

	doit();
	

	return 0;

}

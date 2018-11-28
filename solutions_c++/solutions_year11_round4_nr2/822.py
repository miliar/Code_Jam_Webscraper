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

#define SI ({int x;scanf("%d ",&x);x;})
#define SL ({LL x;scanf("%lld ",&x);x;})
using namespace std;

#define MX 505

int G[MX][MX];
char S[MX];
int D,R,C;
int ans = -1;


void solve(int x1,int y1,int x2,int y2){

	double cx = x1+((x2-x1)/2.0);
	double cy = y1+((y2-y1)/2.0);
	double sumx = 0.0 , sumy = 0.0;

	for(int i=x1;i<x2;i++){
		for(int j=y1;j<y2;j++){
			if(i==x1 && j==y1)continue;
			if(i==x1 && j==y2-1)continue;
			if(i==x2-1 && j==y1)continue;
			if(i==x2-1 && j==y2-1)continue;

			double px = i+0.5, py = j+0.5;
			sumx+=(G[i][j]*(px-cx));
			sumy+=(G[i][j]*(py-cy));

		}
	}
		
	if(fabs(sumx)<=1.0e-6 && fabs(sumy)<=1.0e-6)ans = max(ans,(x2-x1));
		

}

void doit(){

        int cases = SI;
        for(int i=1;i<=cases;i++){

		R = SI; C = SI; D = SI;
		ans = -1;

		for(int f=0;f<R;f++){

			scanf("%s ",S);
			for(int j=0;j<C;j++){
				int w = S[j]-'0';	
				G[f][j] = w+D;
			}
		}
		for(int x1=0;x1<R;x1++){
			for(int y1=0;y1<C;y1++){
				for(int k=3;x1+k<=R && y1+k<=C;k++){
					solve(x1,y1,x1+k,y1+k);
				}
			}
		}
						
		if(ans>=3)
                	printf("Case #%d: %d\n",i,ans);
		else
                	printf("Case #%d: IMPOSSIBLE\n",i);
		
        }
        
}


int main(int argc,char * argv[] ){

	if(argc>1){
		if(argv[1][0]=='s' || argv[1][0]=='S'){
			freopen("../B-small-attempt0.in","r",stdin);
			//freopen("../B-small-practice.in","r",stdin);
			freopen("../B-small-attempt0-output.out","w",stdout);
		}
		else{
			
			//freopen("../B-large-practice.in","r",stdin);
			freopen("../B-large.in","r",stdin);
			freopen("../B-large-output.out","w",stdout);
		}
	}

	doit();
	

	return 0;

}

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
using namespace std;

#define MX 1000005

double V[MX];
double D;
double G[MX];	
int k;

bool f(double y){

//	printf("--> %lf\n",y);
	int n = k;
	G[0] = V[0]-y;
	
	for(int i=1;i<n;i++)
	{	

		double dis = (V[i]-G[i-1]);

		if(dis<=D){
			
			G[i] = min(G[i-1]+D,V[i]+y);
		}
		else{
			G[i] = max(G[i-1]+D,V[i]-y);
		}
		
		double w = (G[i]-G[i-1]);

		if(w<D && D-w>1.0e-9)return false;
	}
	
	return true;	

}

void doit(){

	int t,cases = 0,c,d;
	scanf("%d",&t);

	while(t-->0){

		cases++;
		scanf("%d %d",&c,&d);
		D = d*1.0;
		int p,v;
		k=0;
		for(int i=0;i<c;i++){
			scanf("%d %d",&p,&v);
			for(int j=0;j<v;j++){
				V[k++]=1.0*p;
			}
		}
		
		//sort(V.begin(),V.end());

		double lo = 0.0, hi = 1.0e13;
		int times = 400;
		while(times-- >0){
			double mid = (lo+hi)/2.0;
			if(f(mid)) hi = mid;
			else lo = mid;
		}		

		lo=(lo+hi)/2.0;

		printf("Case #%d: %.20lf\n",cases,lo);
	}	

}


int main(int argc,char * argv[] ){

	if(argc>1){
		if(argv[1][0]=='s' || argv[1][0]=='S'){
			freopen("../B-small-attempt2.in","r",stdin);
			//freopen("../B-small-practice.in","r",stdin);
			freopen("../B-small-attempt2-output.out","w",stdout);
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

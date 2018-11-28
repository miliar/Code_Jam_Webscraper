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


struct DD{
	int x,y,w;
	bool operator<(const DD &b)const{
		if( w != b.w ) return w<b.w;
		return (y-x) < (b.y-b.x);
	}
}dd[10005];


int main(){
	freopen("A-large(1).in","r",stdin);
	freopen("A-large(1).out","w",stdout);
	int cas,Te=1;
	scanf("%d",&cas);
	while( cas-- ){
		//**
		int X,S,R,t,N;
		scanf("%d %d %d %d %d",&X,&S,&R,&t,&N);
		double sum=0.0, s=X;
		for(int i=0;i<N;i++) {
			scanf("%d %d %d",&dd[i].x,&dd[i].y,&dd[i].w);
			s-=(dd[i].y-dd[i].x);
		}
		//sum+=s/S;
		dd[N].x=0,dd[N].y=s,dd[N].w=0;
		N++;
		sort(dd,dd+N);
		double used=0;
		for(int i=0;i<N;i++){
			double v=R+dd[i].w;
			if( used+(dd[i].y-dd[i].x)/v <= t ){
				used+=(dd[i].y-dd[i].x)/v;
				sum+=(dd[i].y-dd[i].x)/v;
			}else{
				double _time=t-used;
				double dis=v*_time,left=(dd[i].y-dd[i].x)-dis;
				used+=_time;
				sum+=dis/v + left/(S+dd[i].w);
			}
		}
		//***
		printf("Case #%d: %.10lf\n",Te++,sum);
	}
	return 0;
}
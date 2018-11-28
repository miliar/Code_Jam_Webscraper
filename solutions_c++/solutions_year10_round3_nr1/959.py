#include <iostream>
#include <sstream>
#include <string>
#include <vector>
#include <deque>
#include <queue>
#include <set>
#include <map>
#include <algorithm>
#include <functional>
#include <utility>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <cstdio>

using namespace std;

#define REP(i,m,n) for((i)=(m);(i)<(int)(n);(i)++)
#define REP0(i,n) REP(i,0,n)
#define newline putchar('\n')

bool intersect(int x1,int y1, int x2, int y2){
	bool intersect=false;
	if((x1<x2 && y1<y2)||(x1>x2 && y1>y2))
		intersect=false;
	else intersect=true;

	return intersect;
}

int x[2000],y[2000],n;

void getdata(){
	scanf("%d",&n);
	int i,j,cut=0;
	REP0(i,n){
		cin>>x[i]>>y[i];
	}

	REP0(i,n){
		REP0(j,i){
			cut+=(int)intersect(x[j],y[j],x[i],y[i]);
		}
	}

	cout<<cut<<endl;
}

void solve(){
	getdata();	
}

main(){
	int n,testcases;
	cin>>testcases;
	REP0(n,testcases){
		printf("Case #%d: ",n+1);
		solve();
	}
}

#include <vector>
#include <string>
#include <sstream>
#include <queue>
#include <stack>
#include <map>
#include <set>
#include <algorithm>
#include <iostream>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <cstring>

using namespace std;

#define all(x) x.begin(),x.end()
#define FOR(it,x) for(__typeof(x.begin())it=x.begin();it!=x.end();++it)
#define bits(x) __builtin_popcount(x)

#define INF 1000000000

int P;
int m[1500];
int cost[12][1500];
//int res[12][1500][12];

int calc(int level, int pos, int acum) {
	int rta=INF;
	if (level>0) {
		rta=min(rta,cost[level][pos]+calc(level-1,2*pos,acum)+calc(level-1,2*pos+1,acum));
		rta=min(rta,calc(level-1,2*pos,acum+1)+calc(level-1,2*pos+1,acum+1));
	}else {
		if (min(m[2*pos],m[2*pos+1])==acum) rta=cost[level][pos];
		if (min(m[2*pos],m[2*pos+1])>acum) rta=0;
	}
	return rta;
}


int main(){
	int casos,c,i,j;
	
	cin>>casos;
	for (c=0;c<casos;c++){
		cout<<"Case #"<<(c+1)<<": ";
		cin>>P;
		
		for (i=0;i<(1<<P);i++) cin>>m[i];
		for (i=0;i<P;i++) for (j=0;j<(1<<(P-1-i));j++) cin>>cost[i][j];
		
		cout<<calc(P-1,0,0)<<endl;
	}
	
	return 0;
}

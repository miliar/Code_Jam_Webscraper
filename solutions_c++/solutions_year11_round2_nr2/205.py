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

long long pos[1000001];
long long npos[1000001];
int d,t;

inline long long mymax(long long a,long long b){
	if(a>b)return a;
	else return b;
}
inline long long myabs(long long a){
	if(a<0)return -a;
	else return a;
}

int check(long long time){
	long long left=-1e+16;
	for(int i=0;i<t;i++){
		npos[i]=mymax(left+d,pos[i]-time);
		if(myabs(npos[i]-pos[i])>time)return 0;
		left=npos[i];
	}
	return 1;
}

int main(){
	freopen("input.txt","r",stdin);
	freopen("output2.txt","w",stdout);

	int Q;
	scanf("%d",&Q);
	for(int test=1;test<=Q;test++){
		memset(pos,0,sizeof(pos));
		memset(npos,0,sizeof(npos));
		int c;
		t=0;
		scanf("%d%d",&c,&d);
		d*=2;
		int i,p,v,j;
		for(i=0;i<c;i++){
			scanf("%d%d",&p,&v);
			p*=2;
			for(j=0;j<v;j++)pos[t++]=p;
		}
		sort(pos,pos+t);
		long long r=1e+14,l=0,mid;
		while(l<r-1){
			mid=(r+l)/2;
			if(check(mid))r=mid;
			else l=mid;
		}
		mid=(r+l)/2;
		if(check(mid))r=mid;
		else l=mid;
		//if(check(r))l=r;
		printf("Case #%d: %.1lf\n",test,r*0.5);
	}
	return 0;
}

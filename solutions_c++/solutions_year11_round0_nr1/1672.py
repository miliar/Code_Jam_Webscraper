// #includes {{{
#include <algorithm>
#include <numeric>

#include <iostream>
#include <sstream>
#include <string>
#include <vector>
#include <queue>
#include <deque>
#include <stack>
#include <set>
#include <map>

#include <cstdio>
#include <cstdlib>
#include <cctype>
#include <cassert>
#include <cstring>

#include <cmath>
#include <complex>
using namespace std;
// }}}
// pre-written code {{{
#define REP(i,n) for(int i=0;i<(int)(n);++i)
#define RREP(i,a,b) for(int i=(int)(a);i<=(int)(b);++i)
#define FOR(i,c) for(__typeof((c).begin())i=(c).begin();i!=(c).end();++i)
#define ALL(c) (c).begin(), (c).end()

typedef long long Int;
typedef long long ll;
typedef long double ld;
// }}}

const int M=110;

int n;
int onow,bnow;

char c[M],num[M];
int times;

int nextPosition(int i,bool orange){
	while(i<n){
		if(orange){
			if(c[i]=='O'){
				return num[i];
			}
		}else{
			if(c[i]=='B'){
				return num[i];
			}
		}
		i++;
	}
	return -1;
}

void forward(int i){
	int o=nextPosition(i,true),b=nextPosition(i,false);
	int tm;
	if(c[i]=='O'){
		tm=abs(onow-o);
		onow=o;
		if(b!=-1){
			if(bnow<=b){
				bnow=min(bnow+tm+1,b);
			}else{
				bnow=max(bnow-tm-1,b);
			}
		}
//		cout<<"push orange"<<endl;
	}else{//c[i]=='B'
		tm=abs(bnow-b);
		bnow=b;
		if(o!=-1){
			if(onow<=o){
				onow=min(onow+tm+1,o);
			}else{
				onow=max(onow-tm-1,o);
			}
		}
//		cout<<"push blue"<<endl;
	}
	times+=tm+1;
//	cout<<endl;
//	cout<<tm<<endl<<onow<<" "<<bnow<<endl;
}


void main2(){
	scanf("%d",&n);
	REP(i,n){
		scanf("%s",c+i);
		scanf("%d",num+i);
//		cout<<c[i]<<" "<<num[i]<<endl;
	}
	times=0;
	onow=bnow=1;
	REP(i,n){
		forward(i);
//		cout<<onow<<" "<<bnow<<endl;	
//		cout<<times<<endl;
	}
	printf("%d\n",times);
}

int main() {
	int T;scanf("%d", &T);
	REP(ct, T){
		printf("Case #%d: ",ct+1);
		main2();
	}
	return 0;
}
// vim: fdm=marker:commentstring=\ \"\ %s:nowrap:autoread


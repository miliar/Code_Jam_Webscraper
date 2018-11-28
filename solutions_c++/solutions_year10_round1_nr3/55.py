
#include <iostream>
#include <sstream>
#include <fstream>
#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <vector>
#include <string>
#include <stack>
#include <queue>
#include <set>
#include <map>
#include <algorithm>
using namespace std;

typedef long long ll;

const int n=1000*1000+1000;

int  val[1+n]={0,0,1};
int rval[1+n]={0,2,4};

inline int check(int a, int b){
	if(a==b)return 0;
	if(b<a)swap(a,b);
	return (a<=val[b]);
}
inline int cnt(int n, int m){
	if(m<  val[n])return m;
	if(m< rval[n])return val[n];
	return m-(rval[n]-1)+val[n];
}
int main(){
	for(int i=3;i<=n;i++){
		for(int k=val[i-1]+1;;k++){	//k<i
			val[i]=k-1;
			if(check(k,i-k)==1)break;
		}
	}

	for(int i=3;i<=n;i++)if(val[i-1]!=val[i]){
		rval[ val[i] ]=i;
	}
	for(int i=val[n]+1;i<=n;i++){
		rval[ i      ]=n;
	}

	int nn;scanf("%d",&nn);
	for(int npr=1;npr<=nn;npr++){
		int a1,a2;scanf("%d%d",&a1,&a2);
		int b1,b2;scanf("%d%d",&b1,&b2);

#if 0
		for(int i=0;i<=40;i++)cout<<"cnt(10,"<<i<<")="<<cnt(10,i)<<endl;
		for(int i=0;i<=40;i++)cout<<"cnt(11,"<<i<<")="<<cnt(11,i)<<endl;
		for(int i=0;i<=40;i++)cout<<"cnt(12,"<<i<<")="<<cnt(12,i)<<endl;
		for(int i=0;i<=40;i++)cout<<"cnt(13,"<<i<<")="<<cnt(13,i)<<endl;
		for(int i=0;i<=40;i++)cout<<"cnt(14,"<<i<<")="<<cnt(14,i)<<endl;
#endif

		ll ans=0;
		for(int i=a1;i<=a2;i++)ans+=cnt(i,b2)-cnt(i,b1-1);
		printf("Case #%d: %lld\n",npr,ans);
	}
	return 0;
}

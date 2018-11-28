#include <cctype>
#include <climits>
#include <cmath>
#include <cstdio>
#include <cstring>
#include <algorithm>
#include <iostream>
#include <map>
#include <set>
#include <string>
#include <vector>
using namespace std;

#define VI vector<int>
#define VS vector<string>
#define SZ(x) ((int)(x).size())
#define FR(i,a,b) for(int i=(a);i<(b);++i)
#define MS(a,b) memset((a),b,sizeof(a))
#define EC(tp,it,a) for(tp::iterator it=(a).begin();it!=(a).end();++it)
#define SE(x) cout<<#x<<" = "<<x<<endl
#define PB push_back

template<class T> void inc(T& a, const T& b) {
	if (a < b) a = b;
}
template<class T> void dec(T& a, const T& b) {
	if (a > b) a = b;
}

const int N=50+3;

int n,k;
char m1[N][N];
char m2[N][N];
int ans;

void skew(){
	for(int i=0;i<n;++i){
		int c1=0,c2=0;
		for(int j=0,t=i;j<n && t<n;++j,++t){
			if(m2[t][j]=='B')++c1;
			else c1=0;
			if(c1>=k)ans|=1;
			
			if(m2[t][j]=='R')++c2;
			else c2=0;
			if(c2>=k)ans|=2;
		}
	}

	for(int j=0;j<n;++j){
		int c1=0,c2=0;
		for(int i=0,t=j;i<n && t<n;++i,++t){
			if(m2[i][t]=='B')++c1;
			else c1=0;
			if(c1>=k)ans|=1;
			
			if(m2[i][t]=='R')++c2;
			else c2=0;
			if(c2>=k)ans|=2;
		}
	}
}

void run(){
	FR(i,0,n)FR(j,0,n)m2[i][j]=m1[n-1-j][i];
//	FR(i,0,n)puts(m2[i]);
	FR(j,0,n){
		for(int low=n-1,high=n-2;low>0 && high>=0;--low,--high){
			if(m2[low][j]!='.')continue;
			while(high>=0 && m2[high][j]=='.')--high;
			if(high>=0)swap(m2[low][j],m2[high][j]);
		}
	}
//	FR(i,0,n)puts(m2[i]);
	
	for(int i=0;i<n;++i){
		int c1=0,c2=0;
		for(int j=0;j<n;++j){
			if(m2[i][j]=='B')++c1;
			else c1=0;
			if(c1>=k)ans|=1;
			
			if(m2[i][j]=='R')++c2;
			else c2=0;
			if(c2>=k)ans|=2;
		}
	}
	
	for(int j=0;j<n;++j){
		int c1=0,c2=0;
		for(int i=0;i<n;++i){
			if(m2[i][j]=='B')++c1;
			else c1=0;
			if(c1>=k)ans|=1;
			
			if(m2[i][j]=='R')++c2;
			else c2=0;
			if(c2>=k)ans|=2;
		}
	}

	skew();
	FR(i,0,n)reverse(m2[i],m2[i]+n);
	skew();
}

int main() {
	freopen("a2.in","r",stdin);
	freopen("a2.out","w",stdout);
	
	int ts;
	scanf("%d",&ts);
	FR(cas,0,ts){
		scanf("%d%d",&n,&k);
		MS(m1,0);
		MS(m2,0);
		FR(i,0,n)scanf("%s",m1+i);
		ans=0;
		run();
		printf("Case #%d: ",cas+1);
		if(ans==0)puts("Neither");
		if(ans==1)puts("Blue");
		if(ans==2)puts("Red");
		if(ans==3)puts("Both");
	}
	return 0;
}

//Author : Sushant Bhatia
#include<iostream>
#include<cstdio>
#include<vector>
#include<string>
#include<algorithm>
#include<set>
#include<map>
#include<queue>
#include<cmath>
#include<cstring>
#define FOR(i,j,k) for(i = j;i < k;i++)
#define RFOR(i,j,k) for(i = k-1;i >= j;i--)
#define LL long long
#define GET(x) scanf("%d",&x)
#define OUT(x) printf("%d\n",x)
#define SET(x) memset(x,0,sizeof(x))
#define S(x) x.size()
bool comp(int i,int j){ return i > j; }
using namespace std;
LL x[10005];
LL GCD(LL a,LL b){
	if(!b) return a;
	return (b,a%b);
}	
int main(){
	int t;
	LL l,h,a,b,k;
	int n;
	GET(t);
	int cs,i;
	bool fnd;
	FOR(cs,1,t+1){
		printf("Case #%d: ",cs);
		GET(n);
		cin>>l>>h;
		FOR(i,0,n) cin>>x[i];
		LL lcm = 1;
		FOR(k,l,h+1){
			fnd = true;
			FOR(i,0,n){
				a = x[i];
				b = k;
				if(a%b != 0 && b%a != 0){
					fnd = false;
					break;
				}
			}
			if(fnd) break;
		}	
		if(fnd)	cout<<k<<endl;
		else cout<<"NO\n";
	}
	return 0;
}	

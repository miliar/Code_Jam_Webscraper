//Free cell Statistics
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
int main(){
	int t,pg,pd;
	LL n;
	int g,d;
	int ltd;
	LL ul = 100;
	GET(t);
	int i,c;
	FOR(c,1,t+1){
		cin>>n;GET(pd);GET(pg);
		n = min(n,ul);
		FOR(i,1,n+1){
			if((pd*i)%100 == 0){
				ltd = ((100-pd)*i)/100;
				break;
			}
		}
		if(i<=n){
			if(pg == 100 && pd != 100) printf("Case #%d: Broken\n",c);
			else if(pg == 0 && pd != 0) printf("Case #%d: Broken\n",c);
			else printf("Case #%d: Possible\n",c);
		}
		else printf("Case #%d: Broken\n",c);
	}
	return 0;
} 

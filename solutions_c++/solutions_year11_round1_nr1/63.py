#include <cmath>
#include <ctime>
#include <cstdio>
#include <cctype>
#include <cstring>
#include <iostream>
#include <algorithm>
#include <set>
#include <map>
#include <string>
#include <vector>
#define maxn 110000
#define maxl 1000000000
using namespace std;

typedef long long ll;

char s[maxn];
pair<char,int> a[maxn];
int nxt[maxn];

int gcd(int x,int y){
	if(y==0)return x;
	return gcd(y,x%y);
}

void solve(){
	ll n;
	int p1,p2,temp;
	cin>>n;
	scanf("%d%d",&p1,&p2);
	if(p2==0 && p1!=0 || p2==100 && p1!=100){
		printf("Broken\n");
		return;
	}
	if(p1==0 || p1==100){
		printf("Possible\n");
		return;
	}
	temp=gcd(p1,100);
	temp=100/temp;
	if(temp>n)printf("Broken\n");else printf("Possible\n");
}
	
		

int main(){
	int t,i;
	scanf("%d",&t);
	for(i=1;i<=t;++i){
		printf("Case #%d: ",i);
		solve();
	}
	return 0;
}

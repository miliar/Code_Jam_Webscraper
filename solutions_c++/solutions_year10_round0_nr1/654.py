#include<iostream>
#include<cstdio>
#include<cstring>
#include<algorithm>
#include<vector>
#include<queue>
#include<utility>
#include<cmath>
#include<string>
using namespace std;

#define llong long long 
const double pi = acos(-1.0);
const int maxInt = 0x7fffffff;
const int minInt = ~maxInt;

const int N = 35;
int s[N];

int main(){
	//freopen("in.txt","r",stdin);freopen("out.txt","w",stdout);
    int i,j,k,t,nc = 0;
	scanf("%d",&t);
	s[1] = 1;
	for(i = 2;i<=30;i++){
		s[i] = s[i-1]*2+1;
	}
	while(t--){
		int n,m;
		scanf("%d%d",&n,&m);
		if((m+1)%(s[n]+1)==0)printf("Case #%d: ON\n",++nc);
		else printf("Case #%d: OFF\n",++nc);
	}
    return 0;
}
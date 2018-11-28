#include <iostream>
#include <fstream>
#include <vector>
#include <set>
#include <map>
#include <string>
#include <cmath>
#include <cassert>
#include <ctime>
#include <algorithm>
#include <queue>
#include <memory.h>
#include <stack>

using namespace std;

#define pb push_back
#define mp make_pair
#define fir first
#define fi first
#define sec second
typedef long long int64;
typedef long double ld;

const int inf=2000000000;
const ld eps=1e-07;

int n,p1,p2,k1,k2;

int main(){
	#ifndef ONLINE_JUDGE
		freopen("input.txt","r",stdin);
		freopen("output.txt","w",stdout);
	#endif
	int t;
	scanf("%d",&t);
	for (int z=1;z<=t;++z){
		scanf("%d %d %d",&n,&p1,&p2);
		k1=100;
		k2=100;
		while (k1 %2==0 && p1 %2==0 && (k1 || p1)){
			k1/=2;
			p1/=2;
		}
		while (k1 %5==0 && p1 %5==0 && (k1 || p1)){
			k1/=5;
			p1/=5;
		}
		while (k2 %2==0 && p2 %2==0 && (k2 || p2)){
			k2/=2;
			p2/=2;
		}
		while (k2 %5==0 && p2 %5==0 && (k2 || p2)){
			k2/=5;
			p2/=5;
		}
		printf("Case #%d: ",z);
		if (k1>n || (p2==1 && k2==1 && (p1!=1 || k1!=1) ) || (p2==0 && p1!=0))
			printf("Broken\n");
		else printf("Possible\n");
	}
	return 0;
}
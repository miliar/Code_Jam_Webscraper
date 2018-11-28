#include <iostream>
#include <cstdio>
#include <vector>
#define ST first
#define ND second
#define MP make_pair
#define PB push_back
using namespace std;
typedef pair<int,int> pi;
typedef double lf;
typedef long double llf;
typedef long long int lld;
typedef vector<int> vi;

int t,n,k,tt;

int main(){
	scanf("%d",&t);
	while(t--){
		scanf("%d %d",&n,&k);
		k++;
		tt++;
		if(k%(1<<n)==0)
			printf("Case #%d: ON\n",tt);
		else
			printf("Case #%d: OFF\n",tt);
	}
}

#include<iostream>
#include<vector>
#include<map>
#include<set>
#include<algorithm>
#include<cstdio>
#include<cmath>
#include<cstdlib>
#include<cstring>
#include<string>
#include<queue>
#include<complex>
#include<numeric>
#include<bitset>

using namespace std;
typedef long long Int;
typedef vector<int> vint;
typedef vector<vint> vvint;
typedef pair<Int,Int> pint;

int main(){
	int a[1000];
	int n,k,t;
	cin >> t;
	for(int i=0;i<t;i++){
		for(int j=0;j<1000;j++) a[j]=0;
		cin >> n >> k;
		for(int j=0;k>0;j++,k/=2){
			a[j]=k%2;
		}
		int c=0;
		for(int j=0;j<n;j++){
			if(a[j]==1) c++;
		}
		if(c==n){
			printf("Case #%d: ON\n",i+1);
		}else{
			printf("Case #%d: OFF\n",i+1);
		}
	}
	return 0;
}



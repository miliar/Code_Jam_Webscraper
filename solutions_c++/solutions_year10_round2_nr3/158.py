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

inline int gcd(int a,int b){
	return b!=0 ? gcd(b,a%b) : a;
}

inline int C(int a,int b){
	int M=100003;
	int tmp[1000];
	int i,j;
	if(a<b) return 0;
	if((a-b)<b) b=a-b;
		
	for(i=0;i<b;i++){
		tmp[i]=a-i;
	}
	for(i=2;i<=b;i++){
		int k=i;
		for(j=0;j<b;j++){
			int g=gcd(k,tmp[j]);
			tmp[j]/=g;
			k/=g;
			if(k==1) break;
		}
	}
	int ans=1;
	for(i=0;i<b;i++){
		ans*=tmp[i];
		ans%=M;
	}
//	cout << a << "	" << b << "	" << ans << endl;
	return ans;
}
		
int main(){
	int i,j,k;
	Int M=100003;
	static Int memo[512][512];
	static Int memoc[512][512];
	for(i=0;i<512;i++){
		for(j=0;j<512;j++) memoc[i][j]=C(i,j);
	}
	for(i=0;i<512;i++){
		memo[1][i]=1;
		memo[i][1]=1;
	}
	for(i=2;i<=500;i++){
		for(j=2;j<i;j++){
			Int ans=0;
			for(k=1;k<j;k++){
				ans+=memo[j][k]*memoc[i-j-1][j-k-1];
				ans%=M;
			}
			memo[i][j]=ans;
		}
	}
	
	int solve[512];
	for(i=1;i<=500;i++){
		Int ans=0;
		for(j=1;j<i;j++){
			ans+=memo[i][j];
			ans%=M;
		}
		solve[i]=ans;
	}


	int t;
	cin >> t;
	for(int l=0;l<t;l++){
		int n;
		cin >> n;
		printf("Case #%d: %d\n",l+1,solve[n]);
	}
	return 0;
}



//{{{
#include <vector> 
#include <list> 
#include <map> 
#include <set> 
#include <deque> 
#include <queue> 
#include <stack> 
#include <bitset> 
#include <valarray> 
#include <algorithm> 
#include <functional> 
#include <numeric> 
#include <utility> 
#include <complex> 
#include <memory> 
#include <new> 
#include <iterator> 
#include <limits> 
#include <sstream> 
#include <iostream> 
#include <iomanip> 
#include <cstdio> 
#include <cmath> 
#include <cstdlib> 
#include <cstring> 
#include <ctime> 
#include <cassert> 
#include <cctype> 
using namespace std;
//}}}

const int maxn=1000000;
bool isprime[maxn];
vector<int> primes;
int father[maxn];
int getf(int f){
	return father[f]==-1?f:father[f]=getf(father[f]);
}
bool merge(int a,int b){
	a=getf(a),b=getf(b);
	if(a!=b){
		father[a]=b;
		return true;
	}
	return false;
}
int main(){
	for(int i=2;i<maxn;i++)
		isprime[i]=true;
	for(int i=2;i<maxn;i++)
		if(isprime[i]){
			primes.push_back(i);
			for(int j=i+i;j<maxn;j+=i)
				isprime[j]=false;
		}
	int tests;
	scanf("%d",&tests);
	for(int t=1;t<=tests;t++){
		long long A,B,P,C;
		cin>>A>>B>>P;
		P<?=C=B-A;
		memset(father,-1,sizeof(father[0])*(C+1));
		int comps=C+1;
		for(int i=0;i<primes.size()&&primes[i]<=C;i++)
			if(primes[i]>=P){
				for(int R=(primes[i]-A%primes[i])%primes[i];R+primes[i]<=C;R+=primes[i])
					if(merge(R,R+primes[i]))
						comps--;
			}
		printf("Case #%d: %d\n",t,comps);
	}
scanf("%*s");
	return 0;
}

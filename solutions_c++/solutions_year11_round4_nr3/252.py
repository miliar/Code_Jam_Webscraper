#include <iostream>
#include <set>
#include <map>
#include <vector>
#include <string>
#include <cmath>
#include <algorithm>

using namespace std;

long long i,j,k,l,m,n,t,tt,ttt,ii,jj,y,d;
int ww[105];
int w,x,s,r,a,b,sum,ss,c;
char mass[12][12];
int isprim[1000001];

int isprime (int x){
	if (x==1) return 0;
	int i;
	for (i=2;i<x;i++){
		if (x%i==0) return 0;
	}
	return 1;
}
int ispowerofprime(int x){
	int i;
	if (x==1) return 1;
	if (isprime(x)) return 1;
	for (i=2;i<x;i++)
		if (x%i==0){
			while (x%i==0){
				x/=i;
			}
			if (x==1) return 1; else return 0;
		}
}

int main(){
	freopen("c:/C-large.in","r",stdin);
	freopen("c:/output.txt","w",stdout);
	isprim[0]=1;
	isprim[2]=0;
	vector<long long> primes;
	for (i=2;i*i<=1000000;i++)
		if (isprim[i]==0){
			for (j=2*i;j<=1000000;j+=i){
				isprim[j]=1;
			}
		}
	for (i=2;i<1000000;i++)
		if (isprim[i]==0) primes.push_back(i);
	cin>>ttt;
	while(ttt--){
		tt++;
		cout<<"Case #"<<tt<<": ";
		cin>>n;
		if (n==1) {cout<<0<<endl;continue;}
		long long ans=0;
		for (i=0;i<primes.size();i++){
			long long p=primes[i];
			long long xar=p*p;
			while (xar<=n){
				ans++;
				xar*=p;
			}
		}
		cout<<ans+1<<endl;
	}
	return 0;
}
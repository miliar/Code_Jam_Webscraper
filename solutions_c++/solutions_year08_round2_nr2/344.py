#include <iostream>
#include <string>
#include <map>
#include <vector>
#include <sstream>
#include <utility>
#include <algorithm>

using namespace std;

bool setf[1001];
int primes[1001],ps;
int q[1001],qs,qi;

int gcd(int a, int b){
	if(b==0)return a;
	else return gcd(b,a%b);
}
void sieve(){
	ps=0;
	primes[ps++]=2;
	bool p[1001];
	memset(p,1,sizeof(p));
	for(int i=3;i<1000;i+=2)
	if(p[i]){
		primes[ps++]=i;
		for(int j=i*2;j<=1000;j+=i)
			p[j]=false;
	}
	//cout<<ps<<" "<<primes[ps-1]<<endl;
	return;
}

int main(){
	int t;
	int a,b,p,ret,tmp;
	sieve();
	cin>>t;
	for(int tc=1;tc<=t;tc++){
		cin>>a>>b>>p;
		memset(setf,0,sizeof(setf));
		ret=0;
		for(int i=a;i<=b;i++)
		if(!setf[i]){
			setf[i]=true;
			//cout<<i<<endl;
			ret++;
			qs=qi=0;
			q[qs++]=i;
			while(qi<qs){
				for(int j=a;j<=b;j++)
				if(!setf[j]){
					for(int k=0;k<ps && !setf[j];k++)
					if(primes[k]>=p && (q[qi]%primes[k])==0 && j%primes[k]==0){
						setf[j]=true;
						q[qs++]=j;
					}
				}
				qi++;
			}
		}
		//printf("Case #%d: %d\n",tc,res);
		cout<<"Case #"<<tc<<": "<<ret<<endl;
	}
	return 0;
}

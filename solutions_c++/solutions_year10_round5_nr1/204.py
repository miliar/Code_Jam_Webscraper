#include<string.h>
#include<math.h>
#include<vector>
#include<iostream>
const int SIZE=11000;
bool prime[SIZE];
using namespace std;
vector<int> primes;
void seive(){
	memset(prime,true,sizeof(prime));
	prime[0]=prime[1]=false;
	int k=2;
	while(k<SIZE) {
		for(int i=2*k;i<SIZE;i+=k)
			prime[i]=false;
		k++;while(k<SIZE && !prime[k])k++;             
	}
	for(int i=2;i<SIZE;i++)if(prime[i])primes.push_back(i); 
}
int D[7]={1,10,100,1000,10000,100000,1000000};
int main(){
	seive();
	int times;
	cin>>times;
	int s[10],d,k,ans;
	for(int tm=1;tm<=times;tm++){
		ans=-1;
		cin>>d>>k;
		cout<<"Case #"<<tm<<": ";
		for(int i=0;i<k;i++){
			cin>>s[i];
		}
		bool idk=0;
		if(k==1){
			idk=1;
		}else{
			int M;
			M=s[0];
			for(int i=1;i<k;i++)M=max(M,s[i]);
			int p,b;
			for(int i=0;i<primes.size();i++){
				p=primes[i];
				if(p<=M)continue;
				if(p>D[d])break;
				for(int a=0;a<=p;a++){
					b=((s[1]-s[0]*a)%p+p)%p;
					bool ac=1;
					for(int j=2;j<k;j++){
						if(s[j]!=(a*s[j-1]+b)%p){
							ac=0;
							break;
						}
					}
					if(ac){
						if(ans==-1 || ans==(a*s[k-1]+b)%p){
							ans=(a*s[k-1]+b)%p;
						}else{
							idk=1;
							break;
						}
					}
				}

			}
		}
		if(idk)
			cout<<"I don't know."<<endl;
		else
			cout<<ans<<endl;
	}
	return 0;
}

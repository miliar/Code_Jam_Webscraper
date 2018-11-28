#include <vector>
#include <string>
#include <queue>
#include <stack>
#include <map>
#include <set>
#include <algorithm>
#include <iostream>
#include <cstdio>
#include <cmath>

using namespace std;

long long A,B,P;

long long gcd(long long a, long long b){
	if (a<b) return gcd(b,a);
	if (b==0) return a;
	return gcd(b,a%b);
}

long long tabla[1100];

long long mayor(long long n){
	long long i,rta=1;
	for (i=2;i*i<=n;i++){
		while (n%i==0){
			rta>?=i;
			n/=i;
		}
	}
	rta>?=n;
	return rta;
}

int vis[1100];

int main(){
	int i,j,casos,c;
	
	for (i=1;i<1100;i++) tabla[i]=mayor(i);
	
	cin>>casos;
	for (c=1;c<=casos;c++){
		cin>>A>>B>>P;
		
		int rta=0;
		
		memset(vis,0,sizeof(vis));
		for (i=A;i<=B;i++) if (!vis[i]){
			rta++;
			vis[i]=true;
			queue<long long> cola;
			cola.push(i);
			
			while (!cola.empty()){
				long long cu=cola.front(); cola.pop();
				
				for (j=A;j<=B;j++) if (!vis[j] && tabla[gcd(cu,j)]>=P){
					vis[j]=true;
					cola.push(j);
				}
			}
		}
		cout<<"Case #"<<c<<": "<<rta<<endl;
	}
	return 0;
}

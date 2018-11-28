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

#define all(x) x.begin(),x.end()
#define FOR(it,x) for(__typeof(x.begin())it=x.begin();it!=x.end();++it)

#define MOD (10007)
#define MAX 101000000

vector<int> fact;

int eleva(int a, int e){
	a=a%MOD;
	if (e==0) return 1;
	int rta=eleva(a,e/2);
	rta=(rta*rta)%MOD;
	if (e%2==1) rta=(rta*a)%MOD;
	return rta;
}

int inv(int a){
	return eleva(a,MOD-2);
}

int enfact(int n){
	int rta=0;
	
	while (n/MOD){
		rta+=n/MOD;
		n/=MOD;
	}
	return rta;
}

int comb(int n, int k){
	if (enfact(n)>enfact(k)+enfact(n-k)) return 0;
	int rta=fact[n];
	
	rta=(rta*inv(fact[k]))%MOD;
	rta=(rta*inv(fact[n-k]))%MOD;
	return rta;
}

int calc(int a, int b){
	if (a<0 || b<0) return 0;
	if ((a+b)%3!=0) return 0;
	if (2*a<b) return 0;
	if (2*b<a) return 0;
	int x=(2*a-b)/3,y=(2*b-a)/3;
	
	return comb(x+y,x);
}

int sacar(int i){
	while (i%MOD==0) i/=MOD;
	
	return (i%MOD);
}

int main(){
	int casos,c,i,j,pri,sec,m;
	
	fact.resize(MAX);
	fact[0]=1;
	for (i=1;i<MAX;i++) fact[i]=(fact[i-1]*sacar(i))%MOD;
	
	cin>>casos;
	for (c=0;c<casos;c++){
		cout<<"Case #"<<c+1<<": ";
		cin>>pri>>sec>>m;
		
		vector<pair<int,int> > lista(m); 
		for (i=0;i<m;i++){
			int a,b;
			
			cin>>a>>b;
			lista[i]=make_pair(a,b);
		}
		lista.push_back(make_pair(pri,sec));
		sort(all(lista));
		vector<int> val(m+1);
		
		for (i=0;i<m+1;i++){
			int a=lista[i].first-1,b=lista[i].second-1;
			val[i]=calc(a,b);
		}
		//for (i=0;i<m+1;i++) cerr<<val[i]<<" "; cerr<<endl;
		
		for (i=0;i<m+1;i++) for (j=i+1;j<m+1;j++){
			int a=lista[j].first-lista[i].first,b=lista[j].second-lista[i].second;
			
			val[j]=((val[j]-calc(a,b)*val[i])%MOD+MOD)%MOD;
		}
		cout<<val[m]<<endl;
	}
	
	return 0;
}

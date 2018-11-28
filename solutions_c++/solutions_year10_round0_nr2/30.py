//Marcin Baran

#include<iostream>
#include<sstream>
#include<vector>
#include<cmath>
#include<list>
#include<algorithm>

using namespace std;
typedef long long int lli;
lli z,N,K;

lli NWD(lli a,lli b){
	if(a < b) return NWD(b,a);
	if(a % b == 0) return b;
		else return NWD(b,a%b);
}

lli absolute(lli a){
	if(a<0) return -a;
	return a;
}

lli a,b;

int main(){
	cin>>z;
	for(lli ii=1;ii<=z;++ii){
		cin>>N;
		vector<lli> wynik;
		cin>>b;
		wynik.push_back(b);
		for(int i=1;i<N;++i){
			cin>>a;
			wynik.back() = absolute(a - wynik.back());
			wynik.push_back(a);
		}
		wynik.resize(wynik.size()-1);
		lli nwd = wynik[0];
		for(unsigned int i=0;i<wynik.size();++i){
			if(wynik[i] == 0) continue;
			if(nwd == 0) nwd = wynik[i];
				else nwd = NWD(nwd,wynik[i]);
		}
//		cout<<nwd<<endl;
		cout<<"Case #"<<ii<<": "; 
		if(nwd == 0 || b % nwd == 0) cout<<0<<endl;
		else cout<<nwd - b%nwd<<endl;
	}
	return 0;
}

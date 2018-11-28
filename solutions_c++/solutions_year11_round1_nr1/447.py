/*
*  Javier Segovia
*  0.016
*/
#include<iostream>
#include<string>
#include<vector>
#include<cmath>
using namespace std;
#define SL size()
#define LE length()
#define PB push_back
#define MP make_pair

long long gcd(long long a,long long b){
	if(b == 0) return a;
	return gcd(b,a%b);
}

int main(){
	int Pd,Pg,T;
	long long N;
	cin>>T;
	for(int i=1;i<=T;i++){
		cin>>N>>Pd>>Pg;
		int a1,b1,gcd1;//a2,b2,gcd1,gcd2;
		bool ok=true;
		gcd1 = gcd(Pd,100);
		a1 = Pd/gcd1;
		b1 = 100/gcd1;
		if(b1 > N) ok=false;
		/*if(ok){
			gcd2 = gcd(Pg,100);
			a2 = Pg/gcd2;
			b2 = Pg/gcd2;
			
		}*/
		if(Pd > 0 && Pg == 0) ok=false;
		if(Pd < 100 && Pg == 100) ok=false; 
		cout<<"Case #"<<i<<": "<<(ok?"Possible":"Broken")<<endl;
	}
}
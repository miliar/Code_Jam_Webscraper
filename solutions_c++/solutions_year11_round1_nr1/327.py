#include<iostream>
using namespace std;

typedef long long int64;

int64 gcd(int64 a,int64 b){
	if( b==0 ) return a;
	while( a%b ){
		int64 temp=a%b;
		a=b;
		b=temp;
	}
	return b;
}

int main(){
	freopen("A-large.in","r",stdin);
	freopen("A-large.out","w",stdout);

	int Te=1,cas; cin>>cas;
	while( cas-- ){
		int64 N,Pd,Pg;
		cin>>N>>Pd>>Pg;
		
		if( (Pg==0 && Pd!=0 ) || (Pg==100 && Pd!=100) ||(100/gcd(100,Pd)>N) )
			printf("Case #%d: Broken\n",Te++);
		else 
			printf("Case #%d: Possible\n",Te++);
	}
}
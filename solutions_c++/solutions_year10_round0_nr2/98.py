#include<iostream>

using namespace std;

#define REP(i, n) for(int i=0;i<n;i++)

typedef unsigned long long Int;

Int gcd(Int a, Int b){
	if(b==0)return a;
	return gcd(b, a%b);
}

const int N=1100;

Int x[N];

int c, n;

Int diff(Int a, Int b){
	if(a>=b)return a-b;
	else return b-a;
}

Int findT(){
	Int g=diff(x[1], x[0]);
	cout<<"g="<<g<<endl;
	for(int i=2;i<n;i++){
		g=gcd(g, diff(x[i], x[i-1]));
	}
	return g;
}

int main(){
	cin>>c;
	REP(i, c){
		cin>>n;
		REP(j, n){
			cin>>x[j];
			cout<<x[j]<<endl;
		}
		Int T=findT();
		cout<<T<<endl;
	}
	return 0;
}

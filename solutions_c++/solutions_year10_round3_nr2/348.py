#include<cstdio>
#include<cmath>
#include<iostream>
using namespace std;
int T, L , P , C;
int findElm(long long int L,long long int P,long long int C){
	int k=0;
	while(L < P){
		L*=C;
		k++;
	}
	k--;
	int a=0;
	while(k!=0)
	{
		k/=2;
		a++;
	}
	return a;
}
int main(){
	cin >> T;
	for(int t=1;t<=T;t++){
		cin >> L >> P >> C;
		int x = findElm(L,P,C);
		cout << "Case #" << t << ": " << x << endl;
	}
}

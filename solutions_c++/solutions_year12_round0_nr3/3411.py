#include <iostream>
#include <vector>
#include <stack>
#include <iomanip>
#include <cstring>
#include <string>
#include <set>
#include <cmath>
#include <stdio.h>
using namespace std;

long A, B, sum;

bool ok[2000001];
int Lenght( long X ){
	int l=1;
	while(X/10!=0){
		X/=10;
		l++;
	}
	return l;
}

void ToNum( string x, long &X ){
	X = 0;
	for(int i=0; i<x.length(); i++){
		X*=10;
		X+=(x[i]-'0');
	}
}


void ror(long & T, int len_1){
	long z = T%10;
	for(int i=0; i<len_1; i++){
		z*=10;
	}
	T/=10;
	T+=z;
}

void check( long X ){
	ok[X] = true;
	int time = 1;
	long T = X;
	int len = Lenght(X)-1;
	
	for(int i=0; i<len; i++){
		ror(T,len);
		if(ok[T]==false && A<=T && T<=B){
			ok[T] = true;
			time++;
		}
	}
	
	sum+=(time*(time-1)/2);
}

int main(){
	freopen("test.txt","r",stdin);
	freopen("test1.txt","w",stdout);

	int k=1;
	int tc;
	string a, b;
	cin >> tc;
	while( tc-- ){
		memset(ok,0,sizeof(ok));
		sum = 0;

		cin >> a >> b;
		int l = a.length();
		ToNum(a,A);
		ToNum(b,B);

		for(long X=A; X<=B; X++){
			if(ok[X]==false)
				check(X);
			sum;
		}
	
		cout << "Case #"<<k++<<": " << sum <<endl;
	

	
	
	
	}




	return 0;
}
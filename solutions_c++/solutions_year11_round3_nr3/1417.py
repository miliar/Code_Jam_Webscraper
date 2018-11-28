#include <iostream>
#include <fstream>
#include <vector>
#include <algorithm>
#include <string>
#include <map>
#include <set>
#include <stdio.h>
#include <limits.h>
#include <math.h>
#define For(I,A,B) for(int I = A; I < B; ++I)
using namespace std;

long long gcd(long long a,long long b){
	if (a > b) swap(a,b);
	while (b) {
		a %= b;
		b ^= a;
		a ^= b;
		b ^= a;
	}
	return a;
}
long long lcc(long long a, long long b){
	return (a/gcd(a,b))*b;
}
int main (){
	ifstream cin ("C-small-attempt0.in");
	ofstream cout ("output.txt");
	int T;
	cin >> T;
	cout.precision (8);
	For(t,1,T+1){
		int N;
		long long L,H,res = 1,G=1;
		cin >> 	N >> L >> H;
		vector <long long> q(N);
		For (i,0,N)
			cin >> q[i];
		bool isP = false;
		if (L == 1){
			isP = true;
			res =1;
		}
		else{
			For (i,0,N){
				res = lcc(G,q[i]);
			}
			for(long long i = L; i<=H; ++i){
				bool isG = true;
				For(j,0,N)
					if (i%q[j]==0 || q[j]%i==0)
						continue;
					else{
						isG = false;
						break;
					}
				if (isG){
					res = i;
					isP = true;
					break;
				}
			}
		}
		cout << "Case #" << t << ": ";
		if (isP)
			cout << res << endl;
		else
			cout << "NO" << endl;
	}
	return 0;
}
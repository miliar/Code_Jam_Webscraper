/*
 * E.cpp
 *
 *  Created on: 27-Apr-2012
 *      Author: ram
 */




#include <iostream>
#include <string>
#include <vector>
#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <sstream>
#include <cassert>
#include <algorithm>
#include <bitset>
using namespace std;

#define f(i,a,b) for(int  i = ( a ); i < ( b ); ++ i )
#define fo(i,b) f( i, 0, ( b ) )
#define mp make_pair
#define pb push_back
#define pob pop_back
#define all(v) (v).begin( ), (v).end( )
#define m memset
int N;
int A[1001][1001];


bitset<1001> b;
bool res = false;
void run(int a){
	int i=1;
	if (res == true) return;
			if (b.test(a)==1) {res = true; /*cout << a << " " << i << endl; */ return;}
			b.set(a,1);
	while(A[a][i]!=-1){
		run(A[a][i]);
		i++;
	}
}






int main(){
	int T;
	cin >> T;


	fo(i,T){
		res = false;
		cin >> N;
		m(A,0,1001*4);
		b.reset();
		fo(j,N){ int Mi=0; cin >> Mi; int k; for(k=0;k<Mi;k++){cin>>A[j+1][k+1];} A[j+1][k+1]=-1;}

		cout << "Case #" << i+1 << ": ";
		f(k,1,N+1){
			if (res == true) break;
			b.reset();
			run(k);
		}
		if (res == true) {cout << "Yes" << endl;}
		else cout << "No" << endl;
	}
}


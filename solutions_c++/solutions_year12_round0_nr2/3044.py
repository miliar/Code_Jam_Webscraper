/*
 * B.cpp
 *
 *  Created on: 14-Apr-2012
 *      Author: ram
 */

#include <iostream>
#include <string>
#include <vector>
#include <cstdio>
#include <cstring>
#include <stdlib.h>
using namespace std;

#define f(i,a,b) for( i = ( a ); i < ( b ); ++ i )
#define fo(i,b) f( i, 0, ( b ) )
#define mp make_pair
#define pb push_back
#define all(v) (v).begin( ), (v).end( )
#define m memset

int main(){
	int T;
	cin >> T;
	int i;
	fo(i,T){
		cout << "Case #" << i+1 << ": ";
		int N,S,p;
		int count=0;
		cin >> N >> S >> p;
		int j;
		fo (j,N){
			int n;
			cin >> n;

			int nn = n-p;
			if (nn >= p * 2 - 2){
				++count ;
			}
			else if (p-(nn-(p-1))<2 && nn-(p-1)>=0 && nn>=0) {++count;}
			else if (p-(nn-(p-2))<=2 && nn-(p-2)>=0 && nn>=0 && S>0){++count;--S;}

		}
		cout << count << endl;
	}
}


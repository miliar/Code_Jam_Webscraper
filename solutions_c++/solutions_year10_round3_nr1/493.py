/*
 * A.cpp
 *
 *  Created on: 22 mai 2010
 *      Author: Rafael
 */
#include<iostream>
#include<fstream>
#include<cmath>
#include<algorithm>
#include<vector>
#include<queue>
#include<map>
#include <set>
#define FOR(i,n) for(int (i) = 0; i < (n); (i)++)
using namespace std;
int N;
int A[1001];
int B[1001];

int intersect(int a , int b){
	if((A[a]<A[b]&&B[a]>B[b])||(A[a]>A[b]&&B[a]<B[b]))return 1;
	return 0;
}


int main(){
	int T;
	cin>>T;
	for(int t =1;t<=T;t++){
		cout<<"Case #"<<t<<": ";
		int ret = 0;
		cin>>N;
		FOR(i,N)
		cin>>A[i]>>B[i];
		for(int i = 0; i < N; i ++)
			for(int j =0; j < i; j++)
				ret+=intersect(i,j);
		cout<<ret<<"\n";
	}
	return 0;
}

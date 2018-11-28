/*
 * FreeCellStatistics.cpp
 *
 *  Created on: May 21, 2011
 *      Author: batchunag
 */

#include <iostream>
#include <algorithm>
#include <vector>
#include <map>
#include <utility>
#include <stdio.h>
#include <string.h>
#include <list>
#define FOR(i,a,b) for (int i=a; i<b; i++)
#define REP(i,n) for(int i=0;i<(int)n;++i)
#define mp make_pair
#define pb push_back

using namespace std;
typedef vector<int> VI;
typedef pair <int,int> PII;

int main(){
	freopen("input.txt","r",stdin);
	freopen("answer.txt","w",stdout);
	int T;
	cin>>T;
	for (int t=1; t<=T; t++){
		cout<<"Case #"<<t<<": ";
		int Pd,Pg;
		long long n;
		cin>>n>>Pd>>Pg;
		if (Pg==100){
			if (Pd!=100) cout<<"Broken";
			else cout<<"Possible";
			cout<<endl;
			continue;
		}
		if (Pg==0){
			if (Pd!=0) cout<<"Broken";
			else cout<<"Possible";
			cout<<endl;
			continue;
		}
		int k=__gcd(Pd,100);
		int D=100/k;
		if (D>n) cout<<"Broken";
		else cout<<"Possible";
		cout<<endl;
	}
	return 0;
}


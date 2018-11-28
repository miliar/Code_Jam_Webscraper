#include <algorithm>
#include <cmath>
#include <climits>
#include <complex>
#include <cstdio>
#include <cstdlib>
#include <iostream>
#include <map>
#include <queue>
#include <set>
#include <sstream>
#include <string>
#include <utility>
#include <vector>
using namespace std;

#define FOR(i,a,b) for(int i=(a);i<(b);i++)
#define REP(i,n) FOR(i,0,n)
#define MP make_pair

typedef long long LL;
typedef pair<int,int> PII;


const int NUM = 1000;

bool check(vector<int>input ) {
	int n = input.size();
	for(int a=0; a<n ;a++) for(int b=a+1; b<input[a]; b++){
		if(input[a]<input[b]) return false;
	} 
	
	return true;
}


int main() {
	int t;
	int T;
	cin>>t;
	T=t;
	for(;t;t--) {
		
		int n;
		cin>>n;
		
		vector<int>input;
		for(int a=0; a<n-1; a++) {
			int p;
			cin>>p;
			input.push_back(p-1);
		}
		if(!check(input)) {
			cout<<"Case #"<<T-t+1<<": "<<"Impossible"<<endl;
		}
		else  {
		/*
		vector<vector<int> > shison;
		for(int a=0; a<n; a++) {
			vector<int>tmp;
			shison.push_back(tmp);
		}
		for(int a=0; a<input.size(); a++) {
			shison[input[a]].push_back(a);
		}*/
		vector<int>now;
		vector<int>answer;
		for(int a=0; a<n; a++) {
			answer.push_back(-1);
			now.push_back(1);
		}
		answer[n-1] = 100000000;
		
		
		for(int a=0; a<n ; a++) for(int b=0; b<n; b++) if(answer[b]==-1) {
			if(answer[input[b]]!=-1) {
				int p = input[b];
				answer[b] = answer[p] - (p-b)*now[p];
				now[p]++;
				now[b] = now[p];
			}
		}
		cout<<"Case #"<<T-t+1<<": ";
		for(int a=0; a<n; a++) {
			cout<<answer[a];
			if(a==n-1) cout<<endl;
			else cout<<" ";
		}
		}
	
	}
	return 0;
	
}


 
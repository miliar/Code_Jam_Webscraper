/*
  Problem No : 
  Author     : Debashis Maitra
  Complexity :
  Date       :
*/

#include <cstdio>
#include <cstring>
#include <cmath>
#include <algorithm>
#include <cstdlib>
#include <ctype.h>
#include <iostream>
#include <map>
#include <set>
#include <vector>
#include <string>
#include <queue>
#include <stack>
#include <sstream>

using namespace std;

#define CLR(x) memset((x),0,sizeof(x))
#define pb push_back
#define sz size()
#define FOR(i,n) for(int i=0;i<n;i++)
#define FORALL(i,x) for(int i=0;i<x.size();i++)
#define FORALLR(i,x) for(int i=x.size()-1;i>=0;i--)
#define lint long long
#define MAX 1000
#define INF 1<<30

typedef vector<int> vi;
typedef vector<string> vs;

int cases,caseno;
long long group[1002];
long long n,k,r;
unsigned long long memo[1002];
bool used[1002];
int pre[1002];
long long t[1002];
int input(){
	cin>>r>>k>>n;
	CLR(memo);
	FOR(i,n){
		cin>>group[i+1];
	}
	return 1; 
}
void process(){
	int turn = 0;
	int next = 1;
	unsigned long long cost = 0;

	while( turn < r ){
		//if( memo[next] ) break;
		int peopleCnt = 0;
		int indx = next;
		CLR(used);
		t[indx] = turn  + 1;		
		while( peopleCnt + group[indx] <= k ){
			peopleCnt+=group[indx];
			used[indx] = 1;
			indx = ( indx + 1 ) % (n + 1);
			if(!indx) indx = 1;
			if(used[indx])break;
		}
		cost += peopleCnt;		

		if( !memo[indx] && indx != 1) {
			pre [indx]= next;				
		}		
		memo[next] = cost;
		next = indx ;
		turn++;
	}
	int remain = r - turn;	
	if( remain ){
		int roundCost = cost - memo [ pre[next] ] ;		
		int fullRound = turn - t[pre[next]] ;
		fullRound = remain / fullRound ;
		remain = remain % (turn - t[pre[next]]) ;
		cost+= roundCost*fullRound;

		while( remain-- ){
			int indx = next;
			int peopleCnt = 0;
			CLR(used);			
			while( peopleCnt + group[indx] <= k ){
				peopleCnt+=group[indx];
				used[indx] = 1;
				indx = ( indx + 1 ) % (n + 1);
				if(!indx) indx = 1;
				if(used[indx])break;
			}
			cost += peopleCnt;		
			next = indx ;
			turn++;
		}
	}

	cout<<"Case #"<<(++caseno)<<": "<<cost<<endl;
}
int main(){
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	cin>>cases;
	while(cases--){
		input();
		process();
	}
}

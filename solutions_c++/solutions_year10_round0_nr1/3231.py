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
long long n,k;
int input(){
	return 1; 
}
void process(){
	int div = 1;
	bool fail = false;
	FOR(i,n){
		if( !( (k/div) % 2 ) ) {
			fail = true;
			break;
		}
		div = div * 2;
	}
	cout<<"Case #"<<(++caseno)<<": ";
	if( fail ) cout<<"OFF"<<endl;
	else cout<<"ON"<<endl;
}
int main(){
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	cin>>cases;
	while(cases--){
		cin>>n>>k;
		process();
	}
}

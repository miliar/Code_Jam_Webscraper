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
int p,q;
vi r;
int mn;
int input(){
	cin>>p>>q;
	r.clear();
	int tmp;
	FOR(i,q){
		cin>>tmp;
		r.pb(tmp);
	}
	return 1; 
}
int getBribe(int x,int rel[]){
	int ret =0 ;
	for(int i=x+1;i<=p;i++){
		if(rel[i])break;
		ret++;
	}
	for(int i=x-1;i>0;i--){
		if(rel[i])break;
		ret++;
	}
	return ret;
}
void rec(int val, int rel[],int tot){
	int rls[200];
	if(tot>=q){
		mn=min(mn,val);
		return;
	}
	for(int i=0;i<200;i++){
		rls[i]=rel[i];
	}
	FORALL(i,r){
		if(rel[r[i]])continue;
		rls[r[i]]=1;
		rec(val+getBribe(r[i],rls),rls,tot+1);
		rls[r[i]]=0;
	}
}
void process(){
	int rel[200];
	CLR(rel);
	mn=INF;
	rec(0,rel,0);
	cout<<"Case #"<<(++caseno)<<": "<<mn<<endl;
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

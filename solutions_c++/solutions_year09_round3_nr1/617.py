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
#define lint unsigned long long
#define MAX 1000
#define INF 1<<30

typedef vector<int> vi;
typedef vector<string> vs;

int cases,caseno;
char s[500];
bool used[500];
vi bases;
int bVal[500];
int input(){
	gets(s);
	CLR(bVal);
	CLR(used);
	return 1; 
}
void markDgt(){
	bases.clear();
	for(int i=0;s[i];i++){
		if(!used[s[i]]){
			bases.pb((int)s[i]);
			used[s[i]]=1;
		}
	}

}
void process(){     
	markDgt();
	bVal[bases[0]]=1;
	if(bases.size()>1)bVal[bases[1]]=0;
	int val=2;
	for(int i=2;i<bases.size();i++){
		bVal[bases[i]]=val++;
	}
	int len=strlen(s);
	lint mul=1;
	int base=bases.size();
	if(base==1)base=2;
	lint res=0;
	for(int i=len-1;i>=0;i--){
		res=res+ (mul)* bVal[s[i]];
		mul=mul*base;
	}
	cout<<"Case #"<<(++caseno)<<": "<<res<<endl;
}
int main(){
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	cin>>cases;
	gets(s);
	while(cases--){
		input();
		process();
	}
}

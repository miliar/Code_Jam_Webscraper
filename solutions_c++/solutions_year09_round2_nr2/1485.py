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
#define lint long long
#define MAX 1000
#define INF 1<<30

typedef vector<int> vi;
typedef vector<string> vs;

int cases,caseno;
int dgts1[20];
int dgts2[20];
lint n;
char s[30];
char task[30];
int input(){
	cin>>n;
	return 1; 
}
void strRev(char *s,int len){

}
lint toInt(char *s,int len){
	lint ret=0;
	for(int i=len;i>=0;i--){
		ret=ret*10+s[i];
	}
	return ret;
}
void toDigit(lint n){
	CLR(dgts2);
	while(n){
		dgts2[n%10]++;
		n/=10;
	}
}
bool check(lint now){
	toDigit(now);
	if(now==14){
		now=now;
	}
	FOR(i,11){
		if(((!i)&&dgts1[i] && dgts1[i]>dgts2[i])||(i&&dgts1[i]!=dgts2[i]))return false;
		//if(dgts1[i] && dgts1[i]>dgts2[i])return false;
	}
	return true;
}
void process(){
	int i=0;
	lint now=n;
	lint tmp=n;
	CLR(dgts1);
	while(n){
		dgts1[n%10]++;
		n/=10;
	}
	while(1){
		now++;
		if(check(now))break;
	}
	cout<<"Case #"<<(++caseno)<<": "<<now<<endl;
	//cout<<tmp<<" Case #"<<(++caseno)<<": "<<now<<endl;
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

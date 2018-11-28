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
#define i64 long long
#define MAX 1000
#define INF 1<<30

typedef vector<int> vi;
typedef vector<string> vs;
int l,d,n;
char hav[100][30];
vs words;
int caseno;
string s;
int input(){
	string tmp;
	FOR(i,d){
		cin>>tmp;
		words.push_back(tmp);
	}
	return 1; 
}
void process(){
	int l=0;
	CLR(hav);
	for(int i=0;i<s.length();){
		if(s[i]=='('){
			i++;
			while(s[i]!=')'){
				hav[l][s[i]-'a']=1;
				i++;
			}
		}else hav[l][s[i]-'a']=1;
		l++;
		i++;
	}
	string str;
	int total=0;
	bool suc;
	FORALL(i,words){
		str=words[i];
		suc=true;
		for(int j=0;j<str.length();j++){
			if(!hav[j][str[j]-'a']){
				suc=false;
				break;
			}
		}
		if(suc)total++;
	}
	cout<<"Case #"<<(++caseno)<<": "<<total<<endl;
}
int main(){
	freopen("input.txt","r",stdin);
	freopen("outputL.txt","w",stdout);
	cin>>l>>d>>n;
	input();
	while(n--){
		cin>>s;
		process();
	}
}

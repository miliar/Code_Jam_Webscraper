#include <algorithm>
#include <cstdio>
#include <iostream>
#include <string>
#include <vector>

using namespace std;

string ss="welcome to code jam";
string s;
int cont;

void procesa(int n,int i){
	if(n==ss.length()){
		cont++;
		return;
	}
	if(i==s.length()) return;
	for(;i<s.length();i++){
		if(ss[n]==s[i]){
			procesa(n+1,i+1);
		}
	}
}

int main(){
	int n;
	//string s;
	scanf("%d\n",&n);
	for(int i=0;i<n;i++){
		cont=0;
		getline(cin,s);
		procesa(0,0);
		printf("Case #%d: %04d\n",i+1,cont%10000);
	}
	return 0;
}


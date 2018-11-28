#include <iostream>
#include <algorithm>
#include <vector>
#include <cstdio>
#include <string>
using namespace std;

int main(){
	int T,t;
	int i,j,k;
	string s;
	char S[] = "yhesocvxduiglbkrztnwjpfmaq";

	t = 1;
	scanf("%d",&T);
	getchar();	
	while(T--){
		getline(cin,s);
		for(i=0;i<s.size();i++){
			if(s[i] == ' ') continue;
			k = s[i] - 97;
			s[i] = S[k];
		}
		printf("Case #%d: %s\n",t,s.c_str());
		t++;
	}
	return 0;
}


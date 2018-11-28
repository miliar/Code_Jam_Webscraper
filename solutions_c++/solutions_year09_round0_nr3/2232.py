#include <cstdlib>
#include <cstdio>
#include <cstring>
#include <string>
#include <iostream>

using namespace std;

char pat[]="welcome to code jam";

int n, l;
int t[30];
string text;

int main(){
	l=strlen(pat);
	scanf("%d\n", &n);
	for(int i=0; i<n; i++){
		getline(cin, text);
		for(int j=0; j<30; j++) t[j]=0;
		t[0]=1;
		for(int j=0; j<text.size(); j++){
			for(int k=0; k<l; k++){
				if(pat[k]==text[j]){
					t[k+1]+=t[k];
					t[k+1]%=10000;
				}
			}
		}
		printf("Case #%d: ", i+1);
		if(t[l]<10) printf("0");
		if(t[l]<100) printf("0");
		if(t[l]<1000) printf("0");
		printf("%d\n", t[l]);
		
	}

}


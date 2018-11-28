#include <iostream>
#include <cmath>
#include <cstring>
using namespace std;

char s[111];
int n;

void go(int d){
	if(d==n){
		long long x = 0;
		for(int i=0;i<n;++i)
			x = x*2 + s[i]-'0';
		long long t = (long long)(sqrt(x)+1e-8);
		if(t*t==x)
			printf("%s\n",s );
		return;
	}
	if(s[d]=='?'){
		s[d]='0';
		go(d+1);
		s[d]='1';
		go(d+1);
		s[d]='?';
	}
	else{
		go(d+1);
	}
}

int main(){
	int t;
	cin >> t;
	for(int c=0;c<t;c++){
		printf("Case #%d: ", c+1);
		cin >> s;
		n = strlen(s);
		go(0);
	}
	return 0;
}

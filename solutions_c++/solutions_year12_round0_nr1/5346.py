#include<iostream>
#include<cstdio>
#include<string.h>
using namespace std;

#define GI ({int t;scanf("%d\n",&t);t;})

char s[1000001];

string magic = "yhesocvxduiglbkrztnwjpfmaq";

string replace(string in) {
	string out = in;
	for(int i = 0;i < out.size();++i){
		if(in[i] != ' ')
			out[i] = magic[in[i] - 'a'];
	}

return out;
}

int main() {
int nt = GI;
for(int t = 1;t <= nt;++t){
	gets(s);
	cout << "Case #"<<t<<": "<<replace(s)<<endl;	
}

return 0;
}

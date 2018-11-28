#include <iostream>
#include <cstdio>
using namespace std;
int main(int argc, char** argv) {
	char v[27] = "yhesocvxduiglbkrztnwjpfmaq";
	char in[101];
	char out[101];
	int tc,len,c;
	scanf("%d\n",&tc);
	for(int i=1;i<=tc;i++)
	{
		gets(in);
		for(len=0;in[len]!='\0';len++) {
			c = in[len]-'a';
			if(c >= 0) out[len] = v[c];
			else out[len] = in[len];
		}
		out[len] = '\0';
		printf("Case #%d: %s\n",i,out);
	}
	while(tc--);
	return 0;
}

#include <cstdio>
#include <cstring>
using namespace std;

char* ch="yhesocvxduiglbkrztnwjpfmaq";
int T;

int main()
{
	scanf("%d",&T);
	char str[110];
	gets(str);
	for (int cases=0;cases<T;++cases){
		gets(str);
		int len=strlen(str);
		for (int i=0;i<len;++i){
			if ((str[i]>='a')&&(str[i]<='z')) str[i]=ch[str[i]-'a'];
		}
		printf("Case #%d: %s\n",cases+1,str);
	}
	return 0;
}


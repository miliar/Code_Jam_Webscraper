#include <cstdio>
#include <iostream>
#include <cstring>
char map[26]={'y','h','e','s','o','c','v','x','d','u','i','g','l','b','k','r','z','t','n','w','j','p','f','m','a','q'};
char input[110];
int main(){
	int T,tt,len;
	int i;
	//freopen("a.in","r",stdin);
	//freopen("a.out","w",stdout);
	scanf("%d",&T);
	gets(input);
	for(tt=1;tt<=T;++tt){
		fgets(input,110,stdin);
		len=strlen(input);
		for(i=0;i<len;++i)
			if(input[i]>='a'&&input[i]<='z')input[i]=map[input[i]-'a'];
		printf("Case #%d: %s",tt,input);
	}
	return 0;
}
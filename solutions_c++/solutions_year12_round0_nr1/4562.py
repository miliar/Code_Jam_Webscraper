#include<stdio.h>
int main()
{
//	freopen("A-small-attempt0.in","r",stdin);
	char t[26]={'y','h','e','s','o','c','v','x','d','u','i','g','l','b','k','r','z','t','n','w','j','p','f','m','a','q'};
	int i=0,n,j;
	char s[101];
	scanf("%d",&n);
	getchar();
	while(i<n){
		gets(s);
		j=0;
		while((s[j]!='\0') && (j<100)){
			if(s[j] != ' ')s[j] = t[s[j]-'a'];
			j++;
		}
		printf("Case #%d: %s\n",i+1,s);
		i++;
	}
	return 0;
}


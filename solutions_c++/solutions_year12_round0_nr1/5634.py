#include<stdio.h>
#include<algorithm>
using namespace std;
char a[256];
char s[1024*100];
char s0[]="ejp mysljylc kd kxveddknmc re jsicpdrysirbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcdde kr kd eoya kw aej tysr re ujdr lkgc jvqz";
char s1[]="our language is impossible to understandthere are twenty six factorial possibilitiesso it is okay if you want to just give upzq";
void conv(char *s){
	int i;
	for(i=0;s[i];i++)
		if(s[i]>='a' && s[i]<='z')
			s[i]=a[s[i]];
}
int main(){
#ifdef _DEBUG
	freopen("in.txt","r",stdin);
	freopen("out.txt","w",stdout);
#endif
	int i,n;
	for(int i=0;s0[i];i++){
		if(s0[i]>='a' && s0[i]<='z')
			a[s0[i]]=s1[i];
	}

	scanf("%d\n",&n);
	for(i=0;i<n;i++){
		gets(s);
		conv(s);
		printf("Case #%d: ",i+1);
		puts(s);
	}

	

	return 0;
}
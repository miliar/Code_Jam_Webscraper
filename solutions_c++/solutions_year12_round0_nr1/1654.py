#include<stdio.h>
int main(){
	int n,i,t,j;
	freopen("A-small-attempt1.in","r",stdin);
	freopen("A-small-attempt1.txt","w",stdout);
	char c[210],d[]="yhesocvxduiglbkrztnwjpfmaq";
	scanf("%d",&n);
	gets(c);
	for(i=0;i<n;i++){
		gets(c);
		for(j=0;c[j]!=0;j++){if(c[j]!=' ')c[j]=d[c[j]-'a'];}
		printf("Case #%d: %s\n",i+1,c);
	}
	/*
	char c[1000],d[1000],e[100]={},q[100]={};
	int i;
	while(gets(c)){
		gets(d);
		for(i=0;c[i]!=0;i++){
			e[c[i]-'a']=d[i];
			q[d[i]-'a']=1;
		}
	}
	for(i=0;i<26;i++)printf("%c",e[i]);puts("");
	for(i=0;i<26;i++)if(q[i]==0)printf("%c\n",i+'a');
	scanf(" ");*/
} 

#include<stdio.h>
#include<iostream>
#include<algorithm>
#include<cmath>
#include<vector>
#include<cstdlib>
#include<stack>
#include<queue>
#include<string>
#include<cstring>


#define PR(x) printf(#x"=%d\n",x)
#define READ2(x,y) scanf("%d %d",&x,&y)
#define REP(i,a) for(int i=0;i<a;i++)
#define READ(x) scanf("%d",&x)
#define PRARR(x,n) for(int i=0;i<n;i++)printf(#x"[%d]=\t%d\n",i,x[i])
using namespace std;
int main() { 
char str[]="ejp mysljylc kd kxveddknmc re jsicpdrysi rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd de kr kd eoya kw aej tysr re ujdr lkgc jv";
char ans[]="our language is impossible to understand there are twenty six factorial possibilities so it is okay if you want to just give up";
char map[27];
for(int i=0;i<26;i++) map[i]='1';
int len=strlen(str);
for(int i=0;i<len;i++) {
if(str[i]!=' ')map[str[i]-'a']=ans[i];
}
map[25]='q';
map['q'-'a']='z';
int t;
scanf("%d",&t);
getchar();
char input[150];
for(int j=0;j<t;j++){
	fgets(input,150,stdin);
	int len=strlen(input);
	for(int i=0;i<len-1;i++) {
	if(input[i]!=' '&&input[i]!='\n')input[i]=map[input[i]-'a'];
	}
	input[len-1]='\0';
	printf("Case #%d: %s\n",j+1,input); 
	}	
//for(int i=0;i<26;i++) printf("%c:%c\n",'a'+i,map[i]);
}

#include<stdio.h>
#include<stdlib.h>
#include<string.h>
using namespace std;
#define N 26

int f[N];
char s1[] = "ejp mysljylc kd kxveddknmc re jsicpdrysi";
char s2[] = "rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd";
char s3[] = "de kr kd eoya kw aej tysr re ujdr lkgc jv";

char s1_r[] = "our language is impossible to understand";
char s2_r[] = "there are twenty six factorial possibilities";
char s3_r[] = "so it is okay if you want to just give up";

void init(char a[],char b[],int len){
	for( int i=0;i<len;++i ){
		if( b[i] != ' ' ) f[ a[i]-'a' ] = b[i]-'a';
	}
}

int main(){
	memset(f,-1,sizeof(f));
	init(s1,s1_r,strlen(s1));	
	init(s2,s2_r,strlen(s2));
	init(s3,s3_r,strlen(s3));
	f['z'-'a'] = 'q'-'a';
	f['q'-'a'] = 'z'-'a';
	/*
	for( int i=0;i<26;++i ){
		printf("%c -> %c\n",i+'a',f[i]+'a');
	}*/
	int t;
	//freopen("a.out","w",stdout);
	scanf("%d",&t);
	getchar();
	for( int _case=0;_case<t;++_case ){
		char tmpStr[200];
		gets(tmpStr);
		int tLen = strlen(tmpStr);
		printf("Case #%d: ",_case+1);
		//fprintf(stderr,"Case #%d: ",i+1);
		for( int i=0;i<tLen;++i ){
			if( tmpStr[i]!=' ' ){
				printf("%c",f[tmpStr[i]-'a']+'a');
				//fprintf(stderr,"%c",f[tmpStr[i]-'a']+'a');
			}else{
				printf(" ");
				//fprintf(stderr," ");
			}
		}
		printf("\n");
		//fprintf(stderr,"\n");
	}
	return 0;
}
/*
3
ejp mysljylc kd kxveddknmc re jsicpdrysi
rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd
de kr kd eoya kw aej tysr re ujdr lkgc jv
*/

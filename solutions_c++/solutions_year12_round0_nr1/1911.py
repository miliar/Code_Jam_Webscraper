#include<iostream>
#include<string.h>
#include<stdio.h>

using namespace std;
char kv[] = {
'y','h','e','s','o','c','v','x','d','u','i','g','l','b','k','r','z','t','n','w','j','p','f','m','a','q'	
};
int main()
{

	char s[11100],t[11100];
	FILE *r = fopen("A-small-attempt1.in","r");
	FILE *w = fopen("ans.txt","w");
	int cas;
	fscanf(r,"%d",&cas);
	int c = 0;
	fscanf(r,"%c");
	while(fgets(s,10000,r)){
		
		int i;
		for(i=0;s[i];i++){
			if(s[i]!=' ')
				t[i]=kv[s[i]-'a'];
			else t[i]=' ';
		}
		t[i]=0;
		
		c++;
		fprintf(w,"Case #%d: %s\n",c,t);
	}

	
}
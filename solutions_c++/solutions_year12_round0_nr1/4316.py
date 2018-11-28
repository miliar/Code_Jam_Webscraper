#include<iostream>
#include<cstdio>
#include<cstring>
using namespace std;

char b[27]="ynficwlbkuomxsevzpdrjgthaq";
char a[27];
int main(){
	int n;
	char c;
	for(int i=0;i<27;i++)
		a[b[i]-'a']=i+'a';
	scanf("%d",&n);
	getchar();
	for(int i=1;i<=n;i++){
		printf("Case #%d: ",i);
		while((c=getchar())!='\n')
			if(c==' ') printf(" ");
			else printf("%c",a[c-'a']);
		printf("\n");
	}
	return 0;
}

#include<iostream>
#include<cstdio>
#include<cstring>
using namespace std;


char a[30]="yhesocvxduiglbkrztnwjpfmaq";
int main(){
	int i,j,k,m,n,r,c;
	char ch;
	freopen("A-small-attempt0.in","r",stdin);
	freopen("out.txt","w",stdout);
	scanf("%d",&r);
	getchar();
	for(c=1;c<=r;++c){
		printf("Case #%d: ",c);
		while(scanf("%c",&ch)==1){
			if(ch==' ')	printf(" ");
			else if(ch=='\n'){
				printf("\n");
				break;
			}
			else	printf("%c",a[ch-'a']);
		}
	}
	
}
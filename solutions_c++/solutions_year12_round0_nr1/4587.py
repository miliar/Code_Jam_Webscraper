#include<iostream>
#include<stdio.h>
#include<string.h>
using namespace std;

char mapping[26]={'y','h','e','s','o','c','v','x','d','u','i','g','l','b','k','r','z','t','n','w','j','p','f','m','a','q'};
int main(){
	int T;
	int len;int i,j;
	scanf("%d",&T);
	cin.get();
	for(j=1;j<=T;j++){
	char G[102];
		cin.getline(G,102);
		len = strlen(G);
		//cout<<G;
		//cout<<len;
		printf("Case #%d: ",j); 
		for (i=0;i<len;i++){
			if (G[i] >= 97 && G[i] <= 122)
			 printf ("%c",mapping[(int)(G[i])-97]);
			else if (i!=len-1)
			 	printf(" ");
			
			
		}
		printf("\n");
	}
}

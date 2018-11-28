#include <stdio.h>
#include <string.h>

int map[26]={'y', 'h', 'e' ,'s', 'o', 'c', 'v', 'x', 'd', 'u', 'i', 'g', 'l', 'b', 'k', 'r', 'z', 't', 'n', 'w', 'j', 'p', 'f', 'm', 'a', 'q'};
char G[102];

int main(int argc, char** argv){
	int i,T,j;
	freopen("input.in","r",stdin);
	freopen("output.out","w",stdout);
	scanf("%d",&T);
	getchar();
	for(i=1; i<=T; i++){
		gets(G);
		j=0;
		while( G[j]!='\0' ){
			if(G[j]!=' ')
				G[j]=map[G[j]-'a'];
			j++;
		}
		printf("Case #%d: %s\n",i,G);
	}
	return 0;
}
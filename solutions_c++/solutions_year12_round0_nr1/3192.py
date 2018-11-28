using namespace std;
#include<iostream>
#include<cstdio>
#include<cstdlib>

int main()
{
	freopen("A-small-attempt0.in","r",stdin);
	freopen("out.txt","w",stdout);
	int n;
	scanf("%d\n",&n);
	char map[26]={'y','h','e','s','o','c','v','x','d','u','i','g','l','b','k','r','z','t','n','w','j','p','f','m','a','q'};
	for(int k=0;k<n;k++){
		char inp[101];
		gets(inp);
		printf("Case #%d: ",k+1);
		for(int i=0;inp[i]!='\0';i++){
			if(inp[i]==' ')
				printf(" ");
			else
				printf("%c",map[inp[i]-97]);
		}
		printf("\n");
	}
	return 0;
}

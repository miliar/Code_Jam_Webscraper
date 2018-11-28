#include<iostream>
#include<stdio.h>

using namespace std;

char m[] = {'y','h','e','s','o','c','v','x','d','u','i','g','l','b','k','r','z','t','n','w','j','p','f','m','a','q' };
char A[105];

int main()
{
	freopen("tc.in","r",stdin);
	freopen("tc.out","w",stdout);
	int t;
	scanf("%d\n",&t);
	for(int k=1;k<=t;k++){
		int l = 0;
		char c;
		while(true){
			c = getchar();
			if(c == '\n') break;
			A[l++] = c;
		}


		printf("Case #%d: ",k);
		for(int i=0;i<l;i++){
			if(A[i] != ' ')
				printf("%c",m[ A[i] - 'a' ]);
			else printf(" ");
		}
		printf("\n");
	}
	return 0;
}
#include <iostream>
#include <stdio.h>

using namespace std;

int main()
{
	char A[] = {'y','h','e','s','o','c','v','x','d','u','i','g','l','b','k','r','z','t','n','w','j',
			'p','f','m','a','q'};

	int n;
	char ch;

	scanf("%d",&n);
	getchar();
	for(int i = 1 ; i <= n ; i++){
		printf("Case #%d: ",i);
		while((ch = getchar()) != '\n'){
			printf("%c",(ch == ' ')? ' ':A[ch-'a']);
		}
		printf("\n");
	}
	return 0;
}


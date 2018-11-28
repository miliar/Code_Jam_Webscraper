#include <stdio.h>
#include <string.h>
#include <iostream>

using namespace std;

int main(){
	int Case, i, j, A, B, len, temp, count = 0, c_count=1;
	char test[10], copy[10];

	freopen("C-large.in", "r", stdin);
	freopen("C-large.out", "w", stdout);
	scanf_s("%d\n", &Case);

	while(Case--){
		scanf_s("%d %d", &A, &B);
		count = 0;
		for(i = A; i <= B; i++){
			itoa(i, test, 10);
			strcpy(copy, test);
			len = strlen(test);

			do{
				temp = copy[len-1];
				for(j=len-1; j>0; j--)
					copy[j] = copy[j-1];
				copy[0] = temp;

				if(atoi(copy) >= A && atoi(copy) <= B && atoi(test) != atoi(copy))
					count++;
			}while(strcmp(test, copy));
		}
		count /= 2;
		printf("Case #%d: %d\n", c_count, count);
		c_count++;
	}
	return 0;
}
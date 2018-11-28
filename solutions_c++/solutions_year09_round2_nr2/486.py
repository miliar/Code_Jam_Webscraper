#include <stdio.h>
#include <stdlib.h>
#include <algorithm>

using namespace std;

int main() {

    int testCases;
	scanf("%d", &testCases);
	
	for (int i = 0; i < testCases; i++) {
	    char number[21];	
		
		scanf("%s", &number);
		int length = 0;
		while (number[length] != '\0') length++;					
		
		if (next_permutation(number, number + length)) {
			printf("Case #%d: %s\n", (i+1), number);
		} else {
			sort(number, number+length);
		    printf("Case #%d: ", (i+1));
			int index = 0;
			while (number[index] == '0') {
				index++;
			}
			int contZeros = index+1;
			
			printf("%c", number[index]);
			for (int i = 0; i < contZeros; i++) {
				printf("0");
			}
			for (int i = index+1; i < length; i++) {
				printf("%c", number[i]);
			}				
			printf("\n");
		}
	}
    return 0;
}

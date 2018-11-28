/*
 * Google Code Jam 2012 - Qualification Round
 */

#include <stdio.h>
#include <string.h>

#define MAX_INPUT_LEN 200

int main() {

	int test_no;
	char text[MAX_INPUT_LEN];
	
	char * mapping = "yhesocvxduiglbkrztnwjpfmaq";

	// Obtain the test number.
	scanf("%d\n", &test_no);

	// Loop each sentence.
	for(int i = 0; i < test_no; i++) {

		fgets(text, MAX_INPUT_LEN, stdin);

		int len = strlen(text);
		for(int j = 0; j < len; j++) {
			if(text[j] >= 'a' && text[j] <= 'z') {
				text[j] = mapping[text[j] - 'a'];
			}
		}

		printf("Case #%d: %s", i+1, text);
	}

	return 0;
}
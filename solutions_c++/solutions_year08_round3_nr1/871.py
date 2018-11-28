/* Compile g++ main.c -o main */
#include <stdio.h>
#include <iostream>
#include <algorithm>
#include <string>

using namespace std;

int main() {
	/* Initialize the variables */
	int num_cases, max_keysize, max_keys, max_letters;
	
	/* SOLVE EVERY INSTANCE */
	scanf("%d\n", &num_cases);
	for(int casee=1;casee<=num_cases;casee++) {

		/* Read the input */
		scanf("%d %d %d\n", &max_keysize, &max_keys, &max_letters);
		int *alphabet = new int(max_letters);
		int *alphabet_sorted = new int(max_letters);
		bool *alpha = new bool(max_letters);
		
		for(int i=0; i<max_letters; i++) {
			alpha[i] = false;
			cin >> alphabet[i];
		}
		
		sort (alphabet, alphabet+max_letters);
		
		int inc=1;
		int max_presses=0;
		int count =0;

		for(int i=max_letters-1; i>=0; i--) {
			if(count == max_keys) {
				inc++;
				count=0;
			}
			max_presses=max_presses+inc*alphabet[i];
			count++;
		}
		/* Output the desired results */
		printf("Case #%d: %d\n", casee, max_presses);
		
		delete alphabet;
		delete alphabet_sorted;
		delete alpha;
	}
	return 0;
}

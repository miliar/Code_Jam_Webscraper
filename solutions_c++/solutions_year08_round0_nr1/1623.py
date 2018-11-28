/* Compile g++ main.c -o main */
#include <stdio.h>
#include <iostream>
#include <string>

#define MAX_NUM_ENGINES 101

using namespace std;

int main() {
	/* Initialize the variables */
	int num_cases,num_engines,num_queries;
	string engines[MAX_NUM_ENGINES];
	
	/* SOLVE EVERY INSTANCE */
	cin >> num_cases;
	for(int casee=1;casee<=num_cases;casee++) {
		/* Read the input */
		scanf("%d\n", &num_engines);
		for(int i=0;i<num_engines;i++) {
			getline(cin,engines[i]);
		}
		scanf("%d\n", &num_queries);

		/* Solve the problem and read the queries on the fly */
		int *max_possible = new int[num_engines];
		// Set all the stats to equal 0
		for(int i=0;i<num_engines;i++) {
			max_possible[i] = 0;
		}
		int counter =0;
		// Read all the queries for this instance and solve for each
		for(int i=0;i<num_queries;i++) {
			// Read and count a set that can be executed on a single engine 
			string query;
			getline(cin,query);
			for(int j=0;j<num_engines;j++) {
				if(engines[j] == query) {
					max_possible[j]++;
					break;
				}
			}
			// Check if we need to change the engine
			bool switch_server = true;
			for(int j=0;j<num_engines;j++) {
				if(max_possible[j] == 0) {
					switch_server = false;
					break;
				}
			}
			// Change the engine and reset the stats for a new count
			if(switch_server == true) {
				for(int j=0;j<num_engines;j++) {
					max_possible[j] =0;
					if(engines[j] == query) {
						max_possible[j]=1;
					}
				}
				counter++;
			}
		}
			
		/* Output the desired results */
		printf("Case #%d: %d\n", casee, counter);
		
		/* Free memory */
		delete max_possible;
	}
	return 0;
}

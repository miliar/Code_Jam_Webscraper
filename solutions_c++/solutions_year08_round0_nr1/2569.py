//============================================================================
// Name        : saving_the_universe.cpp
// Author      : Jestine Paul
//============================================================================

#include <iostream>
#include <cstdio>

using namespace std;

int NumOfEngineSwitches(char(*engines)[100], int num_of_engines,
		char(*queries)[100], int num_of_queries);

int main(int argc, char *argv[]) {

	FILE *ifp;
	FILE *ofp;

	if ((ifp = fopen(argv[1], "r")) == NULL) {
		printf("can't open %s\n", argv[1]);
		return 1;
	}

	if ((ofp = fopen(argv[2], "w")) == NULL) {
		printf("can't write %s\n", argv[2]);
		return 1;
	}

	int num_of_test_cases;
	fscanf(ifp, "%d\n", &num_of_test_cases);

	int num_of_engines;
	char engines[100][100];
	int num_of_queries;
	char queries[1000][100];

	for (int i = 0; i < num_of_test_cases; i++) {

		fscanf(ifp, "%d\n", &num_of_engines);

		for (int j = 0; j < num_of_engines; j++) {
			fgets(engines[j], 100, ifp);
		}

		fscanf(ifp, "%d\n", &num_of_queries);

		for (int j = 0; j < num_of_queries; j++) {
			fgets(queries[j], 100, ifp);
		}

		fprintf(ofp, "Case #%d: %d\n", i+1, NumOfEngineSwitches(engines, num_of_engines, queries,
				num_of_queries));


	}

	return 0;
}

int NumOfEngineSwitches(char(*engines)[100], int num_of_engines,
		char(*queries)[100], int num_of_queries) {

	int counter = 0;
	int num_of_engines_not_queried = num_of_engines;
	bool engines_queried[num_of_engines];

	for(int i = 0; i < num_of_engines; i++)
		engines_queried[i] = false;

	int j;
	for (int i = 0; i < num_of_queries; i++) {
		for (j = 0; j < num_of_engines; j++) {
			if (strcmp(queries[i], engines[j]) == 0)
				break;
		}
		if(engines_queried[j] == false) {
			engines_queried[j] = true;
			--num_of_engines_not_queried;
		}

		if(num_of_engines_not_queried == 0){
			++counter;
			num_of_engines_not_queried = num_of_engines - 1;
			for(int i = 0; i < num_of_engines; i++)
					engines_queried[i] = false;
			engines_queried[j] = true;
		}

	}

	return counter;
}

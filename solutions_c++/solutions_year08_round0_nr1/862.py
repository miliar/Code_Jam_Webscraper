#include <stdio.h>
#include <string.h>
#include <limits.h>

/*void debugPrint (vector< vector<int> > *switch_count, vector<int> &queries, map<string, int> &engines) {
	printf("engines:\n");
	for(int i=0; i<engines
}*/

char* trim (char *str) {
	while(strlen(str) > 0 && (str[strlen(str)-1] == '\n' || str[strlen(str)-1] == '\r')) {
		str[strlen(str)-1] = '\0';
	}
	return str;
}

int processCase (FILE *fp) {
	int		S, Q;
	int		**switch_count;
	int		*queries;
	char	**engines;
	char	buffer[1024];

	fscanf(fp, "%d\n", &S);
	engines = new char*[S];
	for(int i=0; i<S; i++) {
		engines[i] = new char[1024];
		fgets(engines[i], 1024, fp);
		trim(engines[i]);
	}

	fscanf(fp, "%d\n", &Q);
	if(Q == 0) {
		for(int i=0; i<S; i++)
			delete engines[i];
		delete [] engines;
		return 0;
	}
	queries = new int[Q];
	switch_count = new int*[Q];
	for(int i=0; i<Q; i++) {
		fgets(buffer, 1024, fp);
		trim(buffer);
		for(int j=0; j<S; j++) {
			if(strcmp(buffer, engines[j]) == 0) {
				queries[i] = j;
				break;
			}
		}

		switch_count[i] = new int[S];
		for(int j=0; j<S; j++) {
			if(queries[i] == j)
				switch_count[i][j] = -1;
			else
				switch_count[i][j] = 0;
		}
	}

	for(int i=1; i<Q; i++) {
		for(int j=0; j<S; j++) {

			if(queries[i] == j)
				switch_count[i][j] = -1;
			else {
				int	min = INT_MAX, min_k;
				for(int k=0; k<S; k++) {
					if(k == j && switch_count[i-1][k] != -1 && switch_count[i-1][k] < min) {
						min = switch_count[i-1][k];
						min_k = k;
					} else if(k != j && switch_count[i-1][k] != -1 && switch_count[i-1][k] + 1 < min) {
						min = switch_count[i-1][k] + 1;
						min_k = k;
					}
				}
				switch_count[i][j] = min;
			}
		}
	}

	int	result = INT_MAX;
	for(int i=0; i<S; i++) {
		if(switch_count[Q-1][i] != -1 && switch_count[Q-1][i] < result)
			result = switch_count[Q-1][i];
	}

	for(int i=0; i<S; i++)
		delete [] engines[i];
	for(int i=0; i<Q; i++)
		delete [] switch_count[i];
	delete [] switch_count;
	delete [] engines;
	delete [] queries;

	return result;
}

int main (int argc, char **argv) {
	if(argc != 2) {
		printf("Usage: a.out input_file\n");
		return -1;
	}

	// Read input
	FILE	*fp = fopen(argv[1], "r");
	int		N, result;
	
	fscanf(fp, "%d\n", &N);
	for(int i=0; i<N; i++) {
		result = processCase(fp);
		printf("Case #%d: %d\n", i+1, result);
	}

	fclose(fp);

	return 0;
}


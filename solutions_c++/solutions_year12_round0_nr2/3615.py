#include <iostream>
#include <map>
#include <vector>
using namespace std;

int main() {
    FILE * input;
    input = fopen("B-large.in", "r");
    FILE * output;
    output = fopen("B-large.out", "w");
    
    int T;    	  // num cases
    int G;		  // num googlers
    int S;		  // num of surprising triplets
    int P;		  // P value
    int i, j;  // iterators
    int result;	  // result
    int n;
    int min;
    
    fscanf(input, "%d\n", &T);
    for(i = 1; i <= T; i++)
    {
		result = 0;
		fscanf(input, "%d ", &G);
		fscanf(input, "%d ", &S);
		fscanf(input, "%d ", &P);
		min = 3*P-2;
		for(j = 0; j < G; j++) {
			fscanf(input, "%d ", &n);
			if(n >= min) {
				result++;
			} else if(n > 0 && (n == min-1 || n == min-2)) {
				if(S > 0) {
					result++;
					S--;
				}
			}
		}
		fprintf(output, "Case #%d: %d\n", i, result);
	}
	
	cout << "Solved";
	getchar();
	return 0;
}

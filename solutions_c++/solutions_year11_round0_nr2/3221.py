#include <stdlib.h>
#include <stdio.h>
#include <vector>

using namespace std;

const char inFileName[] = "B-large.in";
const char outFileName[] = "B-large.out";

const int L = 26;
const int MaxN = 1000;

int T, n, c, d;
int make[L][L];
int count[L];
bool opposed[L][L];
char s[MaxN];
vector<int> stack;

int val(char a) {
	return (a - 65);
}

int main() {
	
	FILE* inFile = fopen(inFileName, "r");
	FILE* outFile = fopen(outFileName, "w");
	
	fscanf(inFile, "%d", &T);
	for (int t = 0; t < T; t++) {
		
		for (int i = 0; i < L; i++)
			for (int j = 0; j < L; j++) {
				make[i][j] = -1;
				opposed[i][j] = false;
			}
		for (int i = 0; i < L; i++) count[i] = 0;

		fscanf(inFile, "%d", &c);
		
		for (int i = 0; i < c; i++) {
			fscanf(inFile, "%s", s);
			make[val(s[0])][val(s[1])] = val(s[2]);
			make[val(s[1])][val(s[0])] = val(s[2]);
		}

		fscanf(inFile, "%d", &d);
		for (int i = 0; i < d; i++) {
			fscanf(inFile, "%s", s);
			opposed[val(s[0])][val(s[1])] = true;
			opposed[val(s[1])][val(s[0])] = true;
		}

		fscanf(inFile, "%d", &n);
		fscanf(inFile, "%s", s);
		
		stack.clear();
		for (int i = 0; i < n; i++) {
			stack.push_back(val(s[i]));
			count[ val(s[i]) ]++;
			int m = stack.size();

			if (m > 1 && make[stack[m - 2]][stack[m - 1]] != -1) {
				int x = make[stack[m - 2]][stack[m - 1]];
				count[ stack[m - 2] ]--;
				count[ stack[m - 1] ]--;
				count[x]++;
				stack.pop_back(); 
				stack.pop_back();
				stack.push_back(x);
			}
			else {
				bool ok = true;
				for (int j = 0; j < L && ok; j++)
					if (count[j] > 0 && opposed[j][val(s[i])]) {
						ok = false;
						stack.clear();
						for (int k = 0; k < L; k++) count[k] = 0;
					}
			}
		}

		fprintf(outFile, "Case #%d: ", t + 1);
		if (stack.size() == 0) fprintf(outFile, "[]\n");
		else {
			fprintf(outFile, "[");
			for (int i = 0; i < stack.size() - 1; i++)
				fprintf(outFile, "%c, ", stack[i] + 65);
			fprintf(outFile, "%c]\n", stack[stack.size() - 1] + 65);
		}
	}	
	
	fclose(inFile);
	fclose(outFile);
	return 0;
}

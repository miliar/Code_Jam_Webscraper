#include <iostream.h>
#include <math.h>
#include <vector.h>
#include <set.h>

int areRecycled(vector<int>&, vector<int>&);
void num2vector(vector<int>&, int);

int main() {
    FILE * input;
    input = fopen("C-small-attempt1.in", "r");
    FILE * output;
    output = fopen("C-small-attempt1.out", "w");
    
    int T;    	  // num cases
    int A, B;  	  // string
    int i, j, k;  // iterators
    int recycleds;// num recycleds
    
    // get number of cases
    fscanf(input, "%d\n", &T);
    
    for(i = 1; i <= T; i++)
    {
		recycleds = 0;
		fscanf(input, "%d ", &A);
		fscanf(input, "%d\n", &B);
		for(j = A; j < B; j++) {
			for(k = j+1; k <= B && (int)log10(j) == (int)log10(k); k++) {
				vector<int> a;
				vector<int> b;
				num2vector(a, j);
				num2vector(b, k);
				recycleds += areRecycled(a, b);
			}
		}
		fprintf(output, "Case #%d: %d\n", i, recycleds);
	}
	
	printf("Solved");
	getchar();
	return 0;
}

void num2vector(vector<int> &v, int n) {
	while(n > 0) {
		v.insert(v.begin(), n % 10);
		n = n / 10;
	}
}

int areRecycled(vector<int> &n, vector<int> &m) {
	if(n[0] == 0 || n.size() != m.size()) {
		return 0;
	} else {
		int i, j;
		int flag;
		for(i = 0; i < n.size(); i++)
		{
			flag = 1;
			for(j = 0; j < n.size(); j++) {
				if(n[j] != m[j]) {
					// take one in the back to the front
					n.insert(n.begin(), n[n.size()-1]);
					n.pop_back();
					flag = 0;
					break;
				}
			}
			if(flag == 1) {
				return 1;
			}
		}
		return 0;
	}
}

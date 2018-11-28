#include <stdio.h>
#include <math.h>
#include <stdlib.h>

#include <map>
#include <vector>
#include <iostream>
#include <string>

using namespace std;

#define MAX 1000
#define PI 3.141592653589793238

vector<int> vi;
vector<string> vs;
vector<long long> vll;
map<string, int> lut;

string MORSE[] = {".-", "-...", "-.-.", "-.."};

int compare(const void *a, const void *b) {
	return ( *(long*)a - *(long*)b);
}

int main(int argc, char **argv) {

int num,len;
	
scanf("%d", &num);

int i,j,k,p,q;
long A[MAX], B[MAX];

for(i=1;i<=num;i++) {

	scanf("%d", &len);

	for(k=0;k<len;k++) scanf("%d",&A[k]);
	for(k=0;k<len;k++) scanf("%d",&B[k]);

	qsort(A, len, sizeof(long), compare);
	qsort(B, len, sizeof(long), compare);

	long long sum = 0;
	for(k=0;k<len;k++) {
		sum += A[k]*B[len-k-1];
		//printf("mult %d, %d\n", A[k],B[len-k-1]);
	}

	printf("Case #%d: %ld\n",i, sum);


} //for

} //main

/*
 *  r2_A.cpp
 *
 */


#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cassert>

// return the last postion of '1' in str
int get_last_pos(char* row) {
	int len = strlen(row), pos=-1;
	for(int i=0; i<len; i++) 
		if(row[i]=='1') pos=i;
	return pos;
}

// return the #of minimum swaps to make
int get_min(int* arr, int len) {
	int sum = 0; 
	for(int i=0; i<len-1; i++) { 
		// cont the inversions of arr[i]
		int last_counted = arr[i]; 
		for(int j=i+1; j<len; j++) {
			if(arr[j]!=last_counted && arr[j]<arr[i]) {
				last_counted = arr[j]; 
				sum++;
			}
		}
	}
	return sum;
}

// process the case_numth case
void proc_case(int case_num)  {
	int n, num[40]; scanf("%d\n", &n); 
	char row[45]; 
	for(int i=0; i<n; i++) {
		fgets(row, 45, stdin); 
		num[i] = get_last_pos(row);
	}
	printf("Case #%d: %d\n", case_num, get_min(num, n)); 
}

// our main function
int main( int argc, const char* argv[] ) {
	if(argc>1) assert(freopen(argv[1], "r",stdin));
	
	int case_num; scanf("%d", &case_num); 
	for(int k=0; k<case_num; k++)
		proc_case(k+1);
	
	return 0;
}
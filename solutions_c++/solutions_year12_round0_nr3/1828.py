#include <iostream>
#include <cstdlib>
#include <cstdio>
#define MAX(a,b) ((a)>(b)?(a):(b))
#define MIN(a,b) ((a)<(b)?(a):(b))

using namespace std;

const int EXP[] = {1, 1e1, 1e2, 1e3, 1e4, 1e5, 1e6, 1e7, 1e8, 1e9};
const int PER[][10] = {{},
	{0, 1, 11, 111, 1111, 11111, 111111, 1111111, 11111111, 111111111},
	{0, 1, 101, 10101, 1010101},
	{0, 1, 1001, 1001001} };

int compute(int A, int B, int len);

int per(int A, int B, int len, int k) {
	int num = B/EXP[len-k] - A/EXP[len-k] - 1;
	if (A/EXP[len-k] == B/EXP[len-k]) {
		num++;
	    if (A/EXP[len-k]*PER[k][len/k] >= A && 
	    	B/EXP[len-k]*PER[k][len/k] <= B) num++;
	} else {
		if (A/EXP[len-k]*PER[k][len/k] >= A) num++;
		if (B/EXP[len-k]*PER[k][len/k] <= B) num++;
	}	
	return num;
}

int stejne(int A, int B, int len, int k) {
	if (A/EXP[len-k] == B/EXP[len-k]) return 0;
	int nA = A/EXP[len-k], nB = B/EXP[len-k];
	if (nA*PER[k][len/k] < A) nA++;
	if (nB*PER[k][len/k] > B) nB--;
	return compute(nA, nB, k);
}

int compute(int A, int B, int len) {
	int result = 0;
	for (int k=1; k<len; k++){
		for (int c=0; c<16; c++){
			int xmin = 0, xmax = EXP[9], ymin = 0, ymax = EXP[9];
			if (c%2==0){
				xmin = A/EXP[len-k]+1;
			} else {
				xmin = xmax = A/EXP[len-k]; 
				ymin = A%EXP[len-k];
			}
			if ((c>>1)%2==0){
				xmax = MIN(xmax, B/EXP[len-k]-1);
			} else {
				xmax = MIN(xmax, B/EXP[len-k]);
				xmin = MAX(xmin, B/EXP[len-k]);
				ymax = MIN(ymax, B%EXP[len-k]);
			}
			if ((c>>2)%2==0){
				ymin = MAX(ymin, A/EXP[k]+1);
			} else {
				ymin = MAX(ymin, A/EXP[k]);
				ymax = MIN(ymax, A/EXP[k]);
				xmin = MAX(xmin, A%EXP[k]);
			}
			if ((c>>3)%2==0){
				ymax = MIN(ymax, B/EXP[k]-1);
			} else {
				ymin = MAX(ymin, B/EXP[k]);
				ymax = MIN(ymax, B/EXP[k]);
				xmax = MIN(xmax, B%EXP[k]);
			}
			if (xmax >= xmin && ymax >= ymin)
				result += (xmax-xmin+1)*(ymax-ymin+1);
		}
	}
	int res = result;
	switch(len){
		case 2: case 3: case 5: case 7:
			result -= (len-1)*per(A, B, len, 1);
		break;
		case 4:
			result -= per(A, B, len, 2) + 2*per(A, B, len, 1); 
			result -= 2*stejne(A, B, len, 2);
		break;
		case 6:
			result -= per(A, B, len, 3) + 2*per(A, B, len, 2) + 2*per(A, B, len, 1);
			res = result;
			result -= 4*stejne(A, B, len, 2) + 2*stejne(A, B, len, 3);
		break;
	}
	return result/2;
}

int main(void) {
	int testcase;
	scanf("%d", &testcase);
	for (int case_id=1; case_id<=testcase; case_id++) {
		int A, B, len=0;
		scanf("%d %d", &A, &B);
		int tmp = A;
		while (tmp > 0) {
			len++;
			tmp /= 10;
		}
		printf("Case #%i: %i\n", case_id, compute(A, B, len));
	}
	return 0;
}

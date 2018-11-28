#include <stdio.h>
#include <stdlib.h>
#include <iostream>
#include <string>

using namespace std;

int main() {
  long n;

  scanf("%ld\n", &n);

  for (long i = 0; i < n; i++) {
	long na, nb, t;
	
	scanf("%ld\n", &t);
	
	scanf("%ld %ld\n", &na, &nb);
	
	long A[na][2], B[nb][2];
	for (long j = 0; j < na; j++) {
		long a, b, c, d;
		scanf("%ld:%ld %ld:%ld\n", &a, &b, &c, &d);
		A[j][0] = a*60 + b;
		A[j][1] = c*60 + d;
	}
	for (long j = 0; j < nb; j++) {
		long a, b, c, d;
		scanf("%ld:%ld %ld:%ld\n", &a, &b, &c, &d);
		B[j][0] = a*60 + b;
		B[j][1] = c*60 + d;
	}

	long NA = na, NB = nb;
	
	long flagB[nb];
	for (long j = 0; j < nb; j++)
		flagB[j] = 0;
		
	for (long j = 0; j < na; j++)
		for (long k = j+1; k < na; k++)
			if (A[j][1] < A[k][1]) {
				long temp = A[j][1];
				A[j][1] = A[k][1];
				A[k][1] = temp;
			}
	
	for (long j = 0; j < na; j++)
		for (long k = 0; k < nb; k++) {
			if (flagB[k] == 1)
				continue;
			if (A[j][1] + t <= B[k][0]) {
				flagB[k] = 1;
				NB--;
				break;
			}
		}

	long flagA[nb];
	for (long j = 0; j < na; j++)
		flagA[j] = 0;
		
	for (long j = 0; j < nb; j++)
		for (long k = j+1; k < nb; k++)
			if (B[j][1] < B[k][1]) {
				long temp = B[j][1];
				B[j][1] = B[k][1];
				B[k][1] = temp;
			}
	
	for (long j = 0; j < nb; j++)
		for (long k = 0; k < na; k++) {
			if (flagA[k] == 1)
				continue;
			if (B[j][1] + t <= A[k][0]) {
				flagA[k] = 1;
				NA--;
				break;
			}
		}


	cout << "Case #" << i+1 << ": " << NA << " " << NB << endl;
  }

  return 0;
}

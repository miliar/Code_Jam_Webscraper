#include <iostream>
#include <algorithm>
#include <cstdio>

using namespace std;

void makeTest() {
	int T = 15;
	cout << T << endl;
	
	for (int i = 0; i < T; i++) {
		int N = rand() % 500 + 501;
		
		cout << N << endl;
		for (int j = 0; j < N; j++) {
			int A, B;
			A = rand() % 10000 + 1;
			B = rand() % 10000 + 1;			
			
			cout << A << " " << B << endl;
		}
	}
}

int main() {
//	makeTest();
//	return 0;
	
	int T; // # of test case
	cin >> T;
	int **A;
	
	for (int i = 1; i <= T; i++) {
		int res = 0;
		int M;	
		int N;	

		cin >> M;
		cin >> N;
		
		//printf("M[%02d] N[%02d]\n", M, N);
		
		A = new int*[M];
		for (int j = 0; j < M; j++)
			A[j] = new int[N];
		
		char ch;
		for (int j = 0; j < M; j++) {
			int idx = 0;
			for (int k = 0; k < (N/4); k++) { 
				cin >> ch;
			//	cout << "ch: " << ch << " ";
				int tmp = (ch >= 'A') ? (int)(ch - 'A' + 10) : (int)(ch - '0');
	
				A[j][idx+3] = tmp % 2; 
				A[j][idx+2] = (tmp >> 1) % 2;
				A[j][idx+1] = (tmp >> 2) % 2;
				A[j][idx] = (tmp >> 3);
				idx += 4;
		}
		}
	
		/*
		for (int m = 0; m < M; m++) {
			for (int p = 0; p < N; p++) {
				cout << A[m][p] << " ";
			}
			cout << endl;
		}
		*/
		int *C;
		C = new int[min(M,N)+1];
		
		for (int jj = 0; jj <= min(M,N); jj++)
			C[jj] = 0;
		
		
		for (int sz = min(M, N); sz >= 1; sz--) {
			for (int ai = 0; ai <= M - sz; ai++) {
				for (int aj = 0; aj <= N - sz; aj++) {

				//	printf("STEP1 ai[%02d] aj[%02d] sz[%02d]\n", ai, aj, sz);

					int prev = -2;	// ÃÊ±âÈ­
					bool isOk = true;
					for (int si = ai; si < ai + sz; si++) {
						int first_prev;
						if (prev == -2) {
							first_prev = A[si][aj];
						} else {
							prev = first_prev;
							first_prev = A[si][aj];						
						}

						for (int sj = aj; sj < aj + sz; sj++) {
							if (A[si][sj] == -1) {
								isOk = false;
								break;
							}
							if (prev == -2) {
								prev = A[si][sj];
							} else {
								if (prev + A[si][sj] != 1) {
									isOk = false;
									break;
								} else {
									prev = A[si][sj];
								}
							}
						}		
					}
					
					if (isOk == true) {
					//	printf("*****STEP2 ai[%02d] aj[%02d] sz[%02d]\n", ai, aj, sz);
						C[sz] = C[sz] + 1;
						for (int si = ai; si < ai + sz; si++) {
							for (int sj = aj; sj < aj + sz; sj++) {
								A[si][sj] = -1;
							}		
						}
					}
				}				
			}			
		}
			
		for (int p = 1; p <= min(M, N); p++) {
			if (C[p] > 0)
				res++;
		}	
		cout << "Case #" << i << ": " << res << endl;	
		
		for (int p = min(M,N); p >= 1; p--) {
			if (C[p] > 0)
				printf("%d %d\n", p, C[p]);
		}
		
		
	/*	for (int j = 0; j < M; j++)
			delete[] A[j];
	*/
		delete[] A;
		delete[] C;
	}
	
	return 0;	
}

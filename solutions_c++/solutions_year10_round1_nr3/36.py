#include <iostream>
#include <fstream>
#include <vector>
#include <string>
#include <queue>
#include <stack>
#include <math.h>
#include <bitset>
#include <ctime>
#include <sys/time.h>

using namespace std;

int main (void) {
//	fstream IN("C0.in", ios::in);	fstream OUT("C0.out", ios::out);
//	fstream IN("C1.in", ios::in);	fstream OUT("C1.out", ios::out);
	fstream IN("C2.in", ios::in);	fstream OUT("C2.out", ios::out);


	int N=1000001;
	vector <long long> A(N), B(N);
	
	A[1]=1;
	B[1]=1;
	for (int i=2; i<N; i++) {
		int inf=0, sup=i; 
		while (inf+1<sup) {
			int med=(inf+sup)/2;
			if (B[med]>=i) sup=med;
			else inf=med;
			}
		A[i]=sup;
		B[i]=sup+i-1;
		}
	
	int NUM_TEST;
	IN>>NUM_TEST;
		
	for (int test=1; test<=NUM_TEST; test++) {
		long long A1,A2,B1,B2;
		IN>>A1>>A2>>B1>>B2;
		cout<<test<<"\n";
		long long RES=0;
		for (int i=A1; i<=A2; i++) if (B1<=B[i] && B2>=A[i]) RES+=(long long)min(B2,B[i])-max(B1, A[i])+1;
		
		RES=(A2-A1+1)*(B2-B1+1)-RES;
		
		OUT<<"Case #"<<test<<": "<<RES<<"\n";
		}
	return 0;	
	}


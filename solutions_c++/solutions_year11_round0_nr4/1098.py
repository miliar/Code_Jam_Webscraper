#include <iomanip.h>
#include <iostream>
#include <fstream>
#include <string>
#include <stdio.h>
#include <math>
using namespace std;

#define MAX_N 1000

int main()
{
	ifstream fin("D-large.in");
//	ofstream fout("D-small-attempt0.out");
	FILE *fp;
	fp = fopen("D-large.out", "w");

	if(!fin){
		cout << "Cannot open the file.\n";
		return 1;
	}

	int T;
	fin >> T; 

	// prepro
	double g[MAX_N+1];			// the expection of #Goro's attempts to sort n elements
	g[0]=0;
	g[1]=1;
	g[2]=2;
	g[3]=3;
	for(int i=4; i<MAX_N+1; i++){
		g[i] = g[(int)(i/2)] + g[i-(int)(i/2)];
//		cout << "g[" << i << "]=" << g[i] << endl;
	}

	for(int i=0;i<T;i++){
		int N;
		fin >> N;
		int k;
		int wnum=0;
		for(int j=0;j<N;j++){
			fin >> k;
			if(k!=j+1)wnum++;
		}
		
//		cout << "wnum:" << wnum <<endl;
//		cout << "Case #" << i+1 << ": " << g[wnum] << endl;
		fprintf(fp,"Case #%d: %.6f\n",i+1,g[wnum]);
	}


	fin.close();
//	fout.close();
	fclose(fp);
}

// memo ---------
//
// a(n,k): events that only k elelmetns are sorted in an array which has n elements (k <= n)
//
// Pr{a(n,k)} =  nCk * Pr{a(n-k,0)} (0 < k < n-1)
//            =  f(n)/n!            (k = 0)
//            =  1/n!               (k = n)
//            =  0                  (k = n-1)
//
// such that f(n) = (n-1)*(f(n-1)+f(n-2)), f(0)=0 and f(1)=1
//
// Pr{a(1,1)}=1, Pr{a(1,0)}=0
//
// g(n) := Ex[Pr{Goro's attempts to sort n elements}] 
//
// g(n) = sum{k=0...n}{ g(n-k) * Pr{a(n,k)} }, g(0)=1
//      = Pr{a(n,0)/(1-Pr{a(n,0)}) * sum{k=1...n}{ g(n-k)*Pr{a(n,k)} }
//

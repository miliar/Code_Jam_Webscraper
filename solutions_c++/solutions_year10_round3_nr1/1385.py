#include <iostream>
#include <stdio.h>
#include <fstream>
#include <conio.h>

using namespace std;

ifstream fi("A-large.in");
ofstream fo("out.txt");

int t;
long* a;
long* b;
int N;


long check (long* a, long*b) {
	long res=0;
	for (int i=1; i<=N-1; i++)
		for (int j=i+1; j<=N; j++) 
			if ( (a[i]<a[j] && b[i]>b[j]) || (a[i]>a[j] && b[i]<b[j])) res++; 

return res;
}

int main (void) {
	fi>>t;

	for (int c=1; c<=t; c++) {
		fi>>N;
		a=new long[N+1];
		b=new long[N+1];

		for (int j=1; j<=N; j++)  {fi>>a[j]>>b[j];}
		
		fo<<"Case #"<<c<<": "<<check(a,b)<<endl;
		free(a);
		free(b);
	}

		fi.close();
		fo.close();

	return 1;
}

   

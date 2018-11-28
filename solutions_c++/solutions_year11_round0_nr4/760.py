#include<vector>
#include<iostream>
#include<fstream>
#include<stdio.h>

using namespace std;

double getAnswer(vector<int> &A)
{
	int n=0;
	for(size_t i=0;i<A.size();i++)
		if(A[i]-1 != i)
			n++;
	return (double)n;
}

int main(int argc, char *argv[])
{
	ifstream ifs(argv[1]);
	int T;
	ifs >> T;
	for(int i=0;i<T;i++){
		int N;
		ifs >> N;
		vector<int> A(N);
		for(int j=0; j<N; j++)
			ifs >> A[j];

		double a = getAnswer(A);
		cout << "Case #" << i+1 << ": ";
		printf("%.6f\n",a);
	}
	return 0;
}
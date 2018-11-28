#include <iostream>
#include <stdio.h>
#include <fstream>
#include <math.h>
using namespace std;

int main()
{
	int T,N;
	int C[1001];
	int i,j;
	int tryNo, minC, sum;


	cin >> T;
	for (i=1;i<=T;i++)
	{
		cin >> N;
		for (j=0;j<N;j++) 
			cin >> C[j];
		tryNo=0;
		minC=1000001;
		sum = 0;
		for (j=0;j<N;j++) 
		{
			tryNo=tryNo^C[j];
			sum = sum + C[j];
			if (C[j] < minC) minC = C[j];
		}
		
		if (tryNo!=0) cout << "Case #" << i <<": NO" << endl;
		else cout << "Case #" << i <<": " << (sum-minC) << endl;
	}
	return 0;
}
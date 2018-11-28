#include<iostream>
#include<fstream>
#include<cmath>
using namespace std;

int main()
{
	ofstream fout("ans");
	int t,N,K,n;
	cin >> t;
	n = 1;
	while(t>0)
	{
		t--;
		cin >> N >> K;
		N = pow((double)2,N);
		K%=N;
		if( N-1==K )
			fout << "Case #" << n++ << ": ON" << endl;
		else
			fout << "Case #" << n++ << ": OFF" << endl;
	}
}
#include<iostream>
#include<fstream>

using namespace std;

int main (int argc, char * const argv[]) {
	ifstream myfile;
	myfile.open(argv[1]);

	int T,N,K;
	myfile >> T;

	int dp[31];
	for(int counter=0; counter < T; counter++)
	{
		
		myfile >> N >> K;
		
		int tot=0;
		
		for(int i=1; i<=N; i++)
		{
			tot += tot+1;
		
		}
		
		
		if(K!=0 && (K==tot || (K-tot)%(tot+1) == 0))
		{
			cout << "Case #" << counter+1 << ": ON" << endl;
		}
		else {
				cout << "Case #" << counter+1 << ": OFF" << endl;
			
		}
		
	}
	return 0;
}
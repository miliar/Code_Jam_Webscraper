#include <fstream>
#include <string>
using namespace std;

string solve(int n, long int k)
{
	int a = 2;
	for(int c=1;c<n;c++)
		a *=2;
	if (k%a==(a-1))
		return "ON";
	else
		return "OFF";
}

int main()
{
	ifstream inputFile;
    inputFile.open( "input.txt", ios_base::in );
	ofstream outputFile;
    outputFile.open("output.txt", ios_base::out);
	int testCase;
	inputFile>>testCase;
	for(int i = 0;i<testCase;i++)
	{
		int N;
		long int K;
		inputFile>>N;
		inputFile>>K;
		outputFile<<"Case #"<<(i+1)<<": "<<solve(N,K)<<endl;
	}
	return 0;
}
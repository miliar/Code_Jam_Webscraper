#include <fstream>
#include <iostream>
using namespace std;

int main()
{
	ifstream inFile("A-large.in");
	//ifstream inFile();
	ofstream outFile("output.txt");
	int caseNum;
	int N, K;
	inFile>>caseNum;
	for (int i = 0; i < caseNum; i++)
	{
		inFile>>N>>K;
		//cout<<N<<"	"<<K<<endl;
		int sum = INT_MAX - K;
		int divNum = 1;
		divNum = divNum<<N;
		//cout<<sum<<"	"<<divNum<<endl;
		if ((sum % divNum) == 0)
			outFile<<"Case #"<<i+1<<": ON"<<endl;
		else
			outFile<<"Case #"<<i+1<<": OFF"<<endl;
	}
	//cin.get();
	return 0;
}

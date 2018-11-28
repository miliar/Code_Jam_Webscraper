#include <iostream>
#include <fstream>
using namespace std;

int buffer[31];
void init()
{
	buffer[1] = 1;
	for (int i = 2; i <= 30; ++ i)
	{
		buffer[i] = 2 * buffer[i - 1] + 1;
	}
}

bool calc(int n, int k)
{
	k %= buffer[n] + 1;
	return (k == buffer[n]);
}


int main()
{
	fstream inputFile("F:/gcj/data1s.in", ios_base::in);
	fstream outputFile("F:/gcj/data1s.out", ios_base::out);
	
	int caseCount;
	inputFile >> caseCount;
	init();
	for (int ci = 0; ci < caseCount; ++ ci)
	{
		int n, k;
		inputFile >> n >> k;
		outputFile << "Case #" << ci + 1 << ": ";
		if (calc(n, k)) outputFile << "ON" << endl;
		else outputFile << "OFF" << endl;
	}

	inputFile.close();
	outputFile.close();
	return 0;
}
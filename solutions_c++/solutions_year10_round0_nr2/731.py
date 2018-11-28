#include <fstream>
#include <iostream>
#include <queue>
#include <algorithm>
using namespace std;

long long EUCLID(long long a, long long b)
{
	if (b == 0)
		return a;
	else
		return EUCLID(b, a%b);
}

int main()
{
	//ifstream inFile("input.txt");
	ifstream inFile("B-small-attempt0.in");
	ofstream outFile("output.txt");
	int caseNum;
	inFile>>caseNum;
	for (int i = 0; i < caseNum; i++)
	{
		vector<long long> dataVec;
		vector<long long> dataDiff;
		int dataNum;
		inFile>>dataNum;
		for (int j = 0; j < dataNum; j++)
		{
			long long dataElement;
			inFile>>dataElement;
			dataVec.push_back(dataElement);
		}
		sort(dataVec.begin(), dataVec.end());
		sort(dataDiff.begin(), dataDiff.end());

		for (int j = 1; j < dataVec.size(); j++)
			dataDiff.push_back(dataVec[j] - dataVec[j-1]);

		/*for (int j = 0; j < dataVec.size(); j++)
			cout<<dataVec[j]<<"	";
		cout<<endl;

		for (int j = 0; j < dataDiff.size(); j++)
			cout<<dataDiff[j]<<"	";
		cout<<endl;*/

		long long maxFactor = dataDiff[0];

		for (int j = 1; j < dataDiff.size(); j++)
		{
			maxFactor = EUCLID(dataDiff[j], maxFactor);
		}

		long long vecMax = *dataVec.rbegin();
		long long multNum = vecMax/maxFactor;
		long long remValue = vecMax%maxFactor;
		long long result = multNum*maxFactor;
		if (remValue)
			result = result + maxFactor - vecMax;
		else
			result = 0;

		outFile<<"Case #"<<i+1<<": "<<result<<endl;
		//cout<<EUCLID(10, 5)<<"	"<<EUCLID(64, 72)<<"	"<<EUCLID(81, 72)<<endl;
	}
	return 0;
}

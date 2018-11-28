#include <iostream>
#include <fstream>
#include <sstream>
#include <map>
#include <math.h>
#include <string>
#include <stdio.h>
#include <vector>
#include <list>
#include <set>
#include <algorithm>

using namespace std;

ofstream outStream;
ifstream inStream;


int getKeyCount()
{
    int keyCount = 0;
    long long P, K, L;

    inStream >> P >> K >> L ;

    vector<long long >  keyFreq;
	
    for(int i = 0; i < L; i++)
    {
	long long currentValue;
	inStream >> currentValue;

	keyFreq.push_back(currentValue);

	cout<< "Entering value " << currentValue << endl;
    }

    sort(keyFreq.begin(), keyFreq.end());

    vector<long long>::reverse_iterator begin = keyFreq.rbegin();
    int currentKey = 1;
    int keyPress = 1;
    for(;begin != keyFreq.rend(); begin++)
    {
	cout << "key count for value " << (*begin) << endl;

	keyCount += keyPress * (*begin);

	if(currentKey%K == 0)
	{
		keyPress++;
	}
	currentKey++;
    }
    return keyCount;
}

void runTestCase()
{
    int i = 0;

    long long testCaseCount = 0;

    inStream >> testCaseCount;

    cout << "Test case count = " << testCaseCount << endl;
    i = 1;
    for(;i <= testCaseCount; i++)
    {
        int keyCount = 0;
    	
	keyCount = getKeyCount();
        outStream << "Case #" << i  <<": " << keyCount << endl;
    }

}

int main(int argc, const char** argv)
{
    if(argc < 3)
    {
        printf("Wrong number of arguments. Usage: universe input_filename output_filename \n");
    }

    inStream.open(argv[1]);
    outStream.open(argv[2]);

    runTestCase();

    outStream.close();
    inStream.close();

    return 0;
}

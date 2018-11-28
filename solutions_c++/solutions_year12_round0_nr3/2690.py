#include<iostream>
#include<string>
#include<fstream>
#include<math.h>
#include<map>

using namespace std;

void RotateNumber(long long number, map<long long,long long> &myMap, long long &count)
{
	long long start = number;
	
	long long numdigits = (int) log10((double)number); // would return numdigits - 1
	long long multiplier = (int) pow(10.0, (double)numdigits);
	
	while(true)
	{
		long long q = number / 10;
		long long r = number % 10;

		number = number / 10;
		number = number + multiplier * r;
		
		if(myMap[number]>0 && number > start)
		{
			//cout << start << " && " << number << endl;
			count++;
		}

		if(number == start)
			break;
	}

}

int main(int argc, char *argv[])
{	
	ifstream file;
	ofstream outputFile;
	
	long long intTestCases=0, intA=0, intB=0, intCurrentItemPrice=0;
	
	long long count=0;
	map<long long,long long> myMap;
	map<long long,long long>::iterator it;
	
	outputFile.open(argv[2]);
	file.open(argv[1]);
	
	//Read integers..
	if(!file.eof())
		file >> intTestCases;
	
	for(int i=0; i<intTestCases; ++i)
	{
		file >> intA;
		file >> intB;
		
		for (long long j=intA; j<=intB; ++j) {
			myMap[j]++;
		}
		
		for (long long k=intA; k<=intB; ++k) {
			RotateNumber(k,myMap,count);
		}
		
		outputFile << "Case #" << i+1 << ": " << count << endl;
		count=0;
		myMap.clear();
	}
	
	outputFile.close();
	file.close();
	
	return 0;
}

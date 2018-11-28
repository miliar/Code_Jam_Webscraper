#include <iostream>
#include <vector>
#include <fstream>
#include <cmath>
using namespace std;
int numOfDigits(int x)
{
	int i = 1;
	while(pow((double)10, i) <= x)
		i++;
	return i;
}
bool isInInterval(int x, int y, int z)
{
	if(x >= y && x <= z)
		return true;
	else
		return false;
}
int searchForRecycled(int x, int y, int digits)
{
	int result = 0;
	for(int i = x; i < y; i++)
	{
		if( digits == 2)
		{
			int d = floor((double)i/(double)10);
			int u = i - (10 * d);
			int flipped = (10 * u) + d;
			if(isInInterval(flipped, x, y) && flipped > i)
				result++;
		}
		else if (digits == 3)
		{
			int c = floor((double)i/(double)100);
			int d = floor((double)(i - (100*c))/(double)10);
			int u = i - (100*c + 10*d);
			int flippedone = 100 * u + 10 *c + d;
			int flippedtwo = 100 * d + 10* u + c;
			if(isInInterval(flippedone, x, y) && flippedone > i)
				result++;
			if(isInInterval(flippedtwo, x, y) && flippedtwo > i)
				result++;
		}
		else
		{}
	}
	return result;
}
int main()
{
	ifstream infile("input.in");
	ofstream outfile("output.txt");
	int T;
	infile>>T;
	vector<int> numbersA;
	vector<int> numbersB;
	vector<int> recycledPairs;
	for(int i = 0; i < T; i++)
	{
		int A,B = 0;
		infile>>A>>B;
		numbersA.push_back(A);
		numbersB.push_back(B);
	}
	for(int i = 0; i < T; i++)
	{
		int A = numbersA[i];
		int B = numbersB[i];
		int nDigits = numOfDigits(A);
		recycledPairs.push_back(searchForRecycled(A, B, nDigits));
	}
	for(int i = 0; i < T; i++)
	{
		cout<<"Case #"<<i+1<<": "<<recycledPairs[i]<<endl;
		outfile<<"Case #"<<i+1<<": "<<recycledPairs[i]<<endl;
	}
}

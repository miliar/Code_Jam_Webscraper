#include <iostream>
#include <fstream>

using namespace std;

bool isRecycled(int n, int k)
{
	int temp = n;
	int numDigits = 0;
	while(temp != 0)
	{
		temp /= 10;
		numDigits++;
	}

	temp = n;
	temp += (temp % 10) * pow(10.0,numDigits);
	temp /= 10;
	while(temp != n)
	{
		if(temp == k)
			return true;
		temp += (temp % 10) * pow(10.0,numDigits);
		temp /= 10;
	}
	return false;

}

int main()
{
	ifstream fin("input.txt");
	ofstream fout("output.txt");

	int n;
	fin >> n;
	int numRecycled;
	for(int i = 0; i< n; i++)
	{
		numRecycled = 0;
		int a, b;
		fin >> a >> b;
		int j = a, k = b;
		for(k = b; k > a; k--)
		{
			for(j = a; j < k; j++)
			{
				if (isRecycled(j, k))
					numRecycled++;
			}
		}

		fout << "Case #" << i+1 << ": " << numRecycled << endl;
	}


	return 0;
}
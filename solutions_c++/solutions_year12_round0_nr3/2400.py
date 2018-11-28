#include <iostream>
#include <string>
#include <fstream>
using namespace std;

//convert integer to string
string toString(unsigned int n)
{
	char r[11];
	itoa(n,r,10);
	return string(r);
}

//convert string to integer
int toInteger(string s)
{
	const char* r = s.c_str();
	return atoi(r);
}

string composed(int n)
{
	string s=toString(n);
	return s+s;
}

int numberOfRecycledPairs(int A, int B)
{
	int x=B-A+1;
	bool* processed = new bool[x];
	for(int i=0;i <x;i++)
		processed[i]=false;

	int number=0;
	int numberOfDigits=toString(A).size();
	for(int n=A; n<B; n++)
	{
		if (!processed[n-A])
		{
			processed[n-A]=true;
			string s=composed(n);
			int current=0;
			for (int j=1; j<numberOfDigits; j++)
			{
				string sx=s.substr(j, numberOfDigits);
				int k = toInteger(sx);
				if (k>=A && k<=B && n!=k && !processed[k-A])
				{
					current++;
					number+=current;
					processed[k-A]=true;
				}
			}
		}
	}
	return number;
}

int main()
{
	ifstream fin("Recycled Numbers/C-large.in");
	ofstream fout("Recycled Numbers/2x.out");

	int T=0;
	string s;
	getline(fin, s);
	T=toInteger(s);

	for(int t=1; t<=T; t++)
	{
		int A=0, B=0;
		fin>>A>>B;
		fout<<"Case #"<<t<<": "<< numberOfRecycledPairs(A, B) <<"\n";
	}

	return 0;
}
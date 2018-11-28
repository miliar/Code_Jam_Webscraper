#include <iostream>
#include <fstream>
#include <string>

using namespace std;

int GetNumberOf(int results[],int p,int surp, int googlers)
{
	int cnt=0;
	if (p==0) return googlers;
	for (int i=0; i<googlers; ++i)
	{
	if (results[i]!=0)
		{
		if (results[i]/3>=p || (results[i]/3+1>=p && results[i]%3!=0))
			++cnt;
		else if (((results[i]/3+1==p && results[i]%3==0) || (results[i]/3+2==p && results[i]%3==2)) && 0<surp)
				{
					++cnt;
					--surp;
				}
		}
	}
	return cnt;
}

int main()
{
	ifstream inFile;
	ofstream outFile;
	inFile.open("B-large.in");
	outFile.open("output.txt");	
	int size;
	inFile >> size;
	for (int i=0; i<size; ++i)
	{
		outFile << "Case #" << i+1 << ": ";		
		int googlers;
		int surp;
		int p;
		inFile >> googlers >> surp >> p;
		
		int results[googlers];
		for (int j=0; j<googlers; ++j)
		{
			inFile >> results[j];
		}	
		outFile << GetNumberOf(results,p,surp,googlers) << endl;
	}

	inFile.close();
	outFile.close();
}


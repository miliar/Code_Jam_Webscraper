//============================================================================
// Name        : SavingTheUniverse.cpp
// Author      : 
// Version     :
// Copyright   : Your copyright notice
// Description : Hello World in C++, Ansi-style
//============================================================================

#include <iostream>
#include <fstream>
#include <string>
#include <list>
#include <set>

using namespace std;


int main() {

	ifstream fin;
	ofstream fout;
	fout.open("output.txt");
	fin.open("sample.txt");
	int n, maxLetterOnKey, numKey, numLetter;
	

	fin>>n;
	for(int i=0;i<n;i++)
	{
		int total = 0;
		fin>>maxLetterOnKey>>numKey>>numLetter;
		multiset<int> letter;
		
		int temp;
		for(int j =0;j<numLetter;j++)
		{
			fin>>temp;
			letter.insert(temp);
		}
		
		temp = 1;
		int num = numKey;
		cout<<letter.size()<<endl;
		for(multiset<int>::reverse_iterator it = letter.rbegin();it!=letter.rend();it++)
		{
			total = total + temp * (*it);

			num--;
			if (num==0)
			{
				num = numKey;
				temp++;
			}
		}
		cout<<"Case #"<<i+1<<": "<<total<<endl;
		fout<<"Case #"<<i+1<<": "<<total<<endl;
	}
	fout.close();
	fin.close();
	return 0;
}

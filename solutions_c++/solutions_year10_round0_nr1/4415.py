#include <iostream>
#include <fstream>
#include <string>
#include <vector>
using namespace std;



int main ()
{
	string line;
	ifstream testfile;
	ofstream result;
	result.open("e:\\result.txt");
	testfile.open("e:\\example.txt");

	int CaseNo;
	testfile >>CaseNo;
	for(int i = 0; i < CaseNo;i++)
	{
		int nSap;
		testfile >>nSap;
		int nTog;
		testfile >>nTog;
		string snapp;
		for(int n = 0; n < nSap; n++)
			snapp += 'f';
		for(int k = 0; k < nTog; k++)
		{
			int m = 1;
			while(snapp[m-1] == 'n' && m < nSap)
				m++;
			m--;
			for(m; m >= 0; m--)
			{
				if(snapp[m] == 'f')
					snapp[m] = 'n';
				else
					snapp[m] = 'f';
			}
		}
		//Output file
		result<<"Case #"<<i+1<<": ";
		//cout<<"Case #"<<i+1<<": ";
		bool bOpen = true;
		for(int k = 0; k < snapp.length(); k++)
			if(snapp[k] == 'f')
			{
				bOpen = false;
				break;
			}
		if (bOpen)
		{
			result<<"ON"<<endl;
			//cout<<"ON"<<endl;
		}
		else
		{
			result<<"OFF"<<endl;
			//cout<<"OFF"<<endl;
		}
	}
}
#include "stdafx.h"
#include <string>
#include <fstream>
#include <sstream>
#include <algorithm>

using namespace std;
using std::string;
stringstream ss;

int caseNum = 0;

int findDecreasing(int n[], int len);
int findNextBig(int nn[], int targetNum, int len);

int _tmain(int argc, _TCHAR* argv[])
{
	const char *inputFileName;
	
	// Input
	ifstream inp( "D:\\CodeJam09\\B-large.in" );
	// Output
	//FILE * pFile = fopen ("D:\\CodeJam09\\outputLargeFile.txt","w");
	FILE * pFile = fopen ("D:\\CodeJam09\\outputLargeFile.txt","w");

	string temp;
	getline( inp, temp );
	int caseNum = atoi(temp.c_str());		
	
	for(int t=0 ; t<caseNum ; t++)
	{	
		fprintf(pFile, "Case #%d: ", t+1);
		getline( inp, temp );
		
		const char* a;
		int* n;

		a = temp.c_str();

		n = (int*) malloc(strlen(a)*sizeof(int)); 
		for(int i=0 ; i<strlen(a) ; i++){
			string str = temp.substr(i, 1);

			istringstream int_iss(str);
			int_iss >> n[i];
		}

		int pos = findDecreasing(n, strlen(a));

		if(pos > 0){
			string substr = temp.substr(pos, strlen(a)-pos);
			reverse (substr.begin(), substr.end());
			int sublen = substr.length();


			int* nn = (int*) malloc(sublen*sizeof(int)); 
			for(int i=0 ; i<sublen ; i++){
				string str = substr.substr(i, 1);

				istringstream int_iss(str);
				int_iss >> nn[i];
			}
			
			temp = temp.substr(0, pos);
			string last = temp.substr(pos-1, 1);
			int targetNum;
			istringstream int_iss(last);
			int_iss >> targetNum;
			int bigind = findNextBig(nn, targetNum, strlen(a));
			
			string bigL = substr.substr(bigind, 1);

			temp.replace(pos-1, 1, bigL);
			substr.replace(bigind, 1, last);

			//temp = temp.substr(0, pos-1);
			//substr = substr.substr(1, sublen-1);//, substr.length()-1);

			//temp.append(first);
			//substr.insert(0, last);

			temp.append(substr);
			
			a = temp.c_str();

			fprintf(pFile, "%s ", a);
		}
		else if(pos == 0)
		{			
			string last = temp.substr(temp.length()-1, 1);
			int posi;
			for(int t=strlen(a)-1 ; t>=0; t--)
			{
				if(n[t] != 0){
					posi = t;
					t = -100;
				}
			}
			string em = temp.substr(posi, 1);
			temp.replace(posi, 1, "0");
			temp.replace(strlen(a)-1, 1, em);

			reverse (temp.begin(), temp.end());
				

			
			temp.insert(1, "0");
    
			a = temp.c_str();
			fprintf(pFile, "%s ", a);
		}
		
		fprintf(pFile, "\n");
	}	

	fclose (pFile);
	
	return 0;
}

int findNextBig(int nn[], int targetNum, int len)
{
	int index = 0;

	for(int i=0 ; i<len ; i++)
		if(nn[i] > targetNum)
			return i;
}


int findDecreasing(int n[], int len)
{
	int index = 0;

	int prev;
	for(int i=len ; i>=0 ; i--)
	{
		if(i==len)
			prev = n[i];
		else{
			if(prev>n[i])
				return i+1;
			else
				prev = n[i];
		}
	}

	return 0;

}
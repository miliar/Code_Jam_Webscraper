#include <algorithm>
#include <fstream>
#include <string>
#include <sstream>
#include <iterator>
#include <iostream>
#include <stdlib.h>  // atoi
using namespace std;
int rotateStr(string str,const string &strB);
int main()
{
	ifstream infile("F:\\C-small-attempt0.in");
	ofstream outfile("outputRN.txt");
	string temp;
	string line;
	string rotaString;
	string strA;
	string strB;
	int result = 0;
	int tempS;
	int times = 1;
	char array[256];
	getline(infile,temp);
	while(getline(infile,line))
	{
		istringstream stream(line);
		stream >> strA;
		stream >> strB;
		string strVar(strA);
		while (strVar !=strB)
		{
			if (strVar.length()!=1)
			{
				result += rotateStr(strVar,strB);
			}
			tempS = atoi(strVar.c_str());
			itoa(++tempS,array,10);
			strVar = array;
			//cout <<strVar <<endl;	
			
		}
		outfile << "Case #"<< times << ": "<< result <<'\n';
		
		result = 0;
		times++;
	}
	//cout << strA << " " <<strB;
	
	infile.close();
	outfile.close();
}

int rotateStr(string str,const string &strB)
{
	int result =0;
	string::iterator iter = str.begin()+1;
	string copyStr(str);
	string::iterator iterCopy = copyStr.begin();
	for (;iter!=str.end();iter++)
	{
		rotate_copy(str.begin(),iter,str.end(),iterCopy);
		
		if (*(copyStr.begin()) == '0') 
			continue;
		if (atoi(copyStr.c_str())<= atoi(strB.c_str()) && atoi(str.c_str()) < atoi(copyStr.c_str()))
			result++;
	}
	return result;
}
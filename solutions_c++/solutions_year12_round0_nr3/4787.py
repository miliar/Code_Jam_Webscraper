#include <iostream>
#include <fstream>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

using namespace std;


string shuffleStr(char * str, int k)
{
	string temp = str;
	//cout << "temp: " << temp << " k: " << k << endl;

	int len = temp.size();
	int val = len - k;
	//cout << "len: " << len << " val: " << val << endl;
	
	
	string tailToBe  = temp.substr(0, val);
	string headToBe = temp.substr(val, len);

	//cout << "temp.size(): " << temp.size() << endl;
	

	
	//cout << "tailToBe: " << tailToBe << " headToBe: " << headToBe << endl;
	temp.replace(0, k, headToBe);
	temp.replace(k, len - k, tailToBe);

	
	//cout << "temp111: " << temp << endl;
	return temp;
}




int main(int argc, char *argv[])
{
	
	if( remove( "example.txt" ) != 0 )
		perror( "Error deleting file" );
	 else
		puts( "File successfully deleted" );

	  ifstream in("C-small-attempt0.in");
	  //ifstream in("sample01.in");  

	 if(!in) {
		cout << "Cannot open input file.\n";
		return 1;
	 }
	

	string valT;
  	getline(in, valT, '\n');
  	int valIntT = atoi (valT.c_str());

	
	FILE * pFile;
	pFile = fopen ("example.txt", "a");

	ofstream myfile;
	myfile.open ("example.txt", ios::app);


	for(int i = 0; i < valIntT; i++)
	{
		string valA;
		getline(in, valA, ' ');  	

		string valB;
		getline(in, valB, '\n');  	

		int valIntA = atoi (valA.c_str());
		int valIntB = atoi (valB.c_str());

		//cout << "valStrB: " << valIntB << "valStrA: " << valIntA  << endl;
		int totalMatch = 0;

		while(valIntA <= valIntB)
		{
			for(int j = valIntA + 1; j <= valIntB; j++)
			{
			
				char compareStr[7];
				//buffer >> valIntB;
				//cout << "sdasd" << endl;			
				sprintf(compareStr, "%d", j);
				//cout << "aaaa" << endl;
				//cout << "strlen compareStr: " << strlen(compareStr) << endl;
				//cout << "wewew" << endl;
				int match = 0;
				for(int k = 0; k < strlen(compareStr); k++)
				{
					//cout << "strlen(valStrA) " << strlen(valStrA) - 1 << endl;
					//cout << "atoi(  (shuffleStr(valStrA, k)).c_str())" << atoi(  (shuffleStr(valStrA, k)).c_str()) << endl;
					if(valIntA == atoi(  (shuffleStr(compareStr, k)).c_str()) )	
					{
						match++;
						//cout << "valIntA " << valIntA << " atoi(  (shuffleStr(compareStr, k)).c_str()) " <<  compareStr << endl;
					}
	
				}	
				totalMatch += match;	
			}


			
			valIntA++;
		}
		//cout << "Case #" << (i + 1) << ": " << totalMatch << endl << endl;
		myfile << "Case #" << (i + 1) << ": " << totalMatch << endl;
	}
	
	
	

	myfile.close();
	fclose (pFile);


  in.close();

  return 0;
}

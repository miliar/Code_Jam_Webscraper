// code-jam.cpp : Defines the entry point for the console application.
#include "stdafx.h"
#include <map>
#include <iostream>
#include <string>
#include <fstream>
#include <vector>

using namespace std;
char convertArray[] = {'y'  ,'h' ,'e' ,'s' ,'o' ,'c' ,'v' ,'x' ,'d' ,'u' ,'i' ,'g'
                            ,'l' ,'b' ,'k' ,'r' ,'z' ,'t' ,'n' ,'w' ,'j' ,'p' ,'f'
                            ,'m' ,'a' ,'q' };
void ConvertWrite(fstream&, string);
static int counter = 0;
int _tmain(int argc, _TCHAR* argv[])
{
    fstream inpFile, outFile;
    inpFile.open ("input.txt", fstream::in);
    outFile.open("output.txt", fstream::out);
    string str;
    vector<string> vecStr;
    int caseCount  = 0;
    inpFile >> caseCount;
    while(!inpFile.eof()){
        getline(inpFile, str);
        if(str.length() != 0)
            vecStr.push_back(str);            
    }
    for(unsigned int i = 0; i < vecStr.size(); ++i)
        ConvertWrite(outFile, vecStr.at(i));

    inpFile.close();
    outFile.close();
	return 0;
}

void ConvertWrite(fstream& oFile, string str)
{
    ++counter;
    unsigned int len = str.length();
    string oStr(str);
    for(unsigned int i = 0; i < len; ++i){
        if(str[i] == ' ')
            oStr[i] = str[i];
        else
            oStr[i] = convertArray[str[i] - 97];
    }
    oFile << "Case #" << counter << ": "
          << oStr << endl;
}
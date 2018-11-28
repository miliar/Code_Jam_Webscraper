/*
 * parseFile.cpp
 *
 *  Created on: Sep 14, 2009
 *      Author: xhd
 */
#include <iostream>
#include <fstream>
#include <sstream>
#include "parseFile.h"

using namespace std;

parseFile::parseFile(string inputfilename):iFileName(inputfilename) {
	inFile.open(iFileName.c_str(),ifstream::in);
	if (!inFile) {
	    cerr << "Unable to open file: "<<iFileName<<endl;
	    exit(1);
	}
}

parseFile::~parseFile() {
	inFile.close();
}

bool parseFile::nextLineSStream(){
    while(inFile.good()){
            char charLine[LINE_LENTH];
            inFile.getline(charLine, LINE_LENTH);
            line = charLine;
            if(string::npos != line.find('#')) //find '#' in the line
            	continue; //skip the header line

            //delete empty lines?
            rmStrSpace(line);
            if(line.empty())continue;

            os.clear();
            os.str("");
            os<<line;

            if(!inFile.good())
            	return false;

            return true;
    }

    return false;
}

void parseFile::rmStrSpace(string line){
	for(int i=0; i<line.length(); i++){
		if(line[i]=='	'||line[i]==' '||line[i]=='\n')
			line.erase(i,1);
		else{ //encounter first non-space character, exit.
			break;
		}
	}
}


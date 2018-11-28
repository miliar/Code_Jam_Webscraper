
#include <stdio.h>
#include <iostream>
#include <istream>
#include <fstream>
#include <sstream>
#include <map>

using namespace std;


template <class InputType>
bool ReadAtomicLine (InputType& returnValue, istream& inputStream) {

	
	/******************************/
	/* Read one entire line       */
	/******************************/


	string inputLine = "";
	
	while (inputLine.empty()) {
		if ( ! getline(inputStream, inputLine) ) {			
			return false;
		}
	}
	
	
	/******************************/
	/* Atomize line into tokens   */
	/******************************/


	istringstream inputLineStream(inputLine);	
	inputLineStream >> returnValue;
	
	return true;
}

/* Learn Googlerese using the provided... */
bool learnGooglerese(map<char, char>& globalMappingGooglereseEnglish, map<char, char>& globalMappingEnglishGooglerese,const string& strGooglerese, const string& strEnglish) {
	
	/* For debugging - assure that learning input is correct */
	if(strGooglerese.length() != strEnglish.length()) {
		cout << "ATTENTION: length mismatch between " << strGooglerese << " and " << strEnglish << endl;
		return false;
	}
	
	/* Now simply update mapping */
	for (unsigned int curChar = 0;
		 curChar < strGooglerese.length();
		 curChar++) {
		
		/* Assuming that mapping is always the same, we can override previous mappings.
		 * No need for special case for spaces as they will be mapped onto itself... */
		globalMappingGooglereseEnglish[strGooglerese[curChar]] = strEnglish[curChar];	
		globalMappingEnglishGooglerese[strEnglish[curChar]] = strGooglerese[curChar];
	}
		
	return true;
}

/* If we could not learn all from examples, fill gaps here */
bool fillGooglereseGaps(map<char, char>& globalMappingGooglereseEnglish, 
                        map<char, char>& globalMappingEnglishGooglerese) {
							
	const string strEnglishAlphabet = "abcdefghijklmnopqrstuvwxyz";
	
	string EnglishCharMappingMissing = "";
	string GooglereseMappingMissing = "";
	
	
	/************************************************************/
	/* Detect unmapped chars in both English and Googlerese     */
	/************************************************************/
	
	
	for(size_t pos = 0; 
	    pos < strEnglishAlphabet.length(); 
		pos++) {
			
		if(globalMappingEnglishGooglerese.find(strEnglishAlphabet.at(pos)) == globalMappingEnglishGooglerese.end()) {
			
			EnglishCharMappingMissing.push_back(strEnglishAlphabet.at(pos));
		}
		
		if(globalMappingGooglereseEnglish.find(strEnglishAlphabet.at(pos)) == globalMappingGooglereseEnglish.end()) {
			
			GooglereseMappingMissing.push_back(strEnglishAlphabet.at(pos));
		}
				
	}
	
	
	if (GooglereseMappingMissing.length() != EnglishCharMappingMissing.length()) {
		cout << "ERROR: number of unmapped chars is different in English and Googlerese!\n" << endl;
		return false;
	}
	
	
	/************************************************************/
	/* Now assign to Googlerese any English character           */
	/* (preference to itself if possible)                       */
	/************************************************************/


	for(size_t googleresePos = 0; 
	    googleresePos < GooglereseMappingMissing.length();
		googleresePos++) {
		
			
		/* Check if reflexiv mapping is possible */
		size_t englishPos = EnglishCharMappingMissing.find(GooglereseMappingMissing[googleresePos]);
			
		/* If not just take last available char */
		if (englishPos == string::npos) {
			englishPos = EnglishCharMappingMissing.length() - 1;
		}
		
		/* Update mapping (english -> googlerese not needed anymore) */
		globalMappingGooglereseEnglish[GooglereseMappingMissing[googleresePos]] = EnglishCharMappingMissing[englishPos];
		
		/* Remove used english char from string to avoid it being re-used */
		if(englishPos < EnglishCharMappingMissing.length() - 1) {
			EnglishCharMappingMissing[englishPos] = EnglishCharMappingMissing[EnglishCharMappingMissing.length() - 1];			
			EnglishCharMappingMissing.resize(EnglishCharMappingMissing.length() - 1);
		}
	}
	
	
	return true;
}

/* Translate the text using the previously created googlerese mapping */
string& translateText(const map<char, char>& globalGooglereseMapping, string& strText) {
	
	for (unsigned int curChar = 0;
		 curChar < strText.length();
		 curChar++) {
		
		 strText[curChar] = globalGooglereseMapping.at( (strText[curChar]) );
	}
	
	return strText;
}


int main(int argc, char **argv)
{
	/* I am too lazy for dynamic memory allocation here... */
	char DummyFileNameBuffer[255]; 
	/* Filename provided in input */
	char *pInputFileName = NULL;
	
	
	/******************************/
	/* Check input parameters     */
	/******************************/
	
	
	if (argc <= 1) { 
		
		/* No input parameters - read filename from std-in */
	
		cout << "No filename provided in input - please specify: ";
		cin >> DummyFileNameBuffer;
				
		pInputFileName = (char*) DummyFileNameBuffer;
		
	} else {
		
		/* Filename provided with input parameters */
		
		pInputFileName = (char*) argv[1];
	}
	

	/******************************/
	/* Open file                  */
	/******************************/
	

	ifstream InputFileBuffer;
	InputFileBuffer.open(pInputFileName);
	
	if ( ! InputFileBuffer.is_open()) {
		cout << "Unable to open file " << pInputFileName << " ... exit\n";
		return 1;
	}
	

	/*********************************/
	/* Simplified Learning Component */
	/*********************************/


	map<char, char>   globalMappingGooglereseEnglish;
	map<char, char>   globalMappingEnglishGooglerese;

	/* Now learn! */
	learnGooglerese(globalMappingGooglereseEnglish, globalMappingEnglishGooglerese, "yeq", "aoz");
	learnGooglerese(globalMappingGooglereseEnglish, globalMappingEnglishGooglerese, "ejp mysljylc kd kxveddknmc re jsicpdrysi", "our language is impossible to understand");
	learnGooglerese(globalMappingGooglereseEnglish, globalMappingEnglishGooglerese, "rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd", "there are twenty six factorial possibilities");
	learnGooglerese(globalMappingGooglereseEnglish, globalMappingEnglishGooglerese, "de kr kd eoya kw aej tysr re ujdr lkgc jv", "so it is okay if you want to just give up");

	fillGooglereseGaps(globalMappingGooglereseEnglish, globalMappingEnglishGooglerese);

	/******************************/
	/* Now Process Test Cases     */
	/******************************/


	unsigned int curTestCase;
	unsigned int totalNbTestCases;
	
	string curText = "";

	ReadAtomicLine<unsigned int>(totalNbTestCases, InputFileBuffer);
	
	for(curTestCase = 0; curTestCase < totalNbTestCases; curTestCase++) {
		
		curText = "";
		getline(InputFileBuffer, curText);
				
		cout << "Case #" << (curTestCase+1) << ": " << translateText(globalMappingGooglereseEnglish, curText) << endl; 
	}
	
		
	return 0;
}

#include <iostream>
#include <fstream>
#include <string>
#include <cctype>

using std::cout;
using std::endl;
using std::ios;
using std::ifstream;
using std::string;
using std::getline;

static const char EnglishToGooglereseMap[] = {
	/*	'a','b','c','d','e','f','g',	*/
		'y','n','f','i','c','w','l',
	/*	'h','i','j','k','l','m','n',	*/
		'b','k','u','o','m','x','s',
	/*	'o','p','q','r','s','t'			*/
		'e','v','z','p','d','r',
	/*	'u','v','w','x','y','z'			*/
		'j','g','t','h','a','q',
	};

static const char GooglereseToEnglishMap[] = {
	/*	'a','b','c','d','e','f','g',	*/
		'y','h','e','s','o','c','v',
	/*	'h','i','j','k','l','m','n',	*/
		'x','d','u','i','g','l','b',
	/*	'o','p','q','r','s','t'			*/
		'k','r','z','t','n','w',
	/*	'u','v','w','x','y','z'			*/
		'j','p','f','m','a','q',
	};

int PrintUsage(void);
string& TranslateToEnglish(string &googlerese, string &original);

int main(int argc, char* argv[]) {
	
	if(argc < 2)
		return PrintUsage();

	string filename = argv[1];
	string line, original;
	int numOfTestCases(0), testCase(1);

	ifstream ifs(filename.c_str(), ios::in);
	getline(ifs, line);
	numOfTestCases = atoi(line.c_str());
	
	while(testCase <= numOfTestCases) {
		getline(ifs, line);
		cout << "Case #" << testCase << ": " << TranslateToEnglish(line, original) << endl;
		++testCase;
	}

	ifs.close();
	return 0;
}

int PrintUsage(void) {
	cout << "Usage\n\tSpeakingInTongues.exe [filename]" << endl;
	return 0;
}

string& TranslateToGooglerese(string &english, string &googlerese) {
	string::iterator str_iter = english.begin();
	googlerese.clear();
	while(english.end() != str_iter) {
		if(' ' == *str_iter)
			googlerese.append(1, ' ');
		else
			googlerese.append(1, EnglishToGooglereseMap[tolower(*str_iter) - 'a']);
		++str_iter;
	}
	return googlerese;
}

string& TranslateToEnglish(string &googlerese, string &english) {
	string::iterator str_iter = googlerese.begin();
	english.clear();
	while(googlerese.end() != str_iter) {
		if(' ' == *str_iter)
			english.append(1, ' ');
		else
			english.append(1, GooglereseToEnglishMap[tolower(*str_iter) - 'a']);
		++str_iter;
	}
	return english;
}

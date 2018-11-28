#include <iostream>
#include <map>
#include <vector>
#include <string>
#include <sstream>

using namespace std;

map<char, char> translatorDictionary;
vector<string> phrases;

/* Let's make it more interesting...

map['a'] = 'y';
map['b'] = 'n';
map['c'] = 'f';
map['d'] = 'i';
map['e'] = 'c';

map['f'] = 'w';
map['g'] = 'l';
map['h'] = '';
map['i'] = 'k';
map['j'] = '';

map['k'] = '';
map['l'] = 'm';
map['m'] = 'x';
map['n'] = 's';
map['o'] = 'e';

map['p'] = 'v';
map['q'] = '';
map['r'] = 'p';
map['s'] = 'd';
map['t'] = 'r';

map['u'] = 'j';
map['v'] = '';
map['w'] = '';
map['x'] = '';
map['y'] = '';
map['z'] = '';
*/

char translateLetter (char thisLetter) {
	if (translatorDictionary[thisLetter]){
		return translatorDictionary[thisLetter];
	} else {
		cout << endl << "Error with  letter <" << thisLetter << ">." << endl;
		return 'X';
	}
}

int main () {

	//CREATING THE DICTIONARY

	string englishPhrases[] = {"our language is impossible to understand", "there are twenty six factorial possibilities", "so it is okay if you want to just give up"};
	string translatedPhrases[] = {"ejp mysljylc kd kxveddknmc re jsicpdrysi", "rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd", "de kr kd eoya kw aej tysr re ujdr lkgc jv"};

	for (int i = 0; i<3; ++i) {

		string singleEnglishPhrase = englishPhrases[i];
		string singleTranslatedPhrase = translatedPhrases[i];

		for (int j= 0; j<singleEnglishPhrase.size(); ++j) {
			translatorDictionary[singleTranslatedPhrase[j]] = singleEnglishPhrase[j];
		}

	}

	//FIXING

	translatorDictionary['q'] = 'z';
	translatorDictionary['z'] = 'q';

	//END CREATING THE DICTIONARY


	string inputPhrase;
	string phrasesSizeLine;
	

	getline (cin,phrasesSizeLine);
	int phrasesSize;
	stringstream(phrasesSizeLine) >> phrasesSize;

	for (int i = 0; i<phrasesSize; ++i){
		getline (cin,inputPhrase);
		phrases.push_back(inputPhrase);
		//cout << "Got a frase" << endl;
	}

	//TRANSLATE PHRASES

	for (int i = 0; i<phrasesSize; ++i) {
		string phraseToTranslate = phrases[i];
		cout << "Case #" << (i+1) << ": ";
		for (int j = 0; j<phraseToTranslate.size(); ++j){
			cout << translateLetter(phraseToTranslate[j]);
		}
		cout << endl;
	}

	/* Silly tester says that this shit it working
	for (int i= 0; i<phrasesSize; ++i){
		cout << phrases[i] << endl;
	}
	*/
}
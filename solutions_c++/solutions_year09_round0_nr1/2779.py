#include <iostream>
#include <fstream>
#include <vector>
#include <string>

using namespace std;

#define INPUT_FILE "A-large.in"
#define OUTPUT_FILE "alien.out"

int main () {
    
	ifstream in(INPUT_FILE);
	ofstream out(OUTPUT_FILE);
	
	int length = 0, words = 0, cases = 0;
    in>>length>>words>>cases;
	
	vector<string> dictionary;
	string word;
	
	for(int i=0; i<words; i++){
	   	in>>word;
		dictionary.push_back(word);
	}
	
	vector<string> patterns;
	string pattern;
	
	for(int i=0; i<cases; i++){
		in>>pattern;
		patterns.push_back(pattern);
	}
	
	for(int i=0; i<cases; i++){
		
		vector<string> places;
		int count = 0;
		
		bool inP = false;
		string currentPattern = patterns[i];
		string placeString = "";
		
		for(int j=0; j<currentPattern.length(); j++){
		    if(currentPattern[j] == '(')
				inP = true;
			else if(currentPattern[j] == ')')
				inP = false;
			else
				placeString.push_back(currentPattern[j]);
			
			if(!inP){
				places.push_back(placeString);
				placeString = "";
			}
		}
		
		string currentWord;
		string currentPlacePattern;
		size_t match;
		
		for(int k=0; k<words; k++){
			bool doesMatch = true;
			currentWord = dictionary[k];
			
			for(int j=0; j<length; j++){
				currentPlacePattern = places[j];
				match = currentPlacePattern.find(currentWord[j]);
				if(match == string::npos){
					doesMatch = false;
					break;
				}
			}
			
			if(doesMatch)
				count++;
		}
		
		out<<"Case #"<<i+1<<": "<<count<<endl;
		
	}
	
	return 0;
}


#include <iostream>
#include <fstream>
#include <set>
#include <string>

//#define DEBUG
#ifdef  DEBUG
#  include <boost/foreach.hpp>
#endif

//#define INPUT_FILE "A-small-attempt1.in"
//#define OUTPUT_FILE "A-small-attempt1.out"
#define INPUT_FILE "A-large.in"
#define OUTPUT_FILE "A-large.out"

using namespace std;

bool match( string const & test, string const & instr ){

#ifdef DEBUG
	cout << test << "," << instr << endl;
#endif

	for(unsigned int i=0,ti=0; i<instr.size(); ++i){

		if(test[ti]=='('){
			int len=0;
			bool hit=false;

			do{
				len++;
				if(test[ti+len]==instr[i]){
					hit=true;
					break;
				}
			}while( test[ti+len]!=')' );

			if(hit){
				while( test[ti++]!=')' )
					;
			}else{
				return false;
			}
		}else{
			if(test[ti]!=instr[i]){
				return false;
			}
			++ti;
		}
	}
	return true;
}

int main(){

	int L; // length
	int D; // lines
	int N; // test.size()

	typedef set< string > Set;
	Set words;

	fstream fin(INPUT_FILE);
	ofstream fout(OUTPUT_FILE);

	fin >> L >> D >> N;

	// input lines
	for(int i=0; i<D; ++i){
		string tmp;
		fin >> tmp;
		words.insert(tmp);
	}

#ifdef DEBUG
	BOOST_FOREACH( string & str, words ){
		cout << str << "\n";
	}
	cout << endl;
#endif

	// test case
	for(int i=0; i<N; ++i){
		// output
		//   Case  #X: K
		// where X is the test case number, starting from 1,
		// and K indicates how many words in the alien language match the pattern. 
		string testCase;
		fin >> testCase;
		int matchCount=0;

		for( Set::const_iterator iter=words.begin(), end_=words.end()
		   ; iter!=end_; ++iter )
		{
			if(match(testCase, *iter)){
				++matchCount;
			}
		}
		fout << "Case #" << i+1 << ": " << matchCount << endl;
	}

	return (0);
}




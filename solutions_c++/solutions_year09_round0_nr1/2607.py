#include <iostream>
#include <vector>

using namespace std;

class Token {

      public:
      vector<char> tknStream;
      int nextChar;
      int fixed;

      int FindMatch( char check ) {

	    int found = 0;

	    for( int q =0; q < tknStream.size(); q++ ) {

		  if( check == tknStream[q] ) {
			found = 1;
			break;
		  }
	    }

	    return( found );
      }
};

int main() {

      int L = 0; 	// length of the word;

      int D = 0;	// Number of given words in the dictionary

      int N = 0;	// Number of test cases

      vector<string> word;	// This vector contains the given words

      string singleWord;

      vector<string> pattern;	// This vector contains the given patterns

      string singlePattern;

      vector<Token> vecTokens;

      cin >> L;

      cin >> D;

      cin >> N;

      // reading given words in the dictionary
      for( int i = 0; i < D; i++ ) {
	    singleWord.erase();

	    cin >> singleWord;

	    word.push_back( singleWord );
      }

      // reading the given patterns

      for( int i= 0; i < N; i++ ) {

	    singlePattern.erase();

	    cin >> singlePattern;

	    pattern.push_back( singlePattern );
      }

      //cout << pattern[0][0] << endl;

      // Breaking the patterns into tokens and find whether each letter in the word matches with one in the 
      // respective token.

      int varToken = 0;
      Token objToken;

      for( int i = 0; i < pattern.size(); i++ ) {

	    vecTokens.clear();
	    objToken.tknStream.clear();

	    for( int j = 0; j < pattern[i].length(); j++ ) {

		  if( pattern[i][j] == '(' ) {

			varToken = 1;
			objToken.tknStream.clear();
			objToken.fixed = 0;
			objToken.nextChar = 0;
			objToken.tknStream.push_back(pattern[i][j]);

		  } else if( pattern[i][j] == ')' ) {

			varToken = 0;
			objToken.tknStream.push_back(pattern[i][j]);
			vecTokens.push_back( objToken );
			objToken.tknStream.clear();

		  } else if( varToken == 0 ) {

			objToken.fixed = 1;
			objToken.nextChar = 0;
			objToken.tknStream.push_back(pattern[i][j]);

			//if( pattern[i][j+1] == '(' || pattern[i][j+1] == '\0' ) {

			 vecTokens.push_back(objToken);
			//}

			objToken.tknStream.clear();


		  } else if( varToken == 1 ) {

			objToken.tknStream.push_back(pattern[i][j]);

		  }
	    }

	    /* for( int k = 0; k < vecTokens.size(); k++ ) {

		  cout << vecTokens[k].fixed << endl;
		  for( int m = 0; m < vecTokens[k].tknStream.size(); m++ ) {
			cout << vecTokens[k].tknStream[m];
		  }

		  cout << endl;
	    } */ 

	    int match = 0;	// match = 1 is a letter matches with the one in token.
	    int matchWords = 0;
	    for( int h = 0; h < word.size(); h++ ) {

		for( int w = 0; w < word[h].length(); w++ ) {

		    match = vecTokens[w].FindMatch(word[h][w]);

		    if( match == 0 ) 
			  break;
		}
		if( match == 1 )
		      matchWords++;
	    }

	    cout << "Case #" << i+1 << ": " << matchWords << endl;

      } // end of for  processing

}	// End of main

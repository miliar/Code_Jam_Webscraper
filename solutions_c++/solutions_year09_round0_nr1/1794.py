#include <iostream>
#include <algorithm>
#include <functional>
#include <vector>
#include <set>
#include <string>


//#define DEBUG

using namespace std;

void scanLine(string line, int L, set<char>* ch)
{

	int iCh = 0;
	int parenthesis = 0;
	for( size_t i = 0; i < line.size(); i++ ){
		char c = line.at(i);
		if( c == '(' ){
			parenthesis = 1;
		}else if( c == ')' ){
			iCh++;
			parenthesis = 0;
		}else{
			ch[iCh].insert( c );
			if( parenthesis == 0 ) iCh++;
		}
	}

	return;
}


int main(int argc, char** argv)
{
	//freopen("test2.in", "r", stdin );
	//freopen("test.out", "w", stdout );
	//freopen("A-small-attempt0.in", "r", stdin );
	//freopen("A-small-attempt0.out", "w", stdout );
	//freopen("A-large.in", "r", stdin );
	//freopen("A-large.out", "w", stdout );

	int L, D, N;
	string line;
	char table[5000][16];

	cin >> L >> D >> N;
	getline(cin, line, '\n');
	for( int iD = 0; iD < D; iD++){
		getline(cin, line, '\n');
		//cout << line << endl;

		strcpy( table[iD], line.c_str() );
	}

#ifdef DEBUB
	for( int iD = 0; iD < D; iD++){
		cout << table[iD] << endl;
	}
#endif //DEBUG


	for( int iN = 0; iN < N; iN++ ){
		getline(cin, line, '\n');
		
		set<char> ch[15];
		scanLine(line, L, ch);
#ifdef DEBUG
		cout << "* " << line << endl;
		for( int iL = 0; iL < L; iL++){
			cout << "- " ;
			for( set<char>::iterator iter = ch[iL].begin(); iter != ch[iL].end(); ++iter){
				cout << *iter;
			}
			cout << endl;
		}
#endif//DEBUG

		// Iterator word
		int numCnd = 0;
		for( int iD = 0; iD < D; iD++){
			//if( cnd[iD] == 0) continue;

			char* word = table[iD];

			int notFound = 0;
			for( int iL = 0; iL < L; iL++){
				if( ch[iL].find( word[iL] ) == ch[iL].end() ){
					notFound = 1;
					break;
				}
			}
			if( notFound == 0 ){
				numCnd++;

#ifdef DEBUG
				printf("Found: %s\n", word );
#endif //DEBUG
			}
		}
		
		printf( "Case #%d: %d\n", iN+1, numCnd );

	}
}
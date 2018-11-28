#include <iostream>
#include <set>
#include <string>
#include <list>
#include <vector>
using namespace std;

int main() {
    int L, D, N;
    vector<string> dict;
    cin >> L >> D >> N;
    for ( int i = 0; i < D; i++ ) {
	string buf;
	cin >> buf;
	dict.push_back( buf );
    }

    for ( int i = 0; i < N; i++ ) {
	string buf;
	cin >> buf;
	set<char> pattern[L];
	int ind = 0;
	for ( int j = 0; j < L; j++ ) {
	    if ( buf[ind] != '(' ) {
		pattern[j].insert( buf[ind] );
		ind++;
	    } else {
		for ( ;; ) {
		    ind++;
		    if ( buf[ind] == ')') {
			ind++;
			break;
		    }
		    pattern[j].insert( buf[ind] );
		}
	    }
	}
/*
	int num[L],comnum[L];
	for ( int j = 0; j < L; j++ ) {
	    num[j] = pattern[j].size();
	    if ( j == 0 ) {
		comnum[j] = 1;
	    } else {
		comnum[j] = comnum[j-1] * num[j-1];
	    }
	    //cout << pattern[j].front() << ":" << pattern[j].back() << '\t';
	}
	//cout << endl;

	int result = 0;
	for ( int j = 0; j < comnum[L-1] * num[L-1]; j++ ) {
	    string buf;
	    for ( int k = 0; k < L; k++ ) {
		int ind = ( j / comnum[k] ) % num[k];
		buf.push_back( pattern[k][ind] );
	    }
	    
	    if ( dict.find( buf ) != dict.end() ) {
		result++;
	    }
	}
	cout << "Case #" << i + 1 << ": " << result << endl;
*/
	int result = 0;
	for ( int j = 0; j < D; j++ ) {
	    bool match = true;
	    for ( int k = 0; k < L; k++ ) {
		if ( pattern[k].find( dict[j][k] ) == pattern[k].end() ) {
		    match = false;
		    break;
		}
	    }
	    if ( match ) result++;
	}
	cout << "Case #" << i + 1 << ": " << result << endl;
    }
    return 0;
}

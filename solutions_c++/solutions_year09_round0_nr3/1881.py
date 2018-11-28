#include <iostream>
#include <iomanip>
using namespace std;

int main() {
    int N;
    cin >> N;
    string str;
    string welcome = "welcome to code jam";
    getline( cin, str);
    for ( int Case = 0; Case < N; Case++ ) {
	string str;
	getline( cin, str);

	int num[19][str.size()];
	for ( int i = 0; i < 19; i++ ) {
	    for ( int j = 0; j < str.size(); j++ ) {
		num[i][j] = 0;
	    }
	}
	
	for ( int i = str.size() - 1; i >= 0; i-- ) {
	    if ( i == str.size() - 1 ) {
		if ( str[i] == welcome[18] ) {
		    num[18][i] = 1;
		} else {
		    num[18][i] = 0;
		}
	    } else {
		if ( str[i] == welcome[18] ) {
		    num[18][i] = 1 + num[18][i+1];
		} else {
		    num[18][i] = num[18][i+1];
		}
	    }
	    //cout << num[18][i] << endl;
	}
	
	for ( int i = 17; i >= 0; i-- ) {
	    for ( int j = str.size() - 1; j >= 0; j-- ) {
		if ( j > str.size() - 19 + i ) {
		    num[i][j] = 0;
		} else {
		    if ( str[j] == welcome[i] ) {
			num[i][j] = num[i][j+1] + num[i+1][j+1];
			while ( num[i][j] > 10000 ) {
			    num[i][j] -= 10000;
			}
		    } else {
			num[i][j] = num[i][j+1];
		    }
		}
//		if ( num[i][j] != 0 )
		//cout << "num[i][j]: " << num[i][j] << endl;
	    }
	}
	cout << "Case #" << Case+1 << ": ";
	cout << setfill('0');
	cout << setw(4) << num[0][0] << endl;
    }
    return 0;
}

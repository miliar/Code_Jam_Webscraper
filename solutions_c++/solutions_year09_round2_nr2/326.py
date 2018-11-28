#include <iostream>
#include <iomanip>
#include <vector>
#include <string>
#include <map>
#include <set>
#include <boost/lexical_cast.hpp>

using namespace std;

string trim(string s)
{
    int idx = 0;
    while( s[idx] == '0' ) idx++;
    return s.substr(idx);
}
    
string solve(string s)
{
    char maxch = '9' + 1;
    for(int i=s.size()-1;i>=0;i--){
	char m = maxch;
	int idx;
	for(int j=i+1;j<s.size();j++){
	    if( s[i] < s[j] && m > s[j] ){
		m = s[j];
		idx = j;
	    }
	}
	if( m != maxch ){
	    swap( s[i], s[idx] );
	    string rest = s.substr(i+1);
	    sort(rest.begin(), rest.end());
	    return trim(s.substr(0, i+1) + rest);
	}
    }
    /*
    sort(s.begin(), s.end());
    int cnt = 0, i = 0;
    while( s[i] == '0' )i++;
    return s[i] + string(i+1, '0') + s.substr(i+1);
    */
}

		

int main(void)
{
    int T;
    string dummy;
    cin >> T;
    getline(cin, dummy);

    for(int i=0;i<T;i++){
	string s;
	getline(cin, s);
	s = "0" + s;
	cout << "Case #" << (i+1) << ": " << solve(s) << endl;
    }
    
    return 0;
}


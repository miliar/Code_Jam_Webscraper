#include <iostream>
#include <string>
#include <map>
#include <list>

using namespace std;

int main() {
	int t, c, d;
	string in, pair;
	map<char, char> opposed;
	map<string, char> combined;
	list<char> invoke;
	bool inta;

	cin >> t;
	for(int j=0; j<t; j++) {
		opposed.clear();
		combined.clear();
		invoke.clear();
		list<char>::iterator it;

		cin >> c;
		for(int i=0; i<c; i++) {
			cin >> in;
			combined[ in.substr(0,2) ] = in[2];
			combined[ in.substr(1,1) + in.substr(0,1) ] = in[2];
		}

		cin >> d;
		for(int i=0; i<d; i++) {
			cin >> in;
			opposed[ in[0] ] = in[1];
			opposed[ in[1] ] = in[0];
		}
		cin >> d;
		cin >> in;

		
		for(int i=0; i<in.size(); i++) {
			if( invoke.size()>0 ) {
				pair = "";
				pair = pair + invoke.back() + in[i];
			}

			//cout << pair << endl;
			if( invoke.size()>0 && combined[ pair ]!=0 ) {
				invoke.pop_back();
				invoke.push_back( combined[ pair ] );
			} else if( invoke.size()>0 && opposed[ in[i] ]!=0 ) {
				inta = true;
				for(it = invoke.begin(); it!= invoke.end() && inta; it++) {
					if( *it == opposed[ in[i] ] ) {
						invoke.clear();
						inta = false;
			   		}
				}
				if(inta) invoke.push_back( in[i] );
			} else {
				invoke.push_back( in[i] );
			}
		}

		cout << "Case #" << j+1 << ": [";
		if( invoke.size() > 0) cout << *(invoke.begin());
		for(it = ++(invoke.begin()); it!= invoke.end(); it++)
		    	cout << ", " << *it;
		cout << "]\n";
    	}
}


#include <string>
#include <set>
#include <iostream>

using namespace std;

int main ( ) {

	int cases;
	cin >> cases; 
	for ( int caseno = 1; caseno <= cases; caseno++) {
			int existing;
		int created;
		cin >> existing >> created;

		set <string> paths;
		paths.insert("/");
		for ( int i = 0; i < existing; i ++ ) {
			string p ; cin >> p;
			paths.insert(p);
		}
		int mkdirs = 0;
		for ( int i = 0; i < created; i++ ) {
			string p;
			cin >> p;
			
			if ( p == "/" )
				continue;
			for ( int a = 1; a < p.size(); a ++) {
				if ( p[a] == '/' ) {
					if ( paths.find(p.substr(0, a)) == paths.end()) {
						mkdirs += 1;
						paths.insert(p.substr(0, a));
						cerr << "mkdir " << p.substr(0, a) << endl;
					}
					else 
						cerr << "exists " << p.substr(0, a) << endl;
					
				}
				
				
			}
			if ( paths.find(p) == paths.end() ) {
					mkdirs += 1;
					paths.insert(p);
					cerr << "mkdir " << p << endl;
			}
			else {
				cerr << "exists " << p << endl;
			}
		}
		cout << "Case #" << caseno << ": " << mkdirs << endl;
		
	}

	return 0;

}
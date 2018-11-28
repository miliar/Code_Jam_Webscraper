#include <iostream>
#include <string>
#include <string.h>

using namespace std;

char combine[300][300];
bool opposed[300][300];

int main(){
	int T;
	int C, D, N, n;
	string s;
	char c;
	
	cin >> T;
	for (int t=1; t<=T; t++){
		memset( combine, 0, sizeof combine );
		memset( opposed, 0, sizeof opposed );
		
		cin >> C;
		for (int i=0; i<C; i++){
			cin >> s;
			combine[ s[0] ][ s[1] ] = s[2];
			combine[ s[1] ][ s[0] ] = s[2];
		}
		cin >> D;
		for (int i=0; i<D; i++){
			cin >> s;
			opposed[ s[0] ][ s[1] ] = true;
			opposed[ s[1] ][ s[0] ] = true;
		}
		
		cin >> N;
		s = "";
		for (int i=0; i<N; i++){
			cin >> c;
			s += c;
			n = s.length();
			if ( n > 1 ){
				if ( combine[ s[n-1] ][ s[n-2] ] ) s = s.substr(0,n-2) + combine[ s[n-1] ][ s[n-2] ];
				
				for (int j=0; j<n; j++)
					if ( opposed[ s[j] ][ s[n-1] ] ){
						s = "";
						break;
					}
			}
		}
		
		cout << "Case #" << t << ": [";
		for (int i=0; i<s.length(); i++){
			if ( i ) cout << ", ";
			cout << s[i];
		}
		cout << "]" << endl;
	}
	
	return 0;
}

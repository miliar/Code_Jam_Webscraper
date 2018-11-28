#include <iostream>
#include <algorithm>
#include <cmath>
#include <math.h>
#include <stdio.h>
#include <cstring>
#include <vector>
#include <map>
#include <string>
#include <set>
#include <sstream>
#include <iomanip>

#define S               second
#define pi  		2 * acos(0.0)
#define sz(a)   	int((a).size()) 
#define pb 		push_back 
#define tr(c,i) 	for(typeof((c).begin() i = (c).begin(); i != (c).end(); i++) 
#define present(c,x) 	(find(all(c),x) != (c).end()) 

using namespace std;

int main(){
	//freopen("input.txt", "r", stdin);
	//freopen("output.txt", "w", stdout);
	int t, cs = 0;string s = "";
	cin >> t;vector<string> ret;
	while(t--){cs++;ret.clear();
		string ar[4];
		for(int i = 0; i < 4; i++){
			cin >> ar[i];
			ret.pb(ar[i]);
		}s = "";string a = "";bool flag = false;
		for(int i = 0; i < 4; i++){s = "";
			for(int j = 0; j < 4; j++){if(i == j){a += ar[j][i];}
				s += ar[j][i];
				if(ar[j][i] == '.'){flag = true;}
			}
			ret.pb(s);
		}
		ret.pb(a);
		a = ""; bool x = false;bool o = false; bool dr = false;
		a += ar[3][0];  a += ar[2][1];  a += ar[1][2];  a += ar[0][3];
		ret.pb(a);
		for(int i = 0; i < sz(ret); i++){int b = 0, c = 0; 
			for(int j = 0; j < 4; j++){
				if(ret[i][j] == 'X' || ret[i][j] == 'T')b++;
				  if(ret[i][j] == 'O' || ret[i][j] == 'T')c++;

			}
			if(b == 4) x = true;
			if(c == 4) o = true;
		}
		if(x == false && o == false){dr = true;}
		bool g = false;
		if(x == true){cout << "Case #" <<cs <<": X won" << endl;g = true;}
		 if(o == true && g == false){cout << "Case #" <<cs <<": O won" << endl;g = true;}
		 if(flag == true && g == false){cout << "Case #" <<cs <<": Game has not completed" << endl;g = true;}
		if(g == false){cout << "Case #" <<cs <<": Draw" << endl;g = true;}
	}
        
	return 0;
}


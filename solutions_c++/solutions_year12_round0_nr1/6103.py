/* https://code.google.com/codejam/contest/1460488/dashboard#s=p0 */

#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <string>

using namespace std;


int main() {
	int T;
	cin>>T;

	map<char, char> M; 
	M['a'] = 'y';
	M['b'] = 'h';
	M['c'] = 'e';
	M['d'] = 's';
	M['e'] = 'o';
	M['f'] = 'c';
	M['g'] = 'v';
	M['h'] = 'x';
	M['i'] = 'd';
	M['j'] = 'u';
	M['k'] = 'i';
	M['l'] = 'g';
	M['m'] = 'l';
	M['n'] = 'b';
	M['o'] = 'k';
	M['p'] = 'r';
	M['q'] = 'z';
	M['r'] = 't';
	M['s'] = 'n';
	M['t'] = 'w';
	M['u'] = 'j';
	M['v'] = 'p';
	M['w'] = 'f';
	M['x'] = 'm';
	M['y'] = 'a';
	M['z'] = 'q';
		
	string str;
	getline(cin, str); // dummy
	
	for(int i = 0; i < T; i++) {
		str.clear();
		getline(cin, str);
		for(int j = 0; j < str.length(); j++) {
			if(str[j] >= 'a' && str[j] <= 'z')
				str[j] = M[str[j]];
		}
		cout<<"Case #"<<i+1<<": "<<str<<endl;
	}
}
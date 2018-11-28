#include <vector>
#include <valarray>
#include <list>
#include <map>
#include <set>
#include <queue>
#include <deque>
#include <stack>
#include <algorithm>
#include <sstream>
#include <bitset>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <cstring>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <complex>

using namespace std;

int main(){
	freopen("A-small-attempt0.in","r",stdin);
	freopen("A.out","w",stdout);
	
	map<char, char> key;
	key['a'] = 'y'; 
	key['b'] = 'h'; 
	key['c'] = 'e'; 
	key['d'] = 's'; 
	key['e'] = 'o'; 
	key['f'] = 'c'; 
	key['g'] = 'v'; 
	key['h'] = 'x'; 
	key['i'] = 'd';
	key['j'] = 'u'; 
	key['k'] = 'i'; 
	key['l'] = 'g';
	key['m'] = 'l'; 
	key['n'] = 'b'; 
	key['o'] = 'k';
	key['p'] = 'r'; 
	key['q'] = 'z'; 
	key['r'] = 't'; 
	key['s'] = 'n';
	key['t'] = 'w'; 
	key['u'] = 'j'; 
	key['v'] = 'p';
	key['w'] = 'f'; 
	key['x'] = 'm'; 
	key['y'] = 'a'; 
	key['z'] = 'q';
	key[' '] = ' ';
	
	int N;
	cin >> N;
	cin.ignore();
	string msg;
	for(int n = 0; n < N; n++){
		getline(cin, msg); // read current line
		string trans_msg = "";
		for(int i = 0; i < msg.size(); i++)
			trans_msg += key[msg[i]];
		cout << "Case #" << n+1 << ": " << trans_msg << endl;
	}
	return 0;
}

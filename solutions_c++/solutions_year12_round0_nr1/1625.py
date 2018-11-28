#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
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
#include <cstring>

using namespace std;

int main(){

	freopen("1.in", "r", stdin);
	freopen("1.out", "w", stdout);
	int t;
	cin>>t;
	string x;
	string y = "";
	for(int i = 0; i <= t; i++){

		while(	getline(cin,  x)) break;
		int n = x.size();

		for(int j = 0; j < n; j++){

			if(x[j] == ' ') y += " ";
			else if(x[j] == 'a') y += "y";
			else if(x[j] == 'b') y += "h";
			else if(x[j] == 'c') y += "e";
			else if(x[j] == 'd') y += "s";
			else if(x[j] == 'e') y += "o";
			else if(x[j] == 'f') y += "c";
			else if(x[j] == 'g') y += "v";
			else if(x[j] == 'h') y += "x";
			else if(x[j] == 'i') y += "d";
			else if(x[j] == 'j') y += "u";
			else if(x[j] == 'k') y += "i";
			else if(x[j] == 'l') y += "g";
			else if(x[j] == 'm') y += "l";
			else if(x[j] == 'n') y += "b";
			else if(x[j] == 'o') y += "k";
			else if(x[j] == 'p') y += "r";
			else if(x[j] == 'q') y += "z";
			else if(x[j] == 'r') y += "t";
			else if(x[j] == 's') y += "n";
			else if(x[j] == 't') y += "w";
			else if(x[j] == 'u') y += "j";
			else if(x[j] == 'v') y += "p";
			else if(x[j] == 'w') y += "f";
			else if(x[j] == 'x') y += "m";
			else if(x[j] == 'y') y += "a";
			else if(x[j] == 'z') y += "q";
		}
		if(i != 0)
		cout<<"Case #"<<i<<": "<<y<<endl;
		y = "";

	}

return 0;
}

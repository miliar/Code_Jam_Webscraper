#include <fstream>
#include <cmath>
#include <iostream>

using namespace std;

ifstream in("in");
ofstream out("out");

void sol(){
	int n, x, l = 0, spent = 0, pos[2];
	in >> n;
	char last, c;
	pos[0] = pos[1] = 1;
	for(int i = 0; i < n; i++){
		in >> c >> x;
		int d = abs(x - pos[c == 'B']);
		pos[c == 'B'] = x;
		if(c == last)
			spent += d;
		else{
			last = c;
			l += spent;
			if(d > spent) spent = d - spent;
			else spent = 0;
		}
		spent++;//button press
		//out << endl << "spent: " << spent << " l: " << l << endl;
	}
	out << l + spent;
}

int main(){
	int n;
	in >> n;
	for(int i = 0; i < n; i++) 
		out << "Case #" << i + 1 << ": ",
		sol(), out << endl;
}

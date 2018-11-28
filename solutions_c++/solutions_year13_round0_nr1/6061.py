#include <cstdio>
#include <cctype>
#include <cmath>
#include <cstdlib>

#include <string>
#include <iostream>
#include <fstream>
#include <vector>
#include <queue>
#include <map>
#include <set>
#include <algorithm>

#define pb push_back
#define fi(it, v) for (typeof((v).begin()) it = (v).begin(); it != (v).end(); ++it)
#define fit(v) fi(it, v)
#define f(i,n) for(int i = 0; i < (n); ++i)

#define fs first
#define sc second
#define mp make_pair

#define all(v) (v).begin(), (v).end()
#define ll long long int
#define vi vector<int>
#define vii vector<vi >
using namespace std;
int x,o,d;

void check(string s){
	int xc = 0, oc = 0;
	fit(s) 
		if (*it == 'X') xc++;
		else if (*it == 'O') oc++;
		else if (*it == 'T') {xc++; oc++;}
		else d = 1;
	x = max(x,xc);
	o = max(o, oc);
}

int main(){
	
	ofstream output;
	output.open("problemA.out");
	ifstream input;
	input.open("problemA.in");
	
	int t; input >> t;
	for(int c = 1; c <= t; ++c){
		x = 0; o = 0; d = 0;
		vector<string> m;
		string s;
		f(i,4){
			input >> s;
			m.pb(s);
			check(s);
		}
		f(i,4){
			s.clear();
			f(j,4) s.pb(m[j][i]);
			check(s);
		}
		s.clear();
		f(i,4) s.pb(m[i][i]);
		check(s);
		s.clear();
		f(i,4) s.pb(m[i][3-i]);
		check(s);
		
		output << "Case #" << c << ": ";
		if (x == 4) output << "X won";
		else if (o == 4) output << "O won";
		else if (d) output << "Game has not completed";
		else output << "Draw";
		
		output << endl;
	}
	output.close();
	return 0;
}

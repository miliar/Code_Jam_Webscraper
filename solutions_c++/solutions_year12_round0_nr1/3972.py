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
#include <fstream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
using namespace std;

#define pb push_back
#define mp make_pair
#define sz(v) ((int)(v).size())
#define all(v) (v).begin(),(v).end()
#define f(i,a,b) for(int i=(a);i<(b);++i)
#define fr(i,a,b) for(int i=(a);i>(b);--i)
#define fe(i,a,b) for(int i=(a);i<=(b);++i)
#define fre(i,a,b) for(int i=(a);i>=(b);--i)
string itoa(int i) { stringstream ss; ss<<i; return ss.str(); }
#define same(a,b) (fabs((a)-(b))<0.0000001)
#define even(a) ((a)%2==0) 
#define odd(a)  ((a)%2==1)
#define present(c,x) ((c).find(x) !=(c).end())
#define cpresent(c,x) (find(all(c),x)) 

char translate(char c) {
	switch(c) {
	case 'a': return 'y';
	case 'b': return 'h';
	case 'c': return 'e';
	case 'd': return 's';
	case 'e': return 'o';
	case 'f': return 'c';
	case 'g': return 'v';
	case 'h': return 'x';
	case 'i': return 'd';
	case 'j': return 'u';
	case 'k': return 'i';
	case 'l': return 'g';
	case 'm': return 'l';
	case 'n': return 'b';
	case 'o': return 'k';
	case 'p': return 'r';
	case 'q': return 'z';
	case 'r': return 't';
	case 's': return 'n';
	case 't': return 'w';
	case 'u': return 'j';
	case 'v': return 'p';
	case 'w': return 'f';
	case 'x': return 'm';
	case 'y': return 'a';
	case 'z': return 'q';
	}
	return c;
}
int main() {
	int T;
	char input[101] = {0};
	ifstream infile;
	ofstream outfile;
	infile.open("A-small-attempt0.in");
	outfile.open("Qual-A-small0-out.in");
	infile.getline(input, 101);
	T = atoi(input);
	fe(t, 1, T) {
		char s[101] = {0};
		infile.getline(s, 101);
		int endIndex = 0;
		while(s[endIndex] != '\r' && s[endIndex] != '\n' && s[endIndex] != '\0') endIndex++;
		f(i,0,endIndex) {
			s[i] = translate(s[i]);
		}
		outfile << "Case #" << t << ": " << s << endl;;
		cout << "Case #" << t << ": " << s << endl;;
	}

	return 0;
}
//Arash Rouhani

#include <iostream>
#include <vector>
#include <algorithm>
#include <sstream>
#include <string>
#include <math.h>
#include <fstream>
#include <numeric>

using namespace std;

typedef pair < int, int > II;
typedef vector < int > VI;
typedef vector < II > VII;
typedef vector < VI > VVI;
typedef vector < string > VS;
typedef vector < VS > VVS;
typedef long long  LL;
#define all(c) c.begin(), c.end()
#define tr(c, it) for(typeof((c).begin()) it = (c).begin(); it!=(c).end(); it++)
#define sfor(type, e, start, stop) for(type e=start; e<stop; e++)


int l, d, n;

VS wordexp;

struct Chartree {
	Chartree* values[256];
};

Chartree ct;

int count(Chartree *n, int d=0){
	if(d==l)
		return 1;
	int sum = 0;
	tr(wordexp[d], c)
		if((*n).values[(int)*c]!= NULL)
			sum += count((*n).values[(int)*c], d+1);
	return sum;
}

int main(){
	cin >> l >> d >> n;
	VS wordlist(d);
	Chartree *cnode;
	tr(wordlist, word){
		cnode = &ct;
		cin >> *word;
		tr(*word, c){
			Chartree *& nn = (*cnode).values[(int)*c];
			if(nn == NULL)
				nn = new Chartree;
			cnode = nn;
		}
	}

	sfor(int, testcase, 1, n+1){
		string word;
		cin >> word;
		int cid=0;
		wordexp.clear();
		wordexp.resize(l);
		int t=1;
		sfor(int, i, 0, word.length()){
			if(word[i]=='(')
				t=0;
			else if(word[i]==')'){
				t=1;
				cid++;
			}else{
				wordexp[cid].push_back(word[i]);
				cid+=t;
			}
		}
		cout << "Case #" << testcase << ": " << count(&ct) << endl;
	}

}

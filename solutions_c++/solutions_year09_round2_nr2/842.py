#include <algorithm>
#include <fstream>
#include <string>
#include <queue>
#include <set>
#include <stack>
#include <map>
#include <sstream>
#include <iostream>
#include <cmath>
using namespace std;

typedef unsigned int uint;
typedef long long int64;
typedef vector<int> vi;
typedef vector<string> vs;
typedef pair<int,int> pI;
typedef pair<string,int> pSI;
typedef pair<int,string> pIS;

#define FOR(i,n) for(int i=0, upTo##i=n; i<upTo##i; ++i)
#define REVFOR(i,n) for(int i=(n)-1; i>=0; --i)
#define FOR2(i,b,n) for(int i=b; i<(n); ++i)
#define REVFOR2(i,b,n) for(int i=(n)-1; i>=b; --i)
#define SC(i) scanf("%d", i)
#define ALL(C) (C).begin(), (C).end()
#define RALL(C) (C).rbegin(), (C).rend()
#define MIN(C) *min_element(ALL(C))
#define MAX(C) *max_element(ALL(C))
#define A first
#define B second

string findNext(string s) {
	char smallest = s[s.size()-1];

	string s2 = s;
	if (next_permutation(s2.begin(), s2.end()) == false)
	{
		sort(s.begin(), s.end());
		int i=0;
		while(i < s.size() && s[i] == '0')
			++i;

		s = s.substr(i,1) + s.substr(0,i) + s.substr(i+1);


		s.insert(s.begin()+1, '0');
		return s;
	}
	else 
		return s2;

/*
	int i=s.size()-2;
	while(i>=0) 
	{
		if (s[i] < smallest)
			break;

		--i;
	}


	
	return res;*/
}

int main(void) {
    int n; SC(&n);
    FOR(_i,n) {
		string s; 
		cin>>s;

        printf("Case #%d: %s\n", _i+1, findNext(s).c_str());
    }
    return 0;
}

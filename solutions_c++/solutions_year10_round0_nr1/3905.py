

#include "template.h"
#include <cstdio>
#include <iostream>
#include <sstream>
#include <algorithm>
#include <utility>
#include <vector>
#include <sstream>
#include <map>
#include <set>

using namespace std;

#define FOR(i,a,b) for(int i = a; i <b ; i++)
#define FRR(i,a,b) for(int i = b - 1; i >=a ; i--)
#define sz size()
#define pb push_back
#define VI vector<int>
#define VVI vector<VI>
#define eps 1e-9


int main(){
	int cases;
	cin >> cases;
	FOR(caseNum, 0, cases){
		long long int N, K;
		cin >> N >> K;
		cout << "Case #" << caseNum+1 << ": " << ((K+1) % (1 << N) == 0? "ON":"OFF") << endl;
	}
	
}
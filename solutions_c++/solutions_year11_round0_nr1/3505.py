#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <queue>
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
#include <cctype>
#include <string>
#include <cstring>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>

using namespace std;

#define FOR(i, a, b) for (int i(a), _b(b); i <= _b; ++i)
#define REP(i, n) for (int i(0), _n(n); i < _n; ++i)

ifstream fin("C:\\Users\\Администратор\\Downloads\\A-large.in");

int solve(){
	int n,cc;
	int ret;
	vector <char> who;
	vector <int> b;

	fin >> n;
	who.resize(n);
	b.resize(n);


	
	REP(i,n){
		fin >> who[i];
		fin >> b[i];
	}

	ret=0;
	int at1,at2;
	int done =0;
	int t1,t2;
	at1=at2=1;
	t1=t2=1;
	int i;
	i=done;
	while(i<n && who[i]!='O'){
		i++;
	}
	if(i<n)t1 = b[i];

	i=done;
	while(i<n && who[i]!='B'){
		i++;
	}
	if(i<n)t2 = b[i];

	
	while(done<n){
		if(who[done]=='O'){
			if(t1!=at1){
				if(t1<at1) at1--;
				if(t1>at1) at1++;

				if(t2<at2) at2--;
				if(t2>at2) at2++;

			} else {
				done++;
				i=done;
				while(i<n && who[i]!='O'){
					i++;
				}
				if(i<n)t1 = b[i];
				if(t2<at2) at2--;
				if(t2>at2) at2++;
			}
		} else { // for B
			if(t2!=at2){
				if(t1<at1) at1--;
				if(t1>at1) at1++;

				if(t2<at2) at2--;
				if(t2>at2) at2++;

			} else {
				done++;
				i=done;
				while(i<n && who[i]!='B'){
					i++;
				}
				if(i<n)t2 = b[i];
				if(t1<at1) at1--;
				if(t1>at1) at1++;
			}
		}


		ret++;
	}

	return ret;
}

int main(){
	int T;

	ofstream fout("I:\GCJ-Q-A.txt");

	fin >> T;
	cout << T << endl;
	REP(i,T){
		fout << "Case #" << i+1 << ": " << solve() << endl;
	}

	fin.close();
	fout.close();

	system("pause");
	return 0;
}
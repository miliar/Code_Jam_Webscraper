#include <iostream>
#include <map>
#include <vector>
#include <string>
#include <algorithm>

#define REP(i,n) for(typeof(n) _n=n, i=0;i<_n;++i)
#define FOREACH(i,x) for(typeof((x).begin()) i = (x).begin(); i != (x).end(); i++)
#define ALL(x) (x).begin(),(x).end()
#define INFTY 1000000

using namespace std;

void runCase(){
	int k;
	string text;
	cin >> k;	
	getline(cin,text);
	getline(cin,text);	
	//cin >> text;	
	//cerr << text << endl;

	vector<int> perm(k);
	REP(i,k) perm[i] = i;

	int bestSize = INFTY;

	do{
		string text2(text);
		REP(i,text.size())
			text2[i] = text[k*(i/k) + perm[i%k]];
		//cerr << text2 << endl;
		int size = 1;
		for(int i=1;i<text2.size();i++)
			if (text2[i] != text2[i-1])
				size++;
		bestSize = min(size,bestSize);
	} while (next_permutation(ALL(perm)));
	cout << bestSize << endl;
}

int main(){
	int cases;
	cin >> cases;
	string s;
	getline(cin,s);
	REP(i,cases){
		cout << "Case #" << i+1 << ": ";
		runCase();
	}
	return 0;
}

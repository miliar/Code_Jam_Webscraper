#include <vector>
#include <string>
#include <map>
#include <iostream>
#include <algorithm>
#include <cmath>
#include <sstream>
#include <set>
#include <numeric>

using namespace std;

#define SZ(A) (A).size()
#define ALL(A) (A).begin(), (A).end()
#define SORT(A) sort(ALL(A))
#define REP(I,N) for(int I=0, I<N ; I++)
#define PB push_back

typedef vector<int> vi;
typedef vector<vi> vii;
typedef vector<long long> vl;
typedef vector<vl> vvl;

int P;
vector<int> rel;

long long min1 (long long a, long long b){
	if(a>b)	return b;
	return a;
}

long long go(vector<bool> &pr){

	if(SZ(rel) == 0) return 0;

	long long mi = 999999999;
	for(int i=0 ; i<SZ(rel) ; i++){
		unsigned long long cnt = 0;
		pr[rel[i]] = false;
		bool end = false;
		for(int j=rel[i]+1 ; j<=P && !end ; j++){
//			cout << "aa" << j << endl;
			if(pr[j] == false) end = true;
			else cnt++;
		}
		end = false;
		for(int j=rel[i]-1 ; j>=1 && !end ; j--){
//			cout << "bb" << j << endl;
			if(pr[j] == false) end = true;
			else cnt++;
		}
		int aux = rel[i];
//		cout << aux << endl;
		rel.erase(rel.begin()+i);
		mi = min1(mi, go(pr)+cnt);
		rel.insert(rel.begin()+i, aux);
		pr[rel[i]] = true;
	}
	return mi;
}

int main(){

	int T;
	cin >> T;
	for(int t=1 ; t<=T ; t++){
		rel.clear();
		int Q;
		cin >> P >> Q;

		vector<bool> pr(P+1, true);
		for(int i=0 ; i<Q ; i++){
			int aux;
			cin >> aux;
			rel.PB(aux);
		}

		long long coins = go(pr);

		cout <<"Case #"<<t<<": "<< coins <<endl;
	}

	return 0;
}

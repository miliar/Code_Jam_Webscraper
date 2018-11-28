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
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <fstream>

using namespace std;

#define REP(i,n) for((i)=0;(i)<(int)n;(i)++)
#define stoi(i,s) {istringstream is(s); is>>i;}

string intToStr(int k){
	ostringstream os;
	os << k;
	return os.str();
}


int main(int argc, char *argv[])
{
	int i,j,k;
	ifstream fin("A-large.in");
	ofstream fout("sample.out");
	string ss;
	getline(fin,ss);
	int T;
	int n;
	stoi(T,ss);
	REP(i,T){
		string answer = "";
		k = 0;
		unsigned long long ll = 0;
		unsigned long long base = 1;
		getline(fin,ss);
		set<char> symbol;
		REP(j,ss.size())  symbol.insert(ss.at(j));
		n = symbol.size();
		if(n==1)
		 n++;
		vector<int> v;
		v.push_back(0);
		for(j=2;j<n;j++)
			v.push_back(j);
		deque<unsigned long long> bases;
		for(j=ss.size()-1;j>=0;j--){
			bases.push_front(base);
			base *= n;
		}
		map<char,int> m;
		char c1 = ss.at(0);
		m[c1] = 1;
		answer += intToStr(1);
		ll += bases[0];
		for(j=1;j<ss.size();j++){
			if(m.count(ss.at(j))==1){
				ll += m[ss.at(j)]*bases[j];
			}else{
				m[ss.at(j)] = v[k++];
				ll += m[ss.at(j)]*bases[j];
			}
		}
		fout<<"Case #"<<i+1<<": "<<ll<<endl;
	}
    system("PAUSE");
    return EXIT_SUCCESS;
}

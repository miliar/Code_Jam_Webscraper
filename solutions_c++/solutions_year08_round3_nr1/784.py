#include <iostream>
#include <cmath>
#include <vector>
#include <string>
#include <fstream>
#include <cstdlib>
#include <algorithm>

#define IN_FILE "A-small-attempt0.in"

using namespace std;

struct Pr{
	uint freq, key, presses;

	friend bool operator<(const Pr&, const Pr&);
	friend bool greater(const Pr&, const Pr&);
	ostream& print(ostream &os){
		return os << "{freq: " << freq << ", key: " << key << ", presses: " << presses << "}";
	}
	friend ostream& operator<<(ostream &os, Pr &p);
};
bool operator<(const Pr& x, const Pr& y){
    return x.freq < y.freq;
}
bool greater(const Pr& x, const Pr& y){
    return x.freq > y.freq;
}

ostream& operator<<(ostream &os, Pr &p){
	return p.print(os);
}

int main(){
	ifstream ifs(IN_FILE);
	uint N;
	ifs >> N;
	for(int n = 1; n <= N; ++n){		
		uint letsPerKey, numKeys, numLetters;
		ifs >> letsPerKey >> numKeys >> numLetters;
		if(numLetters > letsPerKey*numKeys){cout << "Case #" << n << ": Impoosible\n"; continue;}
		vector<Pr> vec(numLetters);
		for(int i = 0; i < numLetters; ++i){
			ifs >> vec[i].freq;
			vec[i].key = i;
		}
		sort(vec.begin(), vec.end());
		uint press = 1;
		long long sum=0;
		for(int i = numLetters-1; i >= 0; --i){
			vec[i].presses = (numLetters-1-i)/numKeys+1;
			sum += vec[i].presses * vec[i].freq;
		}
		cout << "Case #" << n << ": " << sum << endl;
	}
}

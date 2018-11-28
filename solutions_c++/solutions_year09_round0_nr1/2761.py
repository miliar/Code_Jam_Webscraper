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

class Pattern
{
private:
	long bits[8];
public:
	void init(){
		for (int i=0;i<8;i++)
		{
			bits[i] = 0;
		}
	}
	void fill(){
		for (int i=0;i<8;i++)
		{
			bits[i] = LONG_MAX;
		}
	}
	void shift(int k){
		int idx = k/64;
		int i = k%64;
		long b = 1<<i;
		bits[idx] ^= b;
	}
	void bitAnd(Pattern p){
		for (int i=0;i<8;i++)
		{
			this->bits[i] &= p.bits[i];
		}
	}
	int has(int k){
		int idx = k/64;
		int i = k%64;
		long b = this->bits[idx]>>i;
		if(b%2==1)
			return 1;
		else
			return 0;
	}
	void printP(){
		for (int i=0;i<8;i++)
		{
			cout<<bits[i]<<" ";
		}
	}
};

int main(){
	int i,index;
	int begin = 0;
	char tmpc;
	int L,D,N;
	ifstream fin("A-small-attempt0.in");
	string s;
	getline(fin,s);
	istringstream is(s);
	is>>L>>D>>N;
	int *count = new int[N];
	string *languages = new string[D];
	Pattern **patterns = new Pattern*[27];
	for (i=0;i<N;i++){
		count[i] = 0;
	}
	for (i=1;i<=26;i++){
		patterns[i] = new Pattern[N];
	}
	for (i=1;i<27;i++){
		for (int j=0;j<N;j++){
			patterns[i][j].init();
		}
	}
    for(i=0;i<D;i++){
		getline(fin,s);
		languages[i] = s;
	}
	for (i=0;i<N;i++){
		getline(fin,s);
		index = 0;
		for (int j=0;j<s.length();j++){
			tmpc = s.at(j);
			if(tmpc=='('){
				begin = 1;
				continue;
			}else if(tmpc==')'){
				index++;
				begin = 0;
				continue;
			}else{
				if(begin==1){
					patterns[tmpc-96][index].shift(i);
				}else{
					patterns[tmpc-96][index].shift(i);
					index++;
				}
			}
		}
	}
	for(i=0;i<D;i++){
		Pattern p;
		p.fill();
		for (int j=0;j<L;j++){
			p.bitAnd(patterns[languages[i].at(j)-96][j]);
		}
		for (int k=0;k<N;k++){
			if(p.has(k)==1)
				count[k]++;
		}
	}
	for (i=0;i<N;i++){
		cout<<"Case #"<<i+1<<": "<<count[i]<<endl;
	}
	return 0;
}
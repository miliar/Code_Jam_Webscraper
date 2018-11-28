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

string intToStr(int k){
	ostringstream os;
	os << k;
	return os.str();
}

string longToStr(long k){
	ostringstream os;
	os << k;
	return os.str();
}

int strToInt(string s){
	istringstream is(s);
	int ri;
	is >> ri;
	return ri;
}

long strToLong(string s){
	istringstream is(s);
	long rl;
	is >> rl;
	return rl;
}

int main(){
	string ss;
	ifstream fin("B-large.in");
	ofstream fout("large.out");
	int T;
	int j,k;
	int min_max;
	int min_index;
	string rs = "";
	int digit;
	getline(fin,ss);
	T = strToInt(ss);
	for (int i=1;i<=T;i++){
		getline(fin,ss);
		istringstream is(ss);
		vector<int> D;
		for(j=0;j<ss.size();j++){
			D.push_back(ss.at(j)-'0');
		}
		bool hasBig = false;
		for(j=D.size()-2;j>=0;j--){
			int b = D[j];
			min_max = b;
			for(k=j+1;k<D.size();k++){
				int bb = D[k];
				if(hasBig==false && bb>b){
					hasBig = true;
					min_max = bb;
					min_index = k;
				}
				if(hasBig==true && bb>b && bb<min_max){
					min_max = bb;
					min_index = k;
				}

			}
			if(hasBig==true)
				break;
		}
		if(hasBig==true){
			int tmp = D[j];
			D[j] = min_max;
			D[min_index] = tmp;
			sort(D.begin()+j+1,D.end());
			rs = "";
			for(j=0;j<D.size();j++){
				rs += intToStr(D[j]);
			}
		}else{
			vector<int> newD;
			sort(D.begin(),D.end());
			for(j=0;j<D.size();j++){
				if(D[j]>0)
					break;
			}
			int tmp = D[0];
			D[0] = D[j];
			D[j] = tmp;
			sort(D.begin()+1,D.end());
			newD.push_back(D[0]);
			newD.push_back(0);
			for(j=1;j<D.size();j++){
				newD.push_back(D[j]);
			}
			rs = "";
			for(j=0;j<newD.size();j++){
				rs += intToStr(newD[j]);
			}
		}
		fout<<"Case #"<<i<<": "<<rs<<endl;
	}
	return 0;
	
}

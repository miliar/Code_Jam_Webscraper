#include <algorithm>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <iostream>
#include <map>
#include <sstream>
#include <string>
#include <fstream>
#include <vector>
using namespace std;
int T,P;
vector< pair<string,int> > moves;

int solve(){
	int posO = 1, posB = 1;
	int ret = 0;
	int avanzaO = 0, avanzaB = 0;
	for(int i = 0; i<moves.size(); i++){
		if(moves[i].first == "O"){
			int steps = abs(moves[i].second - posO);
			steps -= avanzaO;
			avanzaB += max(1,steps+1);
			avanzaO = 0; 
			ret += max(1, steps+1);
			posO = moves[i].second;
		}
		else if(moves[i].first == "B"){
			int steps = abs(moves[i].second - posB);
			steps -= avanzaB;
			avanzaO += max(1,steps+1);
			avanzaB = 0; 
			ret += max(1, steps+1);
			posB = moves[i].second;
		}
	}
	return ret;
}

int main(){
	ifstream in("Input.in");
	ofstream out("Output.out");
	in >> T;
	string C;
	for(int i = 0; i<T; i++){
		moves.clear();
		int N;
		in >> N;
		for(int j = 0; j<N; j++){
			in >> C >> P;
			moves.push_back(make_pair(C,P));
		}
		int ret = solve();
		out << "Case #" << i+1 << ": " << ret << endl;
	}
} 


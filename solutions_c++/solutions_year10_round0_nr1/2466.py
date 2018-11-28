#include <algorithm>
#include <iostream>
#include <sstream>
#include <string>
#include <vector>
#include <queue>
#include <set>
#include <map>
#include <cstdio>
#include <cstdlib>
#include <cctype>
#include <cmath>
#include <fstream>
using namespace std;
#define FOR(i,a,b) for(int i=a; i<b; i++)
int ipow(int a, int b) {return b?(b%2?a:1)*ipow(a*a,b/2):1;}

int main(){
	ifstream in("A-large-practice.in");
	ofstream out("A-large-practice.out");
	int T,N,K;
	in >> T;
	string ret;
	for(int t = 0; t<T; t++){
		in >> N >> K;
		if(K == 0){
			ret = "OFF";
		}
		else{
			int need = ipow(2,N)-1;
			K -= need;
			need++;
			if(K%need == 0) ret = "ON";
			else ret = "OFF";
		}
		out << "Case #" << t+1 << ": " << ret << endl;
	}
	
}
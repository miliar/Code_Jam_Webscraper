#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <sstream>
#include <iostream>
#include <vector>
#include <list>
#include <math.h>
#include <algorithm>

using namespace std;

long long val(string str){
	return atoi(str.c_str());
}

long long res;

bool allcomb(long long dec, string inp){
	string num=inp;
	long long min = 1000000000;
	long long tmp;
	
	while (next_permutation(num.begin(),num.end())){
		tmp = val(num);
		if (dec<tmp && tmp<min)
			min =tmp;
	}
	
	if (min<1000000000){
			res = min;
			return true;
	}
	return false;
}

int main(){
	//freopen("input.in", "r", stdin);
	//freopen("output.out", "w", stdout);
	long long T,N;
	cin >> T;
	for (long long i=0; i<T; i++){
		string inp;
		cin >> inp;
		long long num = val(inp);
		bool gotit=false;
		
		while (true){
			if (allcomb(num,inp))
				break;
			inp.insert(inp.begin(),'0');
		}
		
		//allcomb(inp);
		cout << "Case #"<<i+1<<": "<<res<<endl;
	}
}

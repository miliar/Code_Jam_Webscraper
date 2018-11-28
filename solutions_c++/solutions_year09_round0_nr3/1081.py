#include <cstdlib>
#include <iostream>
#include <fstream>
#include <map>
#include <string>
#include <vector>
#include <cstdio>
#include <cmath>
#include <algorithm>

using namespace std;

string str;
string wcj;

int cache[20][502];

int solve(int indexW, int indexS){
	int ret = 0;
	if(indexW == wcj.size()) return 1;
	if(indexS == str.size()) return 0;
	if(cache[indexW][indexS] > -1) return cache[indexW][indexS];
	if(str[indexS] == wcj[indexW]){
		ret += solve(indexW+1,indexS+1)%10000;
	}
	ret += solve(indexW,indexS+1)%10000;
	ret %= 10000;
	cache[indexW][indexS] = ret;
	return ret;
}

int main()
{
	ifstream in("C-small-attempt1.in");
	ofstream out("C-small-attempt1.out");
	int tests;
	wcj = "welcome to code jam";
	char c;
	in >> tests;
	for(int t = 0; t<tests; t++){
		memset(cache,-1,sizeof(cache));
		while(str.size()==0) 
			getline(in,str);
		cout << " caso " << t+1 << endl;
		int ret = solve(0,0);
		if(ret<10)
			out << "Case #" << t+1 << ": 000" << ret << endl;
		else if(ret<100)
			out << "Case #" << t+1 << ": 00" << ret << endl;
		else if(ret<1000)
			out << "Case #" << t+1 << ": 0" << ret << endl;
		else
			out << "Case #" << t+1 << ": " << ret << endl;
		str = "";
	}
    return EXIT_SUCCESS;
}


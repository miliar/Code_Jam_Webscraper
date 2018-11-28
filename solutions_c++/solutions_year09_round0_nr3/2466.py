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
#include <stdio.h>
#include <math.h>
using namespace std;


int main(){
	int n;	
	cin >> n;	
	getchar();
	for(int i = 0; i < n; i++){
		
		string welc = "welcome to code jam";
		int* found = new int [20];
		for(int j = 0; j < 19; j++)
			found[j] = 0;
		found[19] = 1;
		char * st = new char[500];
		gets(st);
		string s(st);
		for(int j = s.length() - 1; j >= 0; j--)
			for(int k = 0; k < 19; k++)
				if (s[j] == welc[k])
					found[k] += found[k + 1];
		int res = found[0] % 10000;
		if (res / 10 == 0)
			cout << "Case #" << i + 1 << ": 000" << found[0] << "\n";
		else
			if (res / 100 == 0)
				cout << "Case #" << i + 1 << ": 00" << found[0] << "\n";
			else
				if (res / 1000 == 0)
					cout << "Case #" << i + 1 << ": 0" << found[0] << "\n";
				else
					cout << "Case #" << i + 1 << ": " << found[0] << "\n";

	}
}
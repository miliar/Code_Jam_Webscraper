#include <algorithm>
#include <iomanip>
#include <iostream>
#include <string>
#include <vector>

#include <cmath>
#include <cstdio>
#include <cstdlib>

using namespace std;

typedef vector<int> vi;
typedef vector<double> vd;
typedef vector<string> vs;

typedef vector<vi> mati;
typedef vector<vd> matd;
typedef vector<vs> mats;

typedef long long int64;
typedef unsigned long long uint64;

string permutar(vi permut, string code)
{
	int i = 0;
	string result("");
	while(i < code.size()) {
		string codeP;
		codeP.resize(permut.size());
		for(int j = 0; j < permut.size(); ++j) {
			codeP[j] = code[permut[j]+i];
		}
		i += permut.size();
		result += codeP;
	}
	return result;
}


int compress(string code)
{
	char letter = '.';
	int answer = 0;
	for(int i = 0; i < code.size(); ++i) {
		if(letter != code[i]) {
			letter = code[i];
			++answer;
		}
	}
	return answer;
}

string code;
int max2;

void takePermut(int k, vi &perm, vector<bool> is)
{
	for(int i = 0; i < k; ++i) {
		if(!is[i]) {
			perm.push_back(i);
			is[i] = true;
			
			takePermut(k, perm, is);
			if(perm.size() == k) {
				string code2 = permutar(perm, code);
				/*
				cout << code << endl;
				for(int i = 0; i < perm.size(); ++i) {
					cout << perm[i] << " ";
				}
				cout << endl;
				cout << code2 << endl;
				*/
				int x = compress(code2);
				//cout << x << endl;
				if(x < max2) {
					max2 = x;
				}
			}
			perm.pop_back();
			is[i] = false;
		}
	}
}


int main()
{
	int cases;
	cin >> cases;
	for(int c = 0; c < cases; ++c) {

		int k;
		vi permut;
		permut.clear();

		cin >> k >> code;

		vector<bool> is;
		is.clear();
		for(int i = 0; i < k; ++i ) is.push_back(false);
		max2 = 99999999;
		takePermut(k, permut, is);
		
		cout << "Case #" << c+1 << ": " << max2 << endl;	
	}
	return 0;
}
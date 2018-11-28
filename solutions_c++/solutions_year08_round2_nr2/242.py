#include <iostream>
#include <string>
#include <vector>
#include <algorithm>

#include <cmath>
#include <cstdio>
#include <cstdlib>

using namespace std;

typedef long long int64;
typedef unsigned long long uint64;

typedef vector<int> vi;
typedef vector<double> vd;

#define PI 3.1415926535897932384626433832795

// Fatoração de primos
// Retorna um vetor com todos os fatores (inclusive repetidos)
vector<int> primeFac(int number)
{
	vector<int> factors;
	factors.clear();
	
	int n = number;

	for(int i = 2; i <= number;) {
		if(!(n%i)) {
			n /= i;
			factors.push_back(i);
		}
		else ++i;
	}
	/*
	cout << "Estou fatorando " << number << endl;
	for(int i = 0; i < factors.size(); ++i) cout << factors[i] << " ";
	cout << endl;
	*/
	return factors;
}

bool vecInter(vector<int> a, vector<int> b, int p)
{
	for(int i = 0; i < a.size(); ++i) {
		for(int j = 0; j < b.size(); ++j) {
			//cout << a[i] << " " << b[j] << " " << p << endl;
			if((a[i] == b[j])&&(a[i] >= p)) {
				//cout << "ok" << endl;
				return true;
			}
		}
	}
	return false;
}


int main()
{
	int cases;
	cin >> cases;
	for(int c = 0; c < cases; ++c) {
		int a, b, p;

		cin >> a >> b >> p;

		vector<vector<int> > facs;

		for(int i = a; i <= b; ++i) {
			vector<int> aux;
			aux = primeFac(i);
			facs.push_back(aux);
		}

		bool done = false;
		while(!done) {
			bool restart = false;
			for(int i = 0; (i < facs.size())&&(!restart); ++i) {
				for(int j = 0; (j < facs.size())&&(!restart); ++j) {
					if(i == j) continue;
					if(vecInter(facs[i], facs[j], p)) {
						/*
						cout << "i: " << a+i << endl;
						for(int x = 0; x < facs[i].size(); ++x) cout << facs[i][x] << " ";
						cout << endl;
						cout << "j: " << a+j << endl;
						for(int x = 0; x < facs[j].size(); ++x) cout << facs[j][x] << " ";
						cout << endl;
						*/
						restart = true;
						for(int k = 0; k < facs[j].size(); ++k) facs[i].push_back(facs[j][k]);
						//for(int x = 0; x < facs[i].size(); ++x) cout << facs[i][x] << " ";
						//cout << endl;
						facs.erase(facs.begin()+j);
					}
				}
			}
			if(!restart) done = true;
		}

		cout << "Case #" << c+1 << ": " << facs.size() << endl;	
	}
	return 0;
}






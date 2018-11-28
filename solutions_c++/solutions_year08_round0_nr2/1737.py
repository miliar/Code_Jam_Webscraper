//#include <stdio.h>
#include <iostream>
#include <stdlib.h>
#include <string>
#include <fstream>
#include <sstream>
#include <list>
#include <algorithm>


using namespace std;
using std::string;


ifstream fin("input.txt");
ofstream fout("output.txt");

#define FOR(a,b,c) for(int a=(b);a<(c);a++)


char line[100];

#define MAX_NA 100
#define MAX_NB 100

void solve(int round)
{
	string s;
/*	string ah1[MAX_NA];
	string am1[MAX_NA];
	string bh1[MAX_NB];
	string bm1[MAX_NB];
	
	string ah2[MAX_NA];
	string am2[MAX_NA];
	string bh2[MAX_NB];
	string bm2[MAX_NB];
	*/
	int ah1[MAX_NA];
	int am1[MAX_NA];
	int bh1[MAX_NB];
	int bm1[MAX_NB];
	
	int ah2[MAX_NA];
	int am2[MAX_NA];
	int bh2[MAX_NB];
	int bm2[MAX_NB];
	
	double a1[MAX_NA];
	double a2[MAX_NA];
	double b1[MAX_NB];
	double b2[MAX_NB];
	
	double T;
	int NA, NB;
	int i, j;
	
	char cc;
	
	//int qn[MAX_Q];
	
	fin >> T;
	fin >> NA;
	fin >> NB;
	getline(fin,s);	
	for(i = 0; i < NA; i++) {
		getline(fin, s);
		stringstream buffer(s);
		buffer >> ah1[i] >> cc >> am1[i] >> ah2[i] >> cc >> am2[i];
		a1[i] = (double)ah1[i] + (double)am1[i]/100;
		a2[i] = (double)ah2[i] + (double)am2[i]/100;
		//cout << am2[i] << endl;
	}
	
	for(i = 0; i < NB; i++) {
		getline(fin, s);
		stringstream buffer(s);
		buffer >> bh1[i] >> cc >> bm1[i] >> bh2[i] >> cc >> bm2[i];
		b1[i] = (double)bh1[i] + (double)bm1[i]/100;
		b2[i] = (double)bh2[i] + (double)bm2[i]/100;
		//cout << bm2[i] << endl;
	}
	
	sort(a1, a1+NA);
	sort(a2, a2+NA);
	sort(b1, b1+NB);
	sort(b2, b2+NB);
	
	int cnt_a2b = NA;
	int cnt_b2a = NB;
	
	bool flag;
	
	
	j = 0;
	for(i = 0; i < NA; i++) {
		flag = 0;
		while (j < NB) {
			if (a2[i]+T/100.0 <= b1[j]) {	// found one
				cnt_b2a--;
				flag = 1;
				j++;
				break;
			}
			j++;
		}
		if (flag == 0 || j >= NB) // no more
			break;
	}
	
	j = 0;
	for(i = 0; i < NB; i++) {
		while (j < NA) {
			if (b2[i]+T/100.0 <= a1[j]) {	// found one
				cnt_a2b--;
				flag = 1;
				j++;
				break;
			}
			j++;
		}
		if (flag == 0 || j >= NA) // no more
			break;
	}

	fout << "Case #" << round << ": " << cnt_a2b << " " << cnt_b2a << endl;
}

int main()
{
	int i;
	int N;
	int cnt;
	
	fin >> N;
	
	int T;
	int NA, NB;
	//int qn[MAX_Q];
	

	for(int i = 0; i < N; i++) {
		solve(i+1);
	}
	
	return 0;
}

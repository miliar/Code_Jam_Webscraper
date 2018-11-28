// CFProblems.cpp : Defines the entry point for the console application.
//

//#include "stdafx.h"

#include <cstdio>
#include <cstdlib>
#include <iostream>
#include <sstream>
#include <fstream>
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
#include <iomanip>
#include <cmath>

using namespace std;

typedef long long ll;
typedef long double ld;

typedef vector<int> vi;
typedef vector<vi> vvi;
typedef vector<string> vs;
typedef vector<ll> vl;
typedef pair<int,int> ii;

#define fr(i, a, b) for(i = (a); i < (b); ++i)
#define rfr(i, a, b) for(i = (a) - 1; i >= (b); --i)
#define sz(a) int((a).size())
#define clr(a, b) memset(a, b, sizeof(a))

#define pb push_back
#define mp make_pair

#define all(c) (c).begin(),(c).end()

#define tr(c,i) for(typeof((c).begin() i = (c).begin(); i != (c).end(); i++)

#define present(c,x) ((c).find(x) != (c).end())
#define cpresent(c,x) (find(all(c),x) != (c).end())

string Combine(string strC, string strAns) {
	if ( sz(strC) == 0 || sz(strAns) < 2 ) return strAns;

	int n, s;
	char c1, c2;

	n = sz(strC);
	s = sz(strAns);
	c1 = strAns[s-2];
	c2 = strAns[s-1];

	size_t fchar1, fchar2;
	fchar1 = strC.find(c1);
	fchar2 = strC.find(c2);

	if ( (fchar1 != string::npos && fchar2 != string::npos) && (c1 == c2) ) {
		fchar2 = strC.find(c2, fchar2 + 1);
	}

	if ( fchar1 != string::npos && fchar2 != string::npos ) {
		if ( strC[fchar1 + 1]  == '|' || strC[fchar2 + 1]  == '|' ) return strAns;
		
		if ( max(fchar1, fchar2) - min(fchar1, fchar2) == 1 ) {
			char comb = strC[ max(fchar1, fchar2) + 1 ];
			strAns.replace(s-2, 2, 1, comb);
		}
	}
	return strAns;
}

string Opposed(string strD, string strAns) {
	if ( sz(strD) == 0 || sz(strAns) < 2) return strAns;

	int s = sz(strAns);
	char c = strAns[s-1];

	size_t fchar = strD.find(c);
	char opp;
	
	if ( fchar != string::npos ) {
		if ( strD[fchar+1] == '|' ) 
			opp = strD[fchar-1];
		else
			opp = strD[fchar+1];

		if ( strAns.find(opp) != string::npos )
			strAns.clear();
	}
	
	return strAns;
}

int main()
{
	int N, T, C, D, i, j, k, x, o, n;
		
	string strC, strD, strAns, s;
	
	ifstream fin("B-small.in");
	ofstream fout("B-small.out");

	fin >> T;	
	fr ( i, 0, T ) {
		
		fin >> C;
		fr ( j, 0, C ) {
			fin >> s;
			strC.append(s);
			strC.append("|");
		}

		fin >> D;
		fr ( k, 0, D ) {
			fin >> s;
			strD.append(s);
			strD.append("|");
		}

		fin >> N >> s;
		fr ( x, 0, N ) {
			strAns.append(s, x, 1);
			if ( x > 0 ) {
				strAns = Combine(strC, strAns);
				strAns = Opposed(strD, strAns);
			}
		}
		
		fout << "Case #" << i+1 << ": [";
		n = sz(strAns);
		fr (o, 0, n ) {
			if ( o == n - 1 )
				fout << strAns[o];
			else
				fout << strAns[o] << ", ";
		}

		fout << "]" << endl;
		strC.clear(); strD.clear(); strAns.clear(); s.clear();
	}
}
#include <cstdio>
#include <iostream>
#include <algorithm>
#include <vector>
#include <set>
#include <map>
#include <string>
#include <cmath>
#include <cstdlib>
#include <cstring>

#include<stdio.h>
#include<ctype.h>
#include<math.h>
#include<string.h>
#include<stdlib.h>

using namespace std;

#define X first
#define Y second
#define MP make_pair
#define PB push_back
#define SZ size

int main () {
	int pocet, i, min, mensie, N, minA, minB, akt, ii, vys;
	cin >> pocet;
	for (i = 0; i < pocet; i++) {
		cin >> N;
		cin >> mensie;
		cin >> min;
		vys = 0;
		if (min >= 2) {
			minA = min * 3 - 2;
			minB = min * 3 - 4;
		} else if (min == 1) {
			minA = 1;
			minB = 1;
		} else {
			minA = 0;
			minB = 0;
		}
		for (ii = 0; ii < N; ii++) {
			cin >> akt;
			if (akt >= minA)
				vys++;
			else if (akt >= minB && mensie > 0) {
				vys++;
				mensie--;
			}
		}
		cout << "Case #" << i + 1 << ": " << vys << endl;
	}
	return 0;
}
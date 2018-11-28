// B-small.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <iostream>

using namespace std;

int n, a[100], b[100], res;

void rec (int x){
	if (x < n){
		int i;
		for (i=0; i<2; i++){
			b[x] = i;
			rec (x+1);
		}
	} else {
		int sum1 = 0, sum2 = 0;
		int i;
		for (i=0; i<n; i++)
			if (b[i] == 0) sum1 = sum1 ^ a[i]; else
				sum2 = sum2 ^ a[i];
		if (sum1 == sum2){
			sum1 = 0; sum2 = 0;
			for (i=0; i<n; i++)
				if (b[i] == 0) sum1 += a[i]; else
					 sum2 += a[i];
			if (sum1 > res && sum2) res = sum1;
			if (sum2 > res && sum1) res = sum2;
		}
	}
}

int main(){
	freopen ("input.txt", "r", stdin);
	freopen ("output.txt","w", stdout);
	int nn, ii;
	cin >> nn;
	for (ii=0; ii<nn; ii++){
		cin >> n;
		int i;
		res = -1;
		for (i=0; i<n; i++) cin >> a[i];
		memset (b, 0, sizeof(b));
		rec(0);
		cout << "Case #" << ii + 1 << ": ";
		if (res == -1) cout << "NO" << endl; else
			cout << res << endl;
	}
}
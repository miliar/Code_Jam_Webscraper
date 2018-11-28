#include <cstdio>
#include <iostream>
#include <sstream>
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

#define fi first
#define se second
#define MP make_pair
#define PB push_back
#define SZ size
#define SIZE(x) (int)(x).size()

#define MAX 105

int N, S, P;

int is_high(int x) {
	bool surp = false;
	for (int a = 0; a <= 10; a++) 
		for (int b = 0; b <= 10; b++)
			for (int c = 0; c <= 10; c++) {
				if (a+b+c == x) {
					if (abs(a-b) <= 1 && abs(b-c) <= 1 && abs(a-c) <= 1) {
						if (a >= P || b >= P || c >= P)
							return 1;
					} else if (abs(a-b) <= 2 && abs(b-c) <= 2 && abs(a-c) <= 2) {
						if (a >= P || b >= P || c >= P)
							surp = true;
					}
				}
			}
	
	if (surp && S > 0) {
		S--;
		return 1;
	} else return 0;
}


int main() {
	int T;
	scanf("%d", &T);
	cin.get();
	
	for (int q = 1; q <= T; q++) {
		scanf("%d %d %d", &N, &S, &P);
		
		int num = 0;
		for (int i = 0; i < N; i++) {
			int a;
			scanf("%d", &a);
			num += is_high(a);
		}	
		
		printf("Case #%d: %d\n", q, num);
	}	
	return 0;
}
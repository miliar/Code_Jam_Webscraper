#include <fstream>
#include <cstdio>
#include <iostream>
#include <cassert>
#include <bitset>

using namespace std;

ifstream fin("C-small-attempt0.in");
ofstream fout("C-small-attempt0.out");

#define MAX 10000

int solve(int A, int B) {
	int dp[MAX];
	for (int i=0; i<MAX; i++) dp[i] = 0;

	for (int i=10; i<MAX; i++) {
		int lastdigit = i%10;
		int remaining = i/10;
		int nBigger = 0;
		while (remaining>0) {
			int last = remaining%10;
			remaining /= 10;
			if (lastdigit>last) nBigger++;
		}
		remaining = i/10;
		dp[i] = (nBigger+1)*(dp[remaining]+1) -1;
		//cout << i << " " << dp[i] << endl;
	}
	int count = 0;
	for (int i=A;i<=B; i++)
		count += dp[i];
	return count;
}

int chop(int i, int pos) {

	int firstHalf = i;
	int secondHalf = 0;
	int k = 1;
	for(int j = 1; j<=pos; j++) {
		int digit = firstHalf%10;
		secondHalf += digit*k;
		k*=10;
		firstHalf /= 10;
	}

	k=1;
	int n = firstHalf;
	while (n != 0) {
		k *= 10;
		n /= 10;
	}
	
	int newnumber = secondHalf*k + firstHalf;
	return newnumber;
}

int countRecycle(int i, int A, int B) {
	int ndigits = 0;
	int n = i;
	while (i>0) {
		ndigits++;
		i /= 10;
	}

	int count = 0;
	bitset<MAX> seen;
	for (int pos=1; pos<=ndigits; pos++) {
		int newi = chop(n,pos);
		if (newi>=A && newi<=B && newi>n) {
			if (!seen[newi]) {
				//cerr << "newi = " << newi << endl;
				count++;
				seen[newi] = 1;
			}
		}
	}
	return count;
}

int solve1(int A, int B) {
	int count = 0;
	for (int i=A;i<=B; i++) {
		int c = countRecycle(i,A,B);
		//if(c) cerr << "i = "<<i << endl;
		count += c;
	}
	return count;
}

int main() {

	assert(chop(10,1)==1);
	assert(chop(123,1) == 312);
	assert(chop(123,2) == 231);
	assert(countRecycle(123,100,300)==1);
	//cerr << endl;
	assert(solve1(1111,2222)==287);

	int T;
	fin >> T;
	for (int test=1;test<=T;test++) {
		int A, B;
		fin >> A >> B;

		fout << "Case #" << test << ": " << solve1(A,B) << endl;
	}
}



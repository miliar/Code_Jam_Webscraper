#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <iterator>
#include <list>
#include <map>
#include <set>
#include<stdio.h>
#include<stdlib.h>
#include<math.h>
using namespace std;
#define REP(i,a,b) for(i=a;i<b;++i)
#define rep(i,n) REP(i,0,n)

#define MAXP (10000)
#define MAXQ (100)
int nTestCase, testCase;
int i, j, k, l;
unsigned long long int ans, tmpAns;
int arrP[MAXP+2];
vector<int> arrQ;
int P, Q, p, q;
unsigned long long int fact;
char str[64], symb[64];
int symbVal[64], strNum[64];
int nSymb;

bool symbAlreadyFound(char c, int nbase, int &retIndex){
	REP(retIndex,0,nbase){
		if(c == symb[retIndex]){
			return true;
		}
	}
	return false;
}

int main(){
	cin >> nTestCase;
	//getline(cin, str);
	for(testCase=0; testCase<nTestCase; ++testCase){
		scanf("%s", str);
		nSymb = 0;
		l = strlen(str);
		REP(i,0,l){
			if(symbAlreadyFound(str[i], nSymb, j)){
				strNum[i] = j;
			}else{
				symb[nSymb] = str[i];
				strNum[i] = nSymb;
				++nSymb;
			}
		}
		REP(i,0,l){
			if(strNum[i] == 0)
				strNum[i] = 1;
			else if(strNum[i] == 1)
				strNum[i] = 0;
		}

		ans = 0;
		fact = 1;
		if(nSymb == 1)
			nSymb = 2;
		for(i=l-1; i>=0; --i){
			ans += fact*strNum[i];
			fact *= nSymb;
		}
		cout << "Case #" << testCase+1 << ": " << ans << endl;
	}

	return 0;
}

#include <cstring>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <cctype>
#include <cstdio>
#include <cstdlib>
#include <deque>
#include <map>
#include <queue>
#include <stack>
#include <vector>
#include <set>
#include <list>
#include <bitset>
#include <complex>
#include <list>
#include <sstream>
#include <iomanip>
#include <algorithm>
#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <functional>
#include <numeric>
#include <utility>
#include <iostream>
#include <fstream>
#include <string>

using namespace std;

#define all(v) v.begin(),v.end()
#define rall(v) v.rbegin(),v.rend()
#define pb push_back
#define SIZE(x) ((int)(x.size()))
#define LENGTH(x) ((int)(x.length()))
#define PI 3.14159265358979323846264338327950288

typedef long long ll;
typedef unsigned long long ull;
int TS,N,L,H;
int phone[110];
/*
 if the frequency of any one of them divides the frequency of the other 
 (that's a pretty restrictive idea of harmony, but the Atlanteans are known to be 
 very conservative in music). 
 
 The first line of the input gives the number of test cases, T. 
 T test cases follow. Each test case is described by two lines.
 The first contains three numbers: N, L and H, denoting the number of other players, 
 the lowest and the highest note Jeff's instrument can play. The second line contains 
 N integers denoting the frequencies of notes played by the other players. 
 */

inline bool Ham(int i,int j){
	return i%j==0 || j%i==0;
}

int main(){
	cin>>TS;
	for (int testId=1; testId<=TS; ++testId) {
		cin>>N>>L>>H;
		for (int i=0; i<N; ++i) {
			cin>>phone[i];
		}
		bool can=false;
		int res;
		for (int note=L; note<=H; ++note) {
			bool suc=true;
			for (int i=0; i<N; ++i) {
				if ( !Ham(phone[i],note) ){suc=false;break;}
			}
			if (suc) {
				can=true;
				res=note;
				break;
			}
		}
		cout << "Case #"<<testId<<": ";
		if (!can)cout<<"NO"<<endl;
		else cout<<res<<endl;
	}
	return 0;
}

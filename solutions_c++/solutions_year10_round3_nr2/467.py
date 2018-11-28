#include <iostream>
#include <fstream>
#include <sstream>
#include <string>
#include <time.h>
#include <vector>
#include <time.h>
#include <cmath>
#include <algorithm>
#include <set>
#include <map>
#include <cstdio>
#include <cstdlib>
#include <stdio.h>
#define all(c) c.begin(), c.end() 
#define PI 3.141592653
#define PAUSE system("pause")
#define FOR(i,j) for(int i=0;i<j;i++)
#define VI vector<int> 
#define VS vector<string>
#define MAX(i,j) i>j? i:j
#define SZ(i) i.size()
using namespace std;

ifstream input("C:/Users/Yeqi SUN/Desktop/B-large.in");
ofstream output("C:/Users/Yeqi SUN/Desktop/test.out");


typedef pair<int, int> P;
void main(){
	long long N,M,T,L,P, C, x, y;
	
	string ss,temp;
	
	input >> T;
	FOR(i, T){
		input >> L >> P >> C;
		long long count;
		long long power = 0;
		long long cur = L;
		while( cur < P ){
			cur *= C;
			power++;
		}
		vector<long long> cnt(100,0);
		cnt[1] = 0;
		cnt[2] = 1;
		cnt[3] = 2;

		for(int k = 4;k<100;k++){
			cnt[k] = cnt[k-k/2]+1;
			if(k >= power)
				break;

		}
		count = cnt[power];
		output << "Case #" << i + 1 << ": " <<  count << endl;
	}






	PAUSE;
}
/*
 * CandySplitting_sort.cpp
 *
 *  Created on: May 7, 2011
 *      Author: batchunag
 */

#include <iostream>
#include <fstream>
#include <algorithm>
#include <vector>
#include <map>
#include <utility>
#include <stdio.h>
#include <string.h>
#include <list>
#define MAXINT 10000000
#define FOR(i,a,b) for (int i=a; i<b; i++)
#define REP(i,n) for(int i=0;i<(int)n;++i)

using namespace std;

int main(){
	FILE *out=fopen("answer.txt","w");
	ifstream in ("input.txt");
	int T,N;
	in>>T;
	REP(t,T){
		in>>N;
		int ans=0;
		int sum=0;
		int min=MAXINT;
		REP(i,N){
			int x;
			in>>x;
			ans^=x;
			if (x<min) min=x;
			sum+=x;
		}
		if (ans==0) fprintf(out,"Case #%d: %d\n",t+1,sum-min);
		else fprintf(out,"Case #%d: NO\n",t+1);
	}
	return 0;
}

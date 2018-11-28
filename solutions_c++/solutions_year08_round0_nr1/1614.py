#include <vector>
#include <list>
#include <string>
#include <cstdio>
#include <stdlib.h>
#include <iostream>
#include <sstream>
#include <map>
#include <cmath>
#include <algorithm>
using namespace std;


	int mm[1001][100];

#include "stdio.h"
int main(int argc, char* argv[])
{
	char buf[200];
	int N;
	gets(buf); sscanf(buf,"%d",&N);
	//cin >> N;
	for (int ca=0; ca<N; ca++) {
		int S;
		gets(buf); sscanf(buf,"%d",&S);
		//int S; cin>>S;
		vector<string> names;
		for(int i=0;i<S;i++) {
			gets(buf);
			names.push_back(string(buf));
			//printf("->%s\n",names[i].c_str()); //cout<<"*"<<names[i]<<endl;
		}
		
		int Q; cin>>Q; gets(buf);
		if (Q<=1) {
			cout<<"Case #"<<ca+1<<": "<<0<<endl;
			continue;
		}
		vector<string> seq;
		for(int i=0;i<Q;i++) { 
			cin.getline(buf,200); 
			seq.push_back(string(buf));
		}
		for(int i=0;i<S;i++) mm[0][i]=names[i]==seq[0] ? 123456 : 0;

		for(int q=1; q<Q; q++) {
//cout<<"In: "<<seq[q]<<endl;
			for(int last=0;last<S;last++) {
				if (names[last]==seq[q]) {
					mm[q][last] = 123456;
				} else {
					int best = 123456;
					for(int prev=0;prev<S;prev++) {
						best=min(best, mm[q-1][prev]+(last==prev ? 0 : 1));
					}
					mm[q][last] = best;			
				}
//cout<<"mm["<<q<<"]["<<names[last]<<"]="<<mm[q][last]<<endl;
			}
		}
		int best=123456;
		for(int i=0;i<S;i++) best=min(best,mm[Q-1][i]);
		cout<<"Case #"<<ca+1<<": "<<best<<endl;
	}
	return 0;
}
// END CUT HERE 

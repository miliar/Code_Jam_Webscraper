#include <map>
#include <iostream>
#include <string>
#include <vector>
#include <fstream>
#include <cstdio>
using namespace std;
int N, NA, NB, T;

bool query(const vector<pair<int, int> > &A, const vector<pair<int, int> > &B, int na, int nb) {
	int trains[1441][2];
	memset(trains, 0, sizeof trains);
	trains[0][0]=na;
	trains[0][1]=nb;
	for(int t=0;t<24*60; t++) {
		//is there a destination at this time
		for(int i=0;i<A.size();i++) {
			if(A[i].first==t) {
				trains[t][0]--;
				trains[A[i].second+T][1]++;
			}
		}
		for(int i=0;i<B.size();i++) {
			if(B[i].first==t) {
				trains[t][1]--;
				trains[B[i].second+T][0]++;
			}
		}
		trains[t+1][0]+=trains[t][0];
		trains[t+1][1]+=trains[t][1];
	}
	for(int t=0;t<24*60; t++)
		for(int i=0;i<2;i++) 
			if(trains[t][i]<0) return false;
	return true;
}
int main() {
	FILE *input, *output;
	input=fopen("B-small.in", "r");
	output=fopen("train_output.txt", "w");
	fscanf(input, "%d", &N);
	for(int test=0;test<N;test++) {
		fscanf(input, "%d", &T);
		fscanf(input, "%d%d", &NA, &NB);
		int dhour, dmin, ahour, amin;
		vector<pair<int, int> > A, B;
		for(int i=0;i<NA;i++) {			
			fscanf(input, "%d:%d %d:%d", &dhour, &dmin, &ahour, &amin);
			A.push_back(make_pair(dhour*60+dmin, ahour*60+amin));
		}
		for(int i=0;i<NB;i++) {			
			fscanf(input, "%d:%d %d:%d", &dhour, &dmin, &ahour, &amin);
			B.push_back(make_pair(dhour*60+dmin, ahour*60+amin));
		}
	
		for(int na=0;na<200;na++) {
			for(int nb=0;nb<200;nb++) {
				if(query(A, B, na, nb)) {
					printf("Case #%d: %d %d\n", test+1, na, nb);
					fprintf(output, "Case #%d: %d %d\n", test+1, na, nb);
					goto end;
				}
			}
		}
		end: int x=5;
	}
}
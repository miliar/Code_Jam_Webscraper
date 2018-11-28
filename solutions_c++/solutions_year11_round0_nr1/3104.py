#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <cstring>

#include <algorithm>
#include <vector>
#include <string>
#include <sstream>
#include <iostream>
#include <map>
#include <set>

using namespace std;

#define forn(i, n) for (int i = 0; i < (int)(n); i++)
#define forit(i, a) for (__typeof((a).begin()) i = (a).begin(); i != (a).end(); i++)
#define sz(a) (int)(a).size()
#define all(a) (a).begin(), (a).end()
#define zero(a) memset(a, 0, sizeof(a))
#define pb push_back
#define mp make_pair

int main(){

	FILE* input = fopen("input.txt", "r");
	FILE* output = fopen("output.txt", "w");
	
	int nTestCases = 0;
	fscanf(input,"%d", &nTestCases);

	for(int tt=0; tt<nTestCases; tt++){
		
		int N = 0;
		fscanf(input, "%d ", &N);
		
		int lastPos[1000];
		lastPos['O'] = lastPos['B'] = 1;

		char lastColor = 'O';

		int pathSum = 0;
		int ret = 0;
		for(int i=0; i<N; i++){
			
			char color;
			int position;
			fscanf(input, "%c %d ", &color, &position);
			
			int val = 0;
			if(color == lastColor){ 
				val = max(0,abs(position - lastPos[color])) + 1;
				pathSum += val;
			}
			else{
				val = max(0,abs(position - lastPos[color]) - pathSum) + 1;
				pathSum = val;
			}
			lastPos[color] = position;
			lastColor = color;
			ret += max(0,val);
		}

		fprintf(output, "Case #%d: %d\n", tt+1, ret);

	}
}
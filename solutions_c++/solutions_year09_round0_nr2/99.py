#include<algorithm>
#include<iostream>
#include<string>
#include<vector>
#include<cstdio>
#include<cstdlib>
#include<sstream>
#include<cmath>
#include<fstream>
#include<map>

#define MAX(x, y) ((x) > (y) ? (x) : (y))
#define MIN(x, y) ((x) < (y) ? (x) : (y))

using namespace std;

int alt[10000];
int to[10000];
char label[10000];

int H, W, N;

int find(int i){


	if(to[i] != -1)
		return to[i];

	int myAlt = alt[i];

	int diff = 0;

	if(i >= W && myAlt > alt[i - W]){
		myAlt = alt[i - W];
		diff = -W;
	}
	if(i % W && myAlt > alt[i - 1]){
		myAlt = alt[i - 1];
		diff = -1;
	}
	if((i + 1) % W && myAlt > alt[i + 1]){
		myAlt = alt[i + 1];
		diff = 1;
	}
	if(i + W < N && myAlt > alt[i + W]){
		myAlt = alt[i + W];
		diff = W;
	}

	if(!diff){
		to[i] = i;
	}
	else
		to[i] = find(i + diff);
	
	return to[i];
}

void process(){

	int i, count = 0;

	memset(to, -1, sizeof(to));

	for(i = 0; i < N; i++){
		find(i);
	}



	memset(label, -1, sizeof(label));

	for(i = 0; i < N; i++){
		if(label[to[i]] < 0){
			label[to[i]] = count++;
		}
		label[i] = label[to[i]];
	}
}
int main()
{
	int T, caseIdx, i;
	
	cin >> T;


	for(caseIdx = 1; caseIdx <= T; caseIdx++){

		cin >> H >> W;
		N = H * W;


		for(i = 0; i < N; i++)
			cin >> alt[i];

		process();

		printf("Case #%d:\n", caseIdx);
		for(i = 0; i < N; ){

			printf("%c", char('a' + label[i++]));

			if(i % W)
				printf(" ");
			else
				printf("\n");
		}

	}
	return 0;
}

/*
 * vim: ts=2 sw=2
 * Local variables:
 * tab-width: 2
 * End:
 */

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
#define ABS(x) ((x) > 0 ? (x) : -(x))

#define SWAP(x, y) {(x) += (y); (y) = (x) - (y); (x) -= (y);}

#define INIT 0
#define FOUND 1


using namespace std;

int dic[5001][16];
int L, D, N;

int cur[500];

int valid[26][16];

int process(string line){

	memset(valid, 0, sizeof(valid));

	int n = line.size();

	int i, j, state;

	for(i = 0, j = 0, state = INIT;
			i < L && j < n;
			j++){

		if(line[j] == ')'){
			i++;
			state = INIT;
			continue;
		}

		else if(line[j] == '('){
			state = FOUND;
		}

		else{
			valid[line[j] - 'a'][i] = 1;
			if(state == INIT)
				i++;
		}
	}

	int ret = 0;
	for(i = 0; i < D; i++){

		for(j = 0; j < L; j++)
			if(!valid[dic[i][j]][j])
				break;

		if(j == L)
			ret++;
	}

	return ret;
}
int main()
{
	
	int i, j;

	string line;

	cin >> L >> D >> N;
	getline(cin, line);

	for(i = 0; i < D; i++){

		getline(cin, line);

		for(j = 0; j < L; j++)
			dic[i][j] = line[j] - 'a';
	}

	for(i = 0; i < N; i++){
		getline(cin, line);

		printf("Case #%d: %d\n", i + 1, process(line));
	}


	return 0;
}

/*
 * vim: ts=2 sw=2
 * Local variables:
 * tab-width: 2
 * End:
 */

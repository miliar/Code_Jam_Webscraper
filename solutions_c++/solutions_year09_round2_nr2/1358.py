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


using namespace std;

int T, caseidx, len;
int digit[21];

int compare (const void * a, const void * b)
{
	  return ( *(int*)a - *(int*)b );
}

void process(){

	int i, j, s, min = 11;

	for(i = len - 1; i; i--){
		if(digit[i] > digit[i - 1])
			break;
	}

	if(i){
		for(j = i; j < len; j++){
			if(digit[j] > digit[i - 1] && digit[j] < min){
				s = j;
				min = digit[j];
			}
		}

		SWAP(digit[s], digit[i - 1]);
		qsort(digit + i, len - i, sizeof(digit[0]), compare);
	}

	else{

		for(i = len; i; i--){
			digit[i] = digit[i - 1];
			if(min >= 11 && digit[i])
			{
				s = i;
				min = digit[i];
			}
		}
		digit[0] = 0;
		SWAP(digit[0], digit[s]);
		qsort(digit + 1, len, sizeof(digit[0]), compare);
		len++;

	}
	
}
int main()
{
	string line;
	getline(cin, line);
	stringstream ss(line);
	ss >> T;

	int i;

	for(caseidx = 1; caseidx <= T; caseidx++){

		getline(cin, line);
		len = line.size();

		for(i = 0; i < len; i++)
			digit[i] = line[i] - '0';

		process();


		printf("Case #%d: ", caseidx);
		for(i = 0; i < len; i++)
			printf("%d", digit[i]);
		printf("\n");
	}
	return 0;
}

/*
 * vim: ts=2 sw=2
 * Local variables:
 * tab-width: 2
 * End:
 */

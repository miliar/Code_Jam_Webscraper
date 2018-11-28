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
#include<set>

#define MAX(x, y) ((x) > (y) ? (x) : (y))
#define MIN(x, y) ((x) < (y) ? (x) : (y))
#define ABS(x) ((x) > 0 ? (x) : -(x))

#define SWAP(x, y) {(x) += (y); (y) = (x) - (y); (x) -= (y);}

using namespace std;

int ncase, idx;

long A[2], B[2];

map<pair<long, long>, int> MAP;

int get(long a, long b){

	//printf("getting %ld %ld:\n", a, b);
	if(a > b){
		SWAP(a, b);
	}
	//printf("getting %ld %ld:\n", a, b);
	//a <= b

	map<pair<long, long>, int>::iterator itr;

	pair<long, long> P(a, b);

	itr = MAP.find(P);
	if(itr != MAP.end())	return MAP[P];

	int ret = 0;

	if(a == b){
		ret = 0;
	}
	else if(!(b % a)){
		ret = 1;
	}
	else{
		do{
			b -= a;
			if(b <= 0)	break;

			if(get(a, b) == 0){
				ret = 1;
				break;
			}
		}while(b);
	}

	MAP[P] = ret;
	return ret;

}

int main()
{
	
	MAP.clear();

	cin >> ncase;

	for(idx = 1; idx <= ncase; idx++){

		cin >> A[0] >> A[1] >> B[0] >> B[1];

		long ret = 0;

		for(long a = A[0]; a <= A[1]; a++){
			for(long b = B[0]; b <= B[1]; b++){
				if(get(a, b))	ret++;
			}
		}

		cout << "Case #" << idx << ": " << ret << endl;


	}

	return 0;
}

/*
 * vim: ts=2 sw=2
 * Local variables:
 * tab-width: 2
 * End:
 */

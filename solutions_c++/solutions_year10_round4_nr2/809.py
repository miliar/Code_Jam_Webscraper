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

int P, M[1024], nnode, ret;

string line;

void compute(int frst, int last){

	int i;
	for(i = frst; i <= last; i++){
		if(M[i] > 0)	break;
	}

	if(i <= last){

		ret++;

		for(int j = frst; j <= last; j++){
			M[j]--;
		}

		compute(frst, (frst + last - 1) >> 1);
		compute((frst + last + 1) >> 1, last);

	}


}
int main()
{
	
	int ncase, cidx;

	scanf("%d", &ncase);

	for(cidx = 1; cidx <= ncase; cidx++){

		scanf("%d", &P);
		nnode = 1 << P;

		for(int i = 0; i < nnode; i++){
			scanf("%d", &M[i]);
			M[i] = P - M[i];
		}

		getline(cin, line);
		for(int i = 0; i < P; i++){
			getline(cin, line);
		}
		
		ret = 0;
		compute(0, nnode - 1);

		printf("Case #%d: %d\n", cidx, ret);
	}
	return 0;
}

/*
 * vim: ts=2 sw=2
 * Local variables:
 * tab-width: 2
 * End:
 */

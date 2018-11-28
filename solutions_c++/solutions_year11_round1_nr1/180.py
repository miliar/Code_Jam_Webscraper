#include<sys/types.h>
#include<dirent.h>

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

#define EPS 1e-6
#define PI 3.14159265358979323846

using namespace std;

long long N, pd, pg;

string ans[] = {"Broken", "Possible"};

int main()
{

	int ncase;
	scanf("%d", &ncase);

	for(int caseidx = 1; caseidx <= ncase; caseidx++){

		scanf("%lld %lld %lld", &N, &pd, &pg);

		int ret = 0;
		if(pg == 100 && pd - 100)	goto done;
		if(!pg && pd)	goto done;

		long long s = pd;
		for(long long n = 1; !ret && n <= N; n++, s += pd){
			if(!(s % 100))	ret = 1;
		}

done:
		printf("Case #%d: %s\n", caseidx, ans[ret].c_str());

	}
	
	return 0;
}

// vi: ts=2 sw=2

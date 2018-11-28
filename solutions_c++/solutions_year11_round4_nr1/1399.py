
#include <boost/math/common_factor.hpp>
#include "cstdio"
#include "iostream"
#include "cstring"
#include "cmath"
#include "vector"
#include "map"
#include "string"
#include <algorithm>

using namespace std;


struct lepcso {
	int b;
	int e;
	int w;
};

bool myfunction (lepcso i,lepcso j) { return (i.w<j.w); }

bool myf2 (lepcso i,lepcso j) { return (i.b<j.b); }


int algo() {
	int tn = 1;
	scanf("%d", &tn);

	for (int ti = 0; ti < tn; ti++) {

		double rv = 0;

		int X, S, R, t, N;
		scanf("%d %d %d %d %d", &X, &S, &R, &t, &N);

		vector<lepcso> v;

		{
			lepcso x;
			x.b=0;x.e=0;x.w=0;
			v.push_back(x);
		}
		for (int i = 0; i < N; i++) {
			lepcso x;
  		scanf("%d %d %d", &(x.b), &(x.e) ,&(x.w));
			v.push_back(x);
		}
		{
			lepcso x;
			x.b=X;x.e=X;x.w=0;
			v.push_back(x);
		}

		sort(v.begin(), v.end(), myf2);
		
		vector<lepcso> v2;
		v2.push_back(v[0]);
		for (int i = 0; i < N+1; i++) {
			if (v[i].e != v[i+1].b) {
				lepcso x;
				x.b = v[i].e;
				x.e = v[i+1].b;
				x.w = 0;
			  v2.push_back(x);
			}
			v2.push_back(v[i+1]);
		}

		sort(v2.begin(), v2.end(), myfunction);

		double runleft = (double) t;
		for (int i = 0; i < v2.size(); i++) {
			lepcso c = v2[i];
			//rintf("  %d %d %d ", c.b, c.e, c.w);

			double len = v2[i].e;
			len -= v2[i].b;

			//run
			double runw = R;
			runw += v2[i].w;
			double runtime = len / runw;
			if (runtime > runleft) {
				rv += runleft;
				len -= runleft * runw;
				runleft = 0;
			} else {
				runleft -= runtime;
				rv += runtime;
				len = 0;
				//continue;
			}

			//walk
			double walkw = S;
			walkw += v2[i].w;
			rv += len / walkw;
			//printf("lenw:%f runtime:%f runleft:%f %f\n", len, runtime, runleft, rv);
		}
		
		

		printf("Case #%d: %.8f\n", ti+1, rv);
		
	}
        
       

	return 0;
}








//STANDARD COMMON CODE BELOW

int main(int argc, char *argv[]) {
	char str[80];
	strcpy(str, argv[1]);
	strcat(str, ".in");
  freopen(str, "r", stdin);
	strcpy(str, argv[1]);
	strcat(str, ".out");
	freopen(str, "w", stdout);

	int rv = algo();

	fclose(stdout);

	return rv;
}






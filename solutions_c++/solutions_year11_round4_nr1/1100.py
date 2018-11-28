#include <algorithm>
#include <string>
#include <set>
#include <map>
#include <vector>
#include <queue>
#include <iostream>
#include <cmath>
#include <cstdio>
#include <cstdlib>

#define MP make_pair
#define ST first
#define ND second
#define PB push_back
#define LL long long
#define VII vector<int>
#define PII pair<int, int>

#define MAX 1000005

using namespace std;

int t, X, S, R, T, n;

double tim[MAX];

int main(){
    scanf("%d", &t);
    for(int testcase = 1; testcase <= t; testcase++){
	double res = 0.0;
	scanf("%d %d %d %d %d", &X, &S, &R, &T, &n);
	R -= S;
	
	for(int i = 0; i < X; i++) tim[i] = 1.0 / S;

	int ain, bin, win;
	for(int i = 0; i < n; i++){
	    scanf("%d %d %d", &ain, &bin, &win);
	    for(int j = ain; j < bin; j++) tim[j] = 1.0 / (S + win);
	}

	for(int i = 0; i < X; i++){
	  res += tim[i];
	}
	
	sort(tim, tim + X);
	
	double left = 1.0 * T;
	double gain;
	int pos = X-1;
	while(left > 0.0 && pos >= 0){
	    gain = tim[pos] - 1.0/(1.0 * R + (1.0 / tim[pos]));
//printf("%lf %lf %lf %lf\n", res, gain, tim[pos], left);
	    if(tim[pos]-gain < left){
		res -= gain;
		left -= tim[pos]-gain;
		pos--;
	    }
	    else{
		res -= tim[pos];
		res += left;
		res += (1.0 - left * (1.0 * R + 1.0 / tim[pos])) * tim[pos];
		break;
	    }
	}
	
	printf("Case #%d: %.7lf\n", testcase, res);
    }
    return 0;
}
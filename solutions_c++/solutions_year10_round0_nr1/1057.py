#include <cstdio>
#include <functional>
#include <numeric>
#include <cstdlib>
#include <math.h>
#include <limits.h>
#include <float.h>
#include <algorithm>
#include <iostream>

using namespace std;

#define ABS(x) ((x)<0?-(x):(x))
#define SQR(x) ((x)*(x))
#define PB push_back
#define MP make_pair
#define SS stringstream
#define LL long long
#define SZ(x) int(x.size())
#define ALL(x) x.begin(),x.end()
#define FOR(a,b) for(int a=0;a<b;a++)
#define FORR(a,s,b) for(int a=s;a<=b;a++)
#define CLR(a,b) memset(a,b,sizeof(a))
#define VI vector<int>
#define VS vector<string>
               
int main()
{
	int t;
	cin >> t;

	FORR(cn,1,t) {
		int n,k;

		int sim[64]={0};
		cin >> n >> k;

		int lame=(1<<n)-1;
		cout << "Case #"<<cn<<": "<< ((k & lame)==lame ? "ON" : "OFF") << "\n";
	}

	return 0;
}



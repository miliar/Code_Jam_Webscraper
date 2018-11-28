#include <cstdio>
#include <iostream>
#include <algorithm>
#include <cstring>
#include <string>
#include <set>
#include <vector>
#include <cmath>
#include <cassert>
#include <cstdlib>
#include <map>

#define y0 y63475625
#define y1 y28435
#define pi 3.141592653589
#define sqr(x) ((x)*(x))

using namespace std;

typedef long long ll;
typedef long double ld;

int main()
{
	int T;
	cin >> T;
	for (int I=0;I<T;I++){
		int n,k;
		cin >> n >> k;
		bool kpyto=true;
		for (int i=0;i<n;i++)if ((k&(1<<i))==0){
			kpyto=false;break;
		}
		cout << "Case #" << I+1 << ": " << (kpyto?"ON\n":"OFF\n");
	}
	return 0;
}

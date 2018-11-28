#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <queue>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <cctype>
#include <string>
#include <cstring>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>

#define len(X) ((int)(X.length()))
#define size(X) ((int) (X.size()))

using namespace std;

int main(){
	string fname = "abig";
	freopen((fname+".in").c_str(), "r", stdin);
	freopen((fname+".out").c_str(), "w", stdout);
	int t=1,T;
	long N,K,r;
	scanf("%d",&T);
	while(t<=T){
		scanf("%d",&N);
		scanf("%d",&K);
		r=1;
		r=r<<N;
		K++;
		if(K%r==0)
		    printf("Case #%ld: ON\n",t);
		else
			printf("Case #%ld: OFF\n",t);
		t++;
	}
	return 0;
}

/*	Soumya Ranjan Maharana
	soumya.r.maharana@gmail.com  */

/*	Dev C++ portable    version 4.9.9.2
	http://www.bloodshed.net/
	Copyright (C) Bloodshed software 		*/

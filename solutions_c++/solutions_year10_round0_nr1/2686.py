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
	string fname = "a1";
	freopen((fname+".in").c_str(), "r", stdin);
	freopen((fname+".out").c_str(), "w", stdout);
	int t=1,T;
	long int n,k,b;
	scanf("%d",&T);
	while(t<=T){
		scanf("%ld",&n);
		scanf("%ld",&k);
		b=1;
		b<<=n;
		k++;
		if(k%b==0)
		    printf("Case #%d: ON\n",t);
		else
			printf("Case #%d: OFF\n",t);
		t++;
	}
	return 0;
}

/*	Chandan Dash
	sonu.dash@gmail.com

	devcpp
*/


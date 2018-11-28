#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cfloat>
#include <climits>
#include <cctype>
#include <cmath>
#include <cassert>
#include <ctime>

#include <iostream>
#include <iomanip>
#include <algorithm>
#include <sstream>
#include <string>
#include <vector>
#include <deque>
#include <list>
#include <queue>
#include <stack>
#include <map>
#include <set>
#include <bitset>
#include <complex>
#include <functional>
#include <numeric>

using namespace std;

typedef long long ll;

#define eps 1e-10
#define inf 0x3f3f3f3f

#define fr(x,y,z) for(int(x)=(y);(x)<(z);(x)++)
#define cast(x,t) *({stringstream ss;static t __ret;ss<<x,ss>>__ret;&__ret;})

#define dbg(x) cout << #x << " == " << x << endl
#define print(x) cout << x << endl

int N, K;

int main() {

	int T;
	scanf("%d",&T);
	
	for(int i = 1; i <= T; i++) {
		printf("Case #%d: ",i);
		scanf("%d %d",&N,&K);
		if( (K+1)%(1<<N) == 0 ) {
			printf("ON\n");
		}
		else {
			printf("OFF\n");
		}
	}

	return(0);
}

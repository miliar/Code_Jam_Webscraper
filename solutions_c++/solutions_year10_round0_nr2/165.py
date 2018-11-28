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

long long A[1010];
int N;

long long gcd(long long x, long long y) {
	while(y) {
		x %= y;
		swap(x,y);
	}
	return x;
}

long long lcm(long long x, long long y) {
	long long g = gcd(x,y);	
	return (x/g) * y;
}

int main() {

	int T;
	scanf("%d",&T);
	
	for(int i = 1; i <= T; i++) {
		printf("Case #%d: ",i);
		
		scanf("%d",&N);
		for(int i = 0; i < N; i++) {
			scanf("%I64d",&A[i]);
		}
		
		long long T = -1;
		for(int i = 0; i < N; i++) {
			for(int j = i+1; j < N; j++) {
				long long C = A[i]-A[j];
				if(C < 0) C = -C;
				
				//dbg(C);
				
				if(T == -1) {
					T = C;
				}
				else {
					T = gcd(T,C);
				}
			}
		}
		
		//dbg(T);

		long long y = -1;
		
		//(A[0]+y) % T == 0;
		
		y = (-A[0]%T + T)%T;
		
		
		printf("%I64d\n",y);	
	}
	
	return(0);
}

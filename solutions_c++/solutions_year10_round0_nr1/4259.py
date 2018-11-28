#include <iostream>
#include <vector>
#include <map>
#include <set>
#include <list>
#include <queue>
#include <algorithm>
#include <string>
#include <fstream>
#include <cstdio>
#include <cstdlib>
#include <sstream>
#include <ctime>
#include <cmath>
#include <numeric>

using namespace std;

typedef long long int64;
typedef vector<int> vi;
typedef vector<string> vs;
typedef vector<double> vd;
typedef pair<int,int> pii;

#define For(i,a,b) for (int i(a),_b(b); i <= _b; ++i)
#define Ford(i,a,b) for (int i(a),_b(b); i >= _b; --i)

int main(int argc, char* argv[])
{
	freopen("in.txt", "rt", stdin);
	freopen("out.txt", "wt", stdout);

	int T;
	scanf("%d", &T);

	For(test, 1, T){
		int N,K;
		scanf("%d %d",&N,&K);

		vector<int> snapper(N+1,0);
		vector<int> power(N+1,0);
		power[0]=1;
		
		For(flip,1,K){
			For(isnap,1,N){
				if(power[isnap-1]){
					snapper[isnap]=1-snapper[isnap];
				}
				else
					break;
			}
			For(isnap,1,N){
				power[isnap] = power[isnap-1]&snapper[isnap];
			}
		}

		if(power[N]){
			printf("Case #%d: ON\n", test);
		}
		else{
			printf("Case #%d: OFF\n", test);
		}
	}
}
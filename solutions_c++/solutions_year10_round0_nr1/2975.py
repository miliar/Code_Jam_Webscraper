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
		int64 K;
		int N;
		scanf("%d %lld",&N,&K);

		int64 maxiter=(int64)1<<(N);

		//vector<bool> snapper(N+1,false);
		//vector<bool> power(N+1,false);
		//power[0]=true;
		
		//int64 flip;
		//int isnap;
		//for(flip=1;flip<=K;flip++){
		//	if(power[N]){
		//		int64 temp=K+(int64)1;
		//		if((temp)%flip==0){
		//			break;
		//		}
		//		else{
		//			power[N]=0;
		//			break;
		//		}
		//	}
		//	for(isnap=1;isnap<=N;isnap++){
		//		if(power[isnap-(int64)1])
		//			snapper[isnap]=(~snapper[isnap]);
		//		else{
		//			break;
		//		}
		//	}
		//	for(isnap=1;isnap<=N;isnap++){
		//		if(power[isnap-(int64)1])
		//			power[isnap] = power[(isnap-(int64)1)]&snapper[isnap];
		//		else 
		//			break;
		//	}
		//}
		int64 temp=K+(int64)1;
		if(temp%maxiter==0){
			printf("Case #%d: ON\n", test);
		}
		else{
			printf("Case #%d: OFF\n", test);
		}
	}
}
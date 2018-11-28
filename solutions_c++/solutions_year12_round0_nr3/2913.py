#define _USE_MATH_DEFINES
#define INF 10000000
#include <iostream>
#include <sstream>
#include <cmath>
#include <algorithm>
#include <queue>
#include <stack>
#include <limits>
#include <map>
#include <string>
#include <cstring>
#include <set>
#include <deque>
#include <bitset>
#include <list>

using namespace std;

typedef long long ll;
typedef pair <int,int> P;
typedef pair <P,P> PP;
typedef pair <int,PP> PPP;

static const double eps = 1e-8;

int dp[1001][1001];

bool cmpPair(string A,string B){
	if(A.size() != B.size()) return false;
	for(int i=0;i<A.size();i++){
		string tmp = A;
		rotate(tmp.begin(),tmp.begin()+i,tmp.end());
		if(tmp==B) return true;
	}

	return false;
}

int main(){
	int T;
	memset(dp,-1,sizeof(dp));
	while(~scanf("%d",&T)){
		for(int t=0;t<T;t++){
			int A,B;
			scanf("%d %d",&A,&B);
			int sum = 0;
			for(int i=A;i<=B;i++){
				for(int j=i+1;j<=B;j++){
					if(dp[i][j] != -1){
						sum += dp[i][j];
						continue;
					}

					char buf1[128],buf2[128];
					sprintf(buf1,"%d",i);
					sprintf(buf2,"%d",j);
					string sA,sB;
					sA = buf1; sB = buf2;
					if(cmpPair(sA,sB)){
						dp[i][j] = 1;
						sum++;
					}
					else dp[i][j] = 0;
				}
			}

			printf("Case #%d: %d\n",t+1,sum);
		}

		break;
	}
}
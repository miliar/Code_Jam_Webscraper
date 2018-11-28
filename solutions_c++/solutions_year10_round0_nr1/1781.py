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
#include <complex> 
#include <sstream> 
#include <iostream> 
#include <iomanip> 
#include <cstdio> 
#include <cmath> 
#include <cstdlib> 
#include <cstring> 
#include <ctime> 
#include <cassert> 
using namespace std;

bool state[100];
int solve(int n){
	memset(state,false,sizeof(state));
	int cnt=1;
	while(true){
		int pos=-1;
		for(int i=0;i<n;i++)
			if(!state[i]){
				pos=i;
				break;
			}
		if(pos==-1)
			return cnt;
		cnt++;
		for(int i=0;i<=pos;i++)
			state[i]=!state[i];
	}
}
const int MAGIC[31]={
1,
2,
4,
8,
16,
32,
64,
128,
256,
512,
1024,
2048,
4096,
8192,
16384,
32768,
65536,
131072,
262144,
524288,
1048576,
2097152,
4194304,
8388608,
16777216,
33554432,
67108864,
134217728,
268435456,
536870912,
1073741824
};
int main(){
	int T,cas=0;
	scanf("%d",&T);
	while(T--){
		int n,k;
		scanf("%d%d",&n,&k);
		printf("Case #%d: %s\n",++cas,(k+1)%MAGIC[n]==0?"ON":"OFF");
	}
}

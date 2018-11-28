#include <stdio.h>
#include <string.h>
#include <string>
#include <vector>
#include <sstream>
#include <iostream>
#include <algorithm>
#include <functional>
#include <list>
#include <set>
#include <map>

using namespace std;

const int MAX_INT = 2147483647;
const int MAX_CHIKS = 51;
struct{
	long long pos;
	int vel;
}chiks[MAX_CHIKS];

int ans,cnt;
int N,K,T;
long long B;

void recurse(int target, int d){
	int i;
	for(i=target; i>=0; i--){
		if(cnt == K)
			return;
		if(chiks[i].pos + T*chiks[i].vel < B){
			if(i>0){
				recurse(i-1, d+1);
				return;
			}
		}else{
			ans+=d;
			cnt++;
		}
	}
}

int main(int argc, char* argv[])
{
	int tc;
    scanf("%d\n", &tc);
	for(int testnum=1; testnum<=tc; testnum++){
		char buf[8096];
	    int i,j,k;
		scanf("%d%d%lld%d\n", &N,&K,&B,&T);

		memset(chiks, 0, sizeof(chiks));

		for(i=0; i<N; i++){
			scanf("%lld", &chiks[i].pos);
        }
		for(i=0; i<N; i++){
			scanf("%d", &chiks[i].vel);
        }

		ans = cnt = 0;
		recurse(N-1, 0);

		if(cnt < K)
			cout << "Case #" << testnum << ": IMPOSSIBLE" << endl;
		else
			cout << "Case #" << testnum << ": " << ans << endl;
    }
	    return 0;
}


#include <stdio.h>
#include <algorithm>
#include <stdlib.h>
#include <string.h>
int n;
int mark[10003];
int mark2[10003];


int q[10003];
int do_greedy(int len){
	int h,t;
	h=t=0;
	int tans = 0x7fFFffFF;
	for(int i = 0;i <= 10001;i ++){
		if(mark[i] > (t-h)){ 
			int cnt = mark[i] - (t-h);
			int cnt2 = (t-h);
			for(int j = 0; j < cnt2;j ++){
				q[t-j-1] ++;
			}
			for(int j = 0;j < cnt;j ++){
				q[t++] = 1;
			}
		}else{
			for(int j = 0;j < mark[i];j ++){
				q[t-j-1] ++;
			}
		}
		int nh = t - mark[i];
		for(int j = h; j < nh; j++){
			tans = std::min(tans,q[j]);
		}
		h = nh;
	}
	if(tans == 0x7fFFffFF) tans = 0;
	return tans;
}

int main(){
	int T;
	scanf("%d",&T);
	for(int testcase = 1; testcase <= T; testcase ++) {
		scanf("%d",&n);
		memset(mark,0,sizeof(mark));
		for(int i = 0;i < n;i ++){
			int val;
			scanf("%d",&val);
			mark[val]++;
		}
		int ans = do_greedy(0);
		printf("Case #%d: %d\n",testcase,ans);
	}
	return 0;
}

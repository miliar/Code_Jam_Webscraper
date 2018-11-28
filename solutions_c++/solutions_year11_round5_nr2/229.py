#include <iostream>
#include <cstdio>
#include <utility>
#include <algorithm>
using namespace std;

const int maxL = 10000;
int cnt[maxL + 1],next[maxL + 1];
int top[maxL + 1];
int n;

bool check(int mid) {
	copy(cnt,cnt + maxL + 1,next);
	fill(top,top + maxL + 1,0);
	bool found = false;
	for(int i = 1;i<=maxL;) {
		int j;
		int mink = n + 1;
		if(next[i]>0) {
			for(j = i ;j<=maxL && j - i<mid;j++) {
				mink = min(mink,next[j]);
				if(next[j]==0)break;
			}
			if(mink==0 || j - i < mid) {
				for(;i<j;i++)
					if(top[i - 1]<next[i])
						return false;
					else {
						top[i - 1] -= next[i];
						top[i] += next[i];
					}
			} else {
				int ti = i;
				found = true;
				top[i + mid - 1] += mink;
				for(;i<j;i++) {
					next[i] -= mink;
				}
				i = ti;
				for(;i<j;i++) {
					if(next[i]==0) {
						i++;
						break;
					}
					if(top[i - 1]<next[i])
						return false;
					else {
						top[i - 1] -= next[i];
						top[i] += next[i];
					}
				}
			}
		}else i++;
	}
	return found;
}

void work() {
	int ans;
	for(ans = n;ans>=1;ans--)
		if(check(ans))break;
	printf("%d\n",ans);
}

int main(){
	int T;
	scanf("%d",&T);
	for(int tc = 1;tc<=T;tc++) {
		scanf("%d",&n);
		printf("Case #%d: ",tc);
		if(n==0) {
			puts("0");
			continue;
		}
		fill(cnt,cnt + maxL + 1,0);
		int a;
		for(int i = 0;i<n;i++){
			scanf("%d",&a);
			cnt[a]++;
		}
		work();
	}
	return 0;
}

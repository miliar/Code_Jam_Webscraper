#include <cstdio>
#include <cstring>
#include <algorithm>
using namespace std;

int TT,N;
char matrix[40][40];
long long mll[40];
int main(void) {
	scanf("%d",&TT);
	for(int T=1;T<=TT;T++) {
		memset(mll,0,sizeof(mll));
		scanf("%d",&N);
		for(int i=0;i<N;i++) {
			scanf("%s",matrix[i]);
			for(int j=0;j<N;j++)
				mll[i]+=(1ll<<(j))*(matrix[i][j]-'0');
		}
		int ans=0;
		/*
		for(int i=0;i<N;i++)
			for(int j=1;j<N;j++) {
				if( (mll[j]>mll[i]) and (mll[j]>=(1ll<<(j+1)))) {
					swap(mll[j],mll[j+1]);
					ans++;
				}
			}*/
		for(int i=0;i<N;i++) {
			if(mll[i]>=(1ll<<(i+1))) {
				for(int j=i+1;j<N;j++) {
					//serve
					if(mll[j]<(1ll<<(i+1))) {
						for(int k=j;k>i;k--) {
							swap(mll[k],mll[k-1]);
							ans++;
						}
						break;
					}
				}
			}
		}
		printf("Case #%d: %d\n",T,ans);
	}
	return 0;
}

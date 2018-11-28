#include <cstdio>
#include <algorithm>
using namespace std;

int main() {
	int T, N;
	int m[50];
	char buff[100];
	scanf("%d",&T);
	for(int t=0;t<T;++t) {
		scanf("%d",&N);
		for(int n=0;n<N;++n) {
			scanf(" %s",buff);
			m[n]=0;
			for(int n2=N-1;n2>=0;--n2)
				if(buff[n2]=='1') {
					m[n]=n2;
					break;
				}
		}
		int ans=0;
		for(int n=0;n<N;++n)
			if(m[n]>n) {
				int i=n+1;
				while(m[i]>n) ++i;
				while(i>n) swap(m[i],m[i-1]), --i, ++ans;
			}
		printf("Case #%d: %d\n",t+1, ans);
	}
}
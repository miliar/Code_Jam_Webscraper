#include <cstdio>
#include <algorithm>
#include <string>
using namespace std;

int main() {
	int N, K;
	char buff[100000];
	char buff2[100000];
	scanf("%d",&N);
	for(int n=0;n<N;++n) {
		scanf("%d %s",&K,buff);
		string perm;
		for(int i=0;i<K;++i)
			perm+=char(i+'0');
		int nr=1<<28;
		do{
			for(int i=0;i<100000 && buff[i]!=0;i+=K) {
				for(int k=0;k<K;++k) {
					buff2[i+perm[k]-'0']=buff[i+k];
				}
			}
			int groups=1;
			for(int i=1;i<100000 && buff[i]!=0;++i)
				if(buff2[i]!=buff2[i-1])
					groups++;
			nr=min(nr,groups);
		} while(next_permutation(perm.begin(), perm.end()));
		printf("Case #%d: %d\n",n+1, nr);
	}
}
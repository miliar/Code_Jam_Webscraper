#include<stdio.h>
#include<algorithm>

char str[1001], st1[1001];
int per[5];
int main() {
	int T;
	scanf("%d", &T);
	for(int cas=1;cas<=T;cas++) {
		int k;
		scanf("%d", &k);
		scanf("%s", str);
		for(int i=0;i<k;i++) per[i]=i;
		int mn=1000;
		do {
			int p;
			for(p=0;str[p];p+=k)
				for(int i=0;i<k;i++)
					st1[p+i]=str[p+per[i]];
			st1[p]=0;

			int cnt=1;
			for(int i=1;st1[i];i++)
				if(st1[i]!=st1[i-1]) cnt++;

			if(cnt<mn) mn=cnt;
		}while(std::next_permutation(per, per+k));
		printf("Case #%d: %d\n", cas, mn);
	}
}
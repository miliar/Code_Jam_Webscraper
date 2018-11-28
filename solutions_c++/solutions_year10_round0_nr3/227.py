#include <stdio.h>
#include <string.h>
#define MAX 10000001

int g[MAX];
int R,k,N;
__int64 val[1001];
int index[1001];

int MakeIndex() {
	int i,pre;
	memset(val,0,sizeof(val));
	memset(index,-1,sizeof(index));
	__int64 sum = 0;
	i = 0;
	pre = 0;
	while(1) {
		if(i>=N) i=0;
		if(sum+g[i]<=k)	{
			sum += g[i];
			++i;
		} else {
			val[pre] = sum;
			if(index[pre]!=-1) {
				return 1;
			} else {
				index[pre] = i;
				sum = 0;
			}
			pre = i;
		}
	}
	return 0;
}

int main(int argc, char *argv[])
{
	int T,Case;
	int i,j;
	__int64 sum;
	scanf("%d",&T);
	for(Case = 1; Case <= T; Case++) {
		scanf("%d%d%d",&R,&k,&N);
		__int64 ts = 0;
		for(i=0;i<N;i++) {
			scanf("%d",&g[i]);
			ts += g[i];
		}
		printf("Case #%d: ",Case);
		if(ts<=k) {
			printf("%I64d\n",ts*R);
			continue;
		}
		MakeIndex();
		int trace;
		sum = 0;
		for(trace = 0,i=0;i<R;i++) {
			sum += val[trace];
			trace = index[trace];
		}
		printf("%I64d\n",sum);
	}
	return 0;
}

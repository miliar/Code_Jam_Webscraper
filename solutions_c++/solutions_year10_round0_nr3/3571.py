#include <cstdio>
#include <cstring>
#include <map>
#include <vector>
#include <cmath>
using namespace std;
int testcase;
int R;
unsigned int K;
int N;//group count
unsigned int  g[1000];
unsigned __int64  money=0;
void makeMoney(){
	int i;
	int j;
	int start=0,end=0;
	int sum=0;
	money=0;
	//printf("%d %d\n",R,K);
	for (i=0;i<R;i++)
	{
		sum=g[start];
		while(1){
			end=(end+1)%N;
			if (end!=start)
			{
				if (sum+g[end]<=K)
				{
					sum+=g[end];
				}else{
					start=end;
					break;
				}
			}else{
				start=end;
				break;
			}
		}
		money+=sum;
	}
}
int main(){
	int i,j;
	freopen("C-small-attempt0.in","rt",stdin);
	freopen("themepark.out","wt",stdout);
	scanf("%d",&testcase);
	for (i=0;i<testcase;i++)
	{
		scanf("%d %d %d",&R,&K,&N);
		for (j=0;j<N;j++)
		{
			scanf("%d",&g[j]);
		}
		money=0;
		makeMoney();
		printf("Case #%d: ",i+1);
		printf("%d\n",money);
	}

	return 0;
}
#include <iostream>
using namespace std;

int main()
{
    int T;
	int cas=1;
	//freopen("E:\\data\\C-small-attempt0.in","r",stdin);
	//freopen("E:\\data\\outC1.txt","w",stdout);

	scanf("%d",&T);
	while(T--){
		int n,i;
		int t,x_min=100000000,x_sum=0,sum=0;
		scanf("%d",&n);
		for(i=0;i<n;++i){
			scanf("%d",&t);
			if(t<x_min)
				x_min=t;
			x_sum = (x_sum^t);
			sum=sum+t;
		}

		if(x_sum == 0){
			printf("Case #%d: %d\n",cas++,sum-x_min);
		}
		else{
			printf("Case #%d: NO\n",cas++);
		}
	}
	return 0;
}
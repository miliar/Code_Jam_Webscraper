#include<cstdio>
#include<algorithm>

using namespace std;

int main(){
	int T;
	scanf("%d",&T);
	for(int tc=1;tc<=T;tc++){
		int N,mindata=10000000,sum=0,f=0,data;
		scanf("%d",&N);
		for(int i=0;i<N;i++){
			scanf("%d",&data);
			mindata=min(mindata,data);
			sum+=data;
			f^=data;
		}
		printf("Case #%d: ",tc);
		if(f==0)printf("%d\n",sum-mindata);
		else printf("NO\n");
	}
	return 0;
}

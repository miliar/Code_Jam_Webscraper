#include<cstdio>
#include<cstring>
using namespace std;
int main(){
	int n,i,j,T,t,s,p,a;
	char ch;
	freopen( "B-large.in", "r", stdin );
	freopen( "output1.out", "w", stdout );
	scanf("%d",&T);
	for(t=1;t<=T;t++){
		printf("Case #%d: ",t);
		int sum1=0,sum2=0,sum=0;
		scanf("%d %d %d",&n,&s,&p);
		if(p==0 || p==1){
			for(i=1;i<=n;i++){
				scanf("%d",&a);
				if(a>=p)
					sum1++;
				if(a>=2)
					sum++;
			}
			if(sum<s)
				printf("0\n");
			else
				printf("%d\n",sum1);
		}
		else{
			for(i=1;i<=n;i++){
				scanf("%d",&a);
				if(a>=2)
					sum++;
				if(a>=p*3-2)
					sum1++;
				else if(a>=p*3-4)
					sum2++;
			}
			if(sum<s)
				printf("0\n");
			else if(sum2>s)
				printf("%d\n",s+sum1);
			else
				printf("%d\n",sum1+sum2);
		}
	}
}
#include<iostream>
#include<queue>
using namespace std;

int t,n;
long r,k;
long group[1001];

void Handle(){
	__int64 sum=0;
	long beg=0;
	for(long i=1;i<=r;++i){
		long end=beg;
		long add=0;
		while(add+group[beg]<=k){
			add+=group[beg];
			beg=(beg+1)%n;
			if(beg==end)
				break;
		}
		sum+=add;
		if(beg==0){
			long mul=r/i;
			sum*=mul;
			i*=mul;
		}
	}
	printf("%lld\n",sum);
}

int main()
{
	freopen("C-large.in","r",stdin);
	freopen("test.out","w",stdout);
    cin>>t;
    for(int i=1;i<=t;++i){
    	printf("Case #%d: ",i);
    	scanf("%ld%ld%d",&r,&k,&n);
    	for(int j=0;j<n;++j)
    		scanf("%ld",&group[j]);
    	Handle();
	}
    return 0;
}

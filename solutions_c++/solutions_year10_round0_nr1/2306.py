#include <cstdio>

using namespace std;

int main(){
	long t;
	scanf("%d",&t);
	
	long i;long n,k1;long j;int state[15];long q;long ans=1;
	for(i=0;i<t;i++){
		
		scanf("%ld%ld",&n,&k1);

		

		
		for(j=1;j<11;j++)
			state[j]=0;
		state[0]=1;//The first one;

		
		for(q=0;q<k1;q++){
			state[1]=1-state[1];
			j=1;
			while(!state[j++]){
				state[j]=1-state[j];
			}
		}

		ans=1;
		for(j=0;j<=n;j++){
			if(!state[j])
				ans=0;
		}

		printf("Case #%d: %s\n",i+1,ans?"ON":"OFF");

	}

	return 0;
}
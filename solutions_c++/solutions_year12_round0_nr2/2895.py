#include<stdio.h>
#include<stdlib.h>
#include<string.h>
#include<algorithm>
using namespace std;


int t[150];

int main(){
//	freopen("B.IN","r",stdin);
//	freopen("o.txt","w",stdout);

	int T,S,p,N,i,j,tot,nh,ml,sl;

	scanf("%d",&T);

	for(i=1;i<=T;i++){
		scanf("%d%d%d",&N,&S,&p);

		ml=3*p-2;
		sl=3*p-4;

		for(j=0;j<N;j++)
			scanf("%d",&t[j]);
		sort(t,t+N);

		tot=0;

		for(j=N-1;t[j]>=ml && j>=0;j--)
			tot++;

		for(;t[j]>=sl && j>=0;j--,S--){
			if(S<1)
				break;

			if(sl<2)
				break;
			tot++;
		}


		printf("Case #%d: %d\n",i,tot);


	}



  return 0;
}
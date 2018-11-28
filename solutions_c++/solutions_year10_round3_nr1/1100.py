#include <stdio.h>
#include <algorithm>
#include <string.h>
#include <string>
#include <math.h>
using namespace std;

const int max_size=1003;
const double eps=1E-7;
struct line{
	int a,b;
}wire[max_size];

int main(){
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	int T,N;
	scanf("%d",&T);
	for(int i=0;i<T;i++){
		scanf("%d",&N);
		for(int j=0;j<N;j++){
			scanf("%d %d",&wire[j].a,&wire[j].b);
		}
		long long sum=0;
		for(int j=0;j<N;j++){
			for(int l=j+1;l<N;l++){
				double tmp=((double)(wire[l].a-wire[j].a))/((double)(wire[j].b-wire[j].a)-(wire[l].b-wire[l].a));
				if(tmp>eps && tmp+eps<1)
					sum++;
			}
		}
		printf("Case #%d: %lld\n",i+1,sum);
	}
	return 0;
}
#include<stdio.h>
#include<algorithm>
using namespace std;
bool comp(int a,int b )
{ 
	return a<b;
}

int go[105];
int main(){
	int t,ti,n,s,p;
	freopen("B-large.in","r",stdin);
	freopen("B-large.out","w",stdout);
	scanf("%d",&t);
	for(ti=1;ti<=t;ti++){
		printf("Case #%d: ",ti);
		scanf("%d %d %d",&n,&s,&p);
		int i;
		for(i=0;i<n;i++)
			scanf("%d",&go[i]);
		sort(go,go+n,comp);
		int sum=0;
		for(i=0;i<n;i++){
			if((go[i]+2)/3>=p)sum++;
			else if(s>0&&go[i]>=2&&go[i]<=28&&(go[i]+4)/3>=p){
				sum++;
				s--;
			}
		}
		printf("%d\n",sum);
	}
	return 0;
}
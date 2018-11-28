#include<stdio.h>
#include<string.h>
#define MAX 50
int ans[MAX];
int len,a,b;
int temp[8];
int find(int a){
	int i;
	for(i=0;i<8;i++)
		if(a==temp[i])return 1;
	return 0;
}
int next(int x){
	int i,temp=x%10;
	x/=10;
	for(i=0;i<len-1;i++)temp*=10;
	x+=temp;
	return x;
}
void check(int i){
	if(i==next(i)){
		ans[1]++;
		return;
	}
	int j,sum=1;
	memset(temp,-1,sizeof(temp));
	for(j=0;j<len-1;j++){
		temp[j]=i;
		i=next(i);
		if(!find(i)&&i>=a&&i<=b)sum++;
	}
	ans[sum]++;
}

int main(){
	int t,ti;
	freopen("C-large.in","r",stdin);
	freopen("C-large.out","w",stdout);
	scanf("%d",&t);
	for(ti=1;ti<=t;ti++){
		printf("Case #%d: ",ti);
		scanf("%d %d",&a,&b);
		int i;
		for(i=0;i<MAX;i++)ans[i]=0;
		len=0;
		int tee=a;
		while(tee){
			len++;
			tee/=10;
		}
		for(i=a;i<=b;i++)
			check(i);
		int sum=0;
		for(i=2;i<MAX;i++)
			sum+=ans[i]*(i-1)>>1;
		printf("%d\n",sum);
	}
	return 0;
}
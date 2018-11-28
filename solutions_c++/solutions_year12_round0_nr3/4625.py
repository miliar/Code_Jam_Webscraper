#include<stdio.h>
#include<algorithm>
using namespace std;
const int maxn=1024*2048;
int a[maxn];
int s[maxn];
int m[16];
void add(int v){
	int p=1;
	for(int val=v;val;val/=10)
		p*=10;
	p/=10;
	int val=v;
	int cnt=0;
	do{
		if(v%10){
			v=p*(v%10)+v/10;
			cnt+=(v<val);
			//printf("%d ",v);
		}
		else
			v=p*(v%10)+v/10;

	}while(v!=val);

	a[val]+=cnt;

	
	//putchar('\n');
}
bool check(int a,int b){
	int p=1;
	for(int val=a;val;val/=10)
		p*=10;
	p/=10;
	int val=a;
	int cnt=0;
	do{
		if(val%10){
			val=p*(val%10)+val/10;
			if(val==b)
				return 1;
		}
		else
			val=p*(val%10)+val/10;		

	}while(a!=val);
	return 0;

}
int calc(int l,int r){
	int i,j;
	int res=0;
	for(i=l;i<=r;i++)
		for(j=i+1;j<=r;j++)
			res+=check(i,j);
	return res;
}
int main(){
#ifdef _DEBUG
	freopen("in.txt","r",stdin);
	freopen("out.txt","w",stdout);
#endif
	int i,n;
	memset(a,0,sizeof(a));
	for(i=1;i<100;i++){
		add(i);
	}
	scanf("%d",&n);
	s[0]=0;
	for(i=1;i<100;i++){
		s[i]=s[i-1]+a[i];
	}

	for(i=0;i<n;i++)
	{	int v1,v2;
		scanf("%d%d",&v1,&v2);
		printf("Case #%d: %d\n",i+1,calc(v1,v2));
	}
	

	return 0;
}
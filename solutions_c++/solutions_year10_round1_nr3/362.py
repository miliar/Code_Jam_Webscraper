#include <cstdio>

int a1,a2,b1,b2;
int T;

int check(int a,int b){
	if(a==0||b==0)
		return 0;
	if(a==b)
		return 1;
	if(a>b){
		if(a-b<=b)
			return 1-check(a-b,b);
		return 1-(check(a%b,b)||check(a%b+b,b));
	}
	else{
		if(b-a<=a)
			return 1-check(b-a,a);
		return 1-(check(b%a,a)||check(b%a+a,a));
	}
}

int main(){
	freopen("out.txt","w",stdout);
	scanf("%d",&T);
	for(int t = 1;t <= T;++t){
		scanf("%d%d%d%d",&a1,&a2,&b1,&b2);
		int num=0;
		for(int a = a1;a <= a2;++a)
			for(int b = b1;b <= b2;++b)
			{
				int tt = check(a,b);
				num += 1-tt;
			}
		printf("Case #%d: %d\n",t,num);
	}
}
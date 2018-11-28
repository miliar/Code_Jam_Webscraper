#include<stdio.h>
int main()
{
	int _,t,a,b;
	scanf("%d",&_);
	for(t=1; t<=_; t++)
	{
		scanf("%d%d",&a,&b);
		a=(1<<a)-1;
		printf("Case #%d: ",t);
		puts((b&a)==a?"ON":"OFF");
	}
	return 0;
}

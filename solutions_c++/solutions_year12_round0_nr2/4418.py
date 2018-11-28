#include<stdio.h>

int main()
{
	int t,k,n,s,p,i,no;
	int total,ans=0;
	scanf("%d",&t);
	k=t+1;
	while(t>0)
	{
	scanf("%d%d%d",&n,&s,&p);
	for(i=1;i<=n;i++)
	{
	scanf("%d",&total);
	if(total==0 && p==0)	ans++;
	if(total==1 && p<=1) ans++;	
	if(total==2) {no=1;
		if(no>=p) ans++;
		else if(no+1>=p && s>0) {ans++;s--;}
		}

	else if(total>=3){
	no=total/3;
	if(total%3==0)
		{
		if(no>=p) ans++;
		else if(no+1>=p && s>0) {ans++;s--;}
		}
	else if(total%3==1)
		{
		if(no+1>=p) ans++;
		}
	else if(total%3==2)
		{
		if(no+1>=p) ans++;
		else if(no+2>=p && s>0) {ans++;s--;}
		}
	 }	
	}
	printf("Case #%d: ",k-t);
	printf("%d\n",ans);
	t--;
	ans=0;
	}
return 0;
}

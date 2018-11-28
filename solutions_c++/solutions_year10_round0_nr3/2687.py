#include<stdio.h>
#include<math.h>


long int data[100000];

int main()
{

long int r,tc,i,jj,ll,m,k,t,n,mm,d,count;
long int f,l,j,temp;
//freopen("C-small-attempt0.in","r",stdin);
//freopen("C-small-attempt0.out","w",stdout);


scanf("%ld",&tc);


for(t=1;t<=tc;t++)
{
  count=0;
	scanf("%ld %ld %ld",&r,&k,&n);

	for(i=1;i<=n;i++)
		scanf("%ld",&data[i]);
	 
	
	f=1;
	l=n;
	for(i=1;i<=r;i++)
	{
		temp=0;
		j=f;
	jj=1;
	ll=n;
	for(;jj<=ll;j++)
		if((data[j]+temp)<=k)
		{
			temp+=data[j];
		    data[++l]=data[j];
		jj++;
		}
		else 
		{
			f=j;
			break;
		}
	count=count+temp;
	} 

printf("Case #%ld: %ld\n",t,count);
} 

return 0;
}
#include<stdio.h>
#include<math.h>


long int data[31];

int main()
{

long int n,tc,i,m,k,t,mm,d;

//freopen("A-large.in","r",stdin);
//freopen("A-large.out","w",stdout);

scanf("%ld",&tc);

data[1]=2;
	
	for(i=2;i<=30;i++)
		data[i]=2*data[i-1];


for(t=1;t<=tc;t++)
{
	scanf("%ld%ld",&n,&k);

	
	 m=data[n];
     mm=k+1;
	 
	 d=mm/m;

	 if(mm==d*m)
          printf("Case #%ld: ON\n",t);
     else 
		  printf("Case #%ld: OFF\n",t);
} 

return 0;
}
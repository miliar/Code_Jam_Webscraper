#include<string.h>
#include<fcntl.h>
#include <sys/types.h>
#include <stdio.h>
#include <unistd.h>
#include <errno.h>
#include <stdlib.h>
#include <math.h>
#include <netdb.h>
unsigned long int t,a,b,m,n,ans=0,temp,nn[30],mm[30];
int rem[10],ni=0,mi=0;
long int pow(long int x,long int y);
void check(unsigned long int i);

long int pow(long int x,long int y)
{
	long int temp = 0,ans = 1;
	while(temp++<y)
	{
		ans = ans * x;
	}
	return ans;
}

void check(unsigned long int i)
{	
	temp = i;
	n = i;
	int no=0,k=0,l=0,newno=0;
	//printf("\ni= %ld rem = ",i);
	while(temp)
	{
		rem[no++] = temp % 10;
		temp = temp / 10;
		//printf("%d ",rem[no-1]);	
	}
	if(no!=1)
	{
	//printf("no = %d",no);
	ni=0;mi=0;
	while(k<(no-1))
	{
		l=k+1;
		m = 0;
		//100 001 010 123 321 230
		while(l>0)
		{
			m = m + (rem[l-1] * pow((long int)10,(long int)(l-1)));
			//printf("\npre rem = %ld pre m = %ld",(rem[l-1] * pow((long int)10,(long int)(l-1))),m);
			l--;
		}
		m = m * pow((long int)10,(long int)(no-k-1));
		l = k+1;
		//while(l-->(k+1))
		{
			//printf(" l = %d",l);			
			m = m + (n / pow((long int)10,(long int)l));
			//printf(" rem = %ld aft m = %ld",(n / pow((long int)10,(long int)l)),m);
		}
		//printf("\nn=%ld m=%ld",n,m);
		temp = m;
		newno = 0;
		while(temp)
		{
			newno++;
			temp = temp / 10;
			//printf("%ld ",rem[no-1]);	
		}
		//112 121
		//printf("\t no = %d newno = %d",no,newno);
		
		if(n<m && no==newno && n>=a && m<=b)
		{
			ans++;
			nn[ni++]=n;
			mm[mi++]=m;
			//printf("\nn=%ld m=%ld",n,m);
			//printf(" ans=%ld",ans);
		}
		k++;
	}
	int loopi,loopo=0;
	while(loopo<ni)
	{
		loopi = loopo+1;
		while(loopi<ni)
		{
			if(nn[loopo] == nn[loopi] && mm[loopo] == mm[loopi])
			{
				//printf("\nmatched: n=%ld m=%ld",nn[loopo],mm[loopo]);
				ans--;
			}
			loopi++;
		}
	loopo++;
	}
     }
}

int main(int argc, char *argv[])
{
        unsigned long int i,j,t;
       	int fdi = open("input.txt",O_RDONLY);
        int fdo = open("output.txt",O_WRONLY|O_CREAT,0644);
        close(1);
        dup(fdo);
        close(0);
        dup(fdi);
        close(fdo);
        close(fdi);
	scanf("%ld\n",&t);
	//printf("\n%ld %ld %ld\n",pow((long int)10,(long int)0),pow((long int)10,(long int)2),pow((long int)10,(long int)3));
	for(j=0;j<t;j++)
        {
		scanf("%ld %ld\n",&a,&b);
		//printf("%d %d %d ",t,a,b);
		i=a;
		ans = 0;
		printf("Case #%ld: ",j+1);
		while(i<b)
		{                
			check(i++);
		}
		printf("%ld\n",ans);
        }
return 0;
}

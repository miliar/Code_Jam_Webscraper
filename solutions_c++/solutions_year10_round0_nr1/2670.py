#include<iostream.h>
int bit(int a,int b)
{
	int i,ans=1;
	for(i=0;i<b;i++)
		ans*=a;
	return ans-1;
}

int main()
{
	FILE *in=fopen("insnap.txt","r");
	FILE *out=fopen("outsnap.txt","w");
	int t,n,k,j,i,count=0,temp1,temp2,temp3;
	
	fscanf(in,"%d",&t);
while(count++<t)
{
	fscanf(in,"%d%d",&n,&k);
	if(k==0)
	{
			fprintf(out,"Case #%d: OFF\n",count);
			continue;
	}
	temp1=bit(2,n);
	if((k+1)%(temp1+1)==0)
			fprintf(out,"Case #%d: ON\n",count);
	else
	fprintf(out,"Case #%d: OFF\n",count);

}



}	 
	 


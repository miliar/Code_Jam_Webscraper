#include <stdio.h>

int main ()
{
	FILE *p1,*p2;
	int N,S,p,numbers[100],cas=0;
	p1= fopen("try.txt","r");
	p2=fopen("output.txt","a");
    int t;
    fscanf(p1,"%d",&t);
    while(t--)
    {
    	cas++;
        fscanf(p1,"%d%d%d",&N,&S,&p);
    	for(int i=0;i<N;i++)
    	{
        	fscanf(p1,"%d",&numbers[i]);
    	}
    	int count=0,scount=0,br;
    	for(int i=0;i<N;i++)
    	{
       	 int n=numbers[i];
        	if(n%3==0)
        	{
           	 br=n/3;
       		 }
        else
        {
            br=(n/3)+1;
        }
        if(br>=p)
            count++;
        else if(p-br==1&&n%3!=1&&n>=3)
        {
            if(scount<S)
            {
                count++;
                scount++;
            }
        }
    }
    fprintf(p2,"Case #%d: %d\n",cas,count);
    }
   	fclose(p1);
	fclose(p2);
    return 0;
}

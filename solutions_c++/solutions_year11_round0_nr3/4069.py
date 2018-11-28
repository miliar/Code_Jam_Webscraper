#include<stdio.h>
#include<conio.h>
void bubble_sort(unsigned int*, size_t);
int main()
{
        int num,j,k1,t,i,sum=0,small=-1,left,prevsum,temp,k,dignotalo[20],p,flag,a1,z,cas=1;
        unsigned int a[20];
        
        FILE *fp, *fp1;
        fp= fopen ("C:\\abc\\inp.txt","r");
        fp1=fopen("C:\\abc\\out.txt","w");
        
        fscanf(fp,"%d",&t);
        while(t--)
        {
        	sum=0;left=0,prevsum=-1,temp=0;
			fscanf(fp,"%d",&num);
        	for(i=0;i<num;i++)
        	  fscanf(fp,"%d",&a[i]);
          bubble_sort(a,num);
		  
		 for (z=0;z<num;z++) 
		  for (j=1;j<=num-z;j++)
		  {
  			temp =0;p=0;k1=j;
		  while(k1--)
		    {
    			temp = temp^a[z+j-1];
    			dignotalo[p++]=z+j-1;
		    }
    			left=0;sum=0;
 			 for(k=0;k<num;k++)
 			 {
 			    flag=0;	
			   for(a1=0;a1<p;a1++)
 			 	 if (k==dignotalo[a1])
 			 	  {
 			 	   flag=1;
 			 	   break;
 			 	  }
 			 	if (flag ==1)
				  continue;   
			    left =left^a[k];
 			 	sum=sum+a[k];
 			 }
    		 if (left == temp && sum > prevsum && sum !=0)
    		   prevsum = sum;
			}
		  if (prevsum > -1)
		    fprintf(fp1, "Case #%d: %d\n", cas++,prevsum);
	   else
	       fprintf(fp1, "Case #%d: NO\n", cas++);
		}
    return 0;
}
void bubble_sort(unsigned int *iarray, size_t size) {
int x,y,holder;
for(x = 0; x < size; x++)
    for(y = 0; y < size-1; y++)
      if(iarray[y] > iarray[y+1]) {
        holder = iarray[y+1];
        iarray[y+1] = iarray[y];
        iarray[y] = holder;
      }

}

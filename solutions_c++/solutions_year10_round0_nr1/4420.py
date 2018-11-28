#include<stdio.h>
#include<memory.h>
#include<string.h>
int n ,k, t;
int on[11];
int power[11];

int main()
{

	
	FILE *fp=fopen("A-small-attempt2.in", "r");
    FILE *ofp=fopen("a.out", "w");
    

	int i, j,index,tc=1;
	fscanf(fp, "%d", &t);
	
	while((t--)>0)
	{
       memset(on, 0, sizeof(on));
       memset(power, 0, sizeof(power));
       power[0]=1;
       fscanf(fp, "%d %d", &n, &k);
       for(i=0;i<k;i++){
      
            for(j=1;j<n;j++){
               if((on[j-1]&&power[j-1])==1)
                  power[j]=1;
               else
                  power[j]=0;
            }
            for(j=n-1;j>0;j--)
            {
                if((power[j])==1)
                {
                  if(on[j]==1)
                  on[j]=0;
                  else
                  on[j]=1;
                }
            }
            if(on[0]==1)
              on[0]=0;
            else
             on[0]=1;
             
          
      }
       
        for(j=1;j<n;j++){
               if((on[j-1]&&power[j-1])==1)
                  power[j]=1;
               else
                  power[j]=0;
            }   
       
       if((on[n-1]==1)&&(power[n-1]==1))
          fprintf(ofp, "Case #%d: ON\n", tc++);
       else
          fprintf(ofp, "Case #%d: OFF\n", tc++);   
         
       
                  
    }
	
	return 0;
}

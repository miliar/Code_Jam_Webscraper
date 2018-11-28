# include <stdio.h>
# include <string.h>

int main()
{

    char x[510],y[510],cg;
	int r,l1,l2,i,j,c[510][510],cas;
	
    strcpy(y,"welcome to code jam"); 
    
    //freopen("C-large.in","r",stdin);
   // freopen("c out.txt","w",stdout);
    scanf("%d%c",&cas,&cg);


	 for(r = 1;r <= cas;r++)
	 {
         gets(x);
		 memset(c,0,sizeof(c));
		 l1 = strlen(x);
		 l2 = 19;

		 // for first row
		 
		 for(i = 1;i<=l1;i++)
		  if(y[0] == x[i-1])
		   c[1][i] = c[1][i-1] + 1;
	      else
	       c[1][i] = c[1][i-1];
		  
		 
          for(i=2;i<=l2;i++)              
		    for(j=i;j<=l1;j++)
               if(x[j-1] == y[i-1])
                   c[i][j] = (c[i-1][j-1] + c[i][j-1])%10000;
			   else
               c[i][j] = c[i][j-1];
       
		   printf("Case #%d: %04d\n",r,c[i-1][j-1]);
		  
		   
		   
  }
  
 
return 0;
}

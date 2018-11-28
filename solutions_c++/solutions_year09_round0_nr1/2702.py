
#include<stdio.h> 
#include<string.h>
char inputs[25][11];
int l,d,n;
char slot_det[10][1000];
bool matchothers(int i)
{  
     int c=0,j,r=0;	
     int  flag1;
     while(c<l)              // traversing that word
    {
	 j=0;
	 flag1=0;
	//  printf("Flag reset to zero ");
	 
	 while(slot_det[r][j]!=' ')
	 {
	      if(slot_det[r][j]==inputs[i][c])
	      {
		//   printf("i=%d",i);
		//   printf("Matched %c with %c\n",slot_det[r][j],inputs[i][c]);
		   flag1=1;
 		//   printf("setting flag to 1");
		   break;
	      }
	      j++;
	 }
	      
	  c++;
	  r++;
    
  //printf("Flag : %d\n",flag1);
     if(flag1==0)
		    return  false;
	
    }
    if(flag1==0)
	 return false;
    else
	 return true;
 }
  


int  findmatch(char c)
{
  //   printf("Inside findmatch");
     int i=0;
     int ways=0;
     char  a;
     while(i<d)
     {
	  a=inputs[i][0];
	  if(a==c)
	  {
//	     printf("Matching with %s\n\n",inputs[i]);
	       if(matchothers(i))
	       {
		     ways++;
	       }
	  
	  }
	i++;
     }
return ways;  
}
int main()
{
      char testcases[10][1000];
      int slot=-1;
      int i,j,k,m,ways,open=0;
      char word[25],c;
     scanf("%d %d %d",&l,&d,&n );
      //printf("%d %d",l,d);
      
     for(i=0;i<d;i++)
     { 
	  scanf("%s",inputs[i]);
	 //printf("Copying into  inputs %s",word);
	// strcpy(inputs[i],word);
     }
       for(i=0;i<d;i++)
     {
	//  printf("%d==>\n%s%d\n",i,inputs[i],strlen(inputs[i]));
	 //printf("Copying into  inputs %s",word);
	// strcpy(inputs[i],word);
     }
   //  printf("this is it");
     for(i=0;i<n;i++)
    {
	   scanf("%s",testcases[i]);           
      }
     for(i=0;i<n;i++)
    {
		    slot=-1;
		    for(k=0;k<10;k++)
		    {
			 for(m=0;m<100;m++)
			 {
			     //printf("empty");
			      slot_det[k][m]=' ';
			 }
		    }
	  for(j=0;j<strlen(testcases[i]) ;j++)             // runs for each  test case
	  {
		   
			      ways=0;
		
			      c=testcases[i][j];
		     if(c=='(')             // a slot starts
		     {
			  slot++;
		//  j++;    //we do not want to include the (
			  k=0;
			  open=1;
			  while(c!=')')
			  {
				   j++;
				c=testcases[i][j];
				if(c==')')
				     break;
		//	    printf("Checking slots for %c\n",c);
			       slot_det[slot][k]=c;
				k++;
				
			  }
			  if(c==')')
			       open=0;
			  
		     }
		     else if(open==0)
			{	
	//    printf("Checking slots for open=0 %c\n",testcases[i][j]);
			  slot_det[++slot][0]=testcases[i][j];
			}
	  }
	  c=slot_det[0][0];     // starting with the first character in the first slot
	  k=0;
	  while(c!=' ')
	  {
	//     printf("Finding match for starting with %c:\n",c);
	      ways+=findmatch(c);
	      c=slot_det[0][++k];
	      
	  }
	  printf("Case #%d: %d\n",i+1,ways);
	  }
      return 0;
}
       
      
      
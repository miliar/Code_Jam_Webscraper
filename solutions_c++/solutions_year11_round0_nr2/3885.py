#include<stdio.h>
#include<conio.h>

int main()
{
        char c[4],d[3],n[101],final[500],k,m[101];;
        int other,c1,d1,n1,t,i=0,cas=1,m1,first,second,flag;
        
        FILE *fp, *fp1;
        fp= fopen ("C:\\abc\\inp.txt","r");
        fp1=fopen("C:\\abc\\out.txt","w");
        
        fscanf(fp,"%d",&t);
        while(t--)
        {
             first = -1;second=-1;
			 for(i=0;i<4;i++)
               c[i] = '\0';
             for(i=0;i<3;i++)
               d[i] = '\0';
             for(i=0;i<101;i++)
               n[i] = '\0';   
              for(i=0;i<101;i++)
               m[i] = '\0';   
             for(i=0;i<500;i++)
               final[i] = '\0';    
             fscanf(fp,"%d",&c1);
             if(c1 != 0)
                   fscanf(fp,"%s",c); 

              fscanf(fp,"%d",&d1);
             if(d1 != 0)
                   fscanf(fp,"%s",d); 
             fscanf(fp,"%d",&n1);
             fscanf(fp,"%s",n); 
         m1=0;flag=0;
         if (c1 == 0 && d1 == 0)
           {
             for(i=0;i<n1;i++)
                {
                    m[m1++] =n[i];
                }
              m[m1]='\0';
            }                     
         if (c1 != 0 && d1 == 0)
           {
               for(i=0;i<n1;i++)
                {
                    if (c[0] == n[i])
                      if(c[1] == n[i+1])
                       {
                              
                         m[m1++] = c[2];
                         i++;
                         continue;
                       }  
                    
                    if (c[1] == n[i])
                      if(c[0] == n[i+1])
                        {
                         m[m1++] = c[2]; 
                         i++;
                         continue;
                        }
                   m[m1++] = n[i];          
                } 
             m[m1] ='\0'; 
           }
         other=-1;
		 if (c1 == 0 && d1 != 0 ) 
		  {
  			for(i=0;i<n1;i++){
		   if(d[0] == n[i] && other == -1)
					{
					   other=1;
					   first = i;
					}
					else if (d[1] == n[i] && other ==-1)
					 {
 						other=0;
 						first = i;
 					}
		  			if (d[other] == n[i])
					  second = i;
					if (first >= 0 && second >= 0 && n[first]!= n[second] )
					 {
					   n[second] = ' ';
					   m[0] = '\0';
					   m1=0;
					   first=-1;second=-1;other=-1;
					 }
					 else 
					  {		
		  				m[m1++] = n[i];
		  			
					  }
  		}
		  }
		  other = -1;    
        if (c1 != 0 && d1 != 0)
           {
               for(i=0;i<n1;i++)
                {
                	if (c[0] == n[i] && i !=0)
                      if(c[1] == n[i-1])
                       {
                         m1=m1-1;     
                         m[m1++] = c[2];
                         n[i]= ' ';  
						 if (flag == 1){
 				
						   first =-1;
						   	other = -1;
                            }   
                         continue;
                       }  
                    
                    if (c[1] == n[i] && i != 0)
                      if(c[0] == n[i-1])
                        {
                         m1=m1-1;
						 m[m1++] = c[2]; 
                         n[i]= ' ';
                           if (flag == 1)
                            {
                            	first =-1; 
                            	other = -1;
                            }
                         continue;
                        }
                   	flag=0;				
					if(d[0] == n[i] && other == -1)
					{
					   other=1;
					   first = i;
					   flag=1;
					   
					}
					else if (d[1] == n[i] && other ==-1)
					 {
 						other=0;
 						first = i;
 						flag=1;
 						  
 					}
		  			if (other != -1 && d[other] == n[i])
					  second = i;
					if (first >= 0 && second >= 0 && n[first]!= n[second] )
					 {
					   n[second] = ' ';
					   m[0] = '\0';
					   m1=0;
					   first=-1;second=-1;other=-1;
					 }
					 else 
					  {		
		  				m[m1++] = n[i];
		  			
					  }
                }
              m[m1] = '\0';  
           }
         final[0] = '[';
         k=1;
         for(i=0;i<m1;i++)
         {
                 final[k++] = m[i];
                 final[k++] = ',';
                 final[k++] = ' ';
                 }       
         if (m1 !=0)
         {
		 final[k-2]=']';
         final[k-1]='\0';       
         }
         else
          {
          	final[1] = ']';
          	final[2]='\0';
          }
         fprintf(fp1,"Case #%d: %s\n",cas++, final);
       
       }
  fclose(fp);
 fclose(fp1);
  return 0;
}       

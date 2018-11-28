#include<stdio.h>
#include<stdlib.h>
#include<string.h>
 
int main()
{
      int i=0,j=0,t,c=1,N=1,n,s,p,total=0,num=0,m=0;  
       
      FILE *stream,*stream2;
      stream=fopen("B-large.in","r");
      stream2=fopen("out2.txt","w");
       char buffer[1000],a1[10],a2[10],a3[10],temp[100];
      while(!feof(stream))
      {                     
                          
       if((fgets(buffer,sizeof(buffer),stream)!=NULL))
        {
            if(c==1)
            {   //1
                    
                    t=atoi(buffer);
                    c=0;
            }      //1 
            else
            {   
                if(N<=t)
               {   //5
                        total=0;
                        /*a1[0]=buffer[0];
                         a2[0]=buffer[2];
                         a3[0]=buffer[4];
                         a1[1]='\0';
                         a2[1]='\0';
                          a3[1]='\0'; 
                         n=atoi(a1);
                         s=atoi(a2);
                          p=atoi(a3); 
                         */
                         
                          for(i=0;buffer[i]!=' ';i++)
                   {  //4
                         if(buffer[i]!=' ')
                         { 
                                         a1[m++]=buffer[i];
                                         
                         }//2
                         //a1[m]='\0';
                         
                   }
                   i++;
                    a1[m]='\0'; 
                   m=0;
                      for(;buffer[i]!=' ';i++)
                   {  //4
                         if(buffer[i]!=' ')
                         { 
                                         a2[m++]=buffer[i];
                                         
                         }//2
                         //a2[m]='\0';
                   }  
                   a2[m]='\0'; 
                   m=0  ; 
                   i++;
                      for(;buffer[i]!=' ';i++)
                   {  //4
                         if(buffer[i]!=' ')
                         { 
                                         a3[m++]=buffer[i];
                                         
                         }//2
                      //   a3[m]='\0';
                   }   
                   a3[m]='\0';     
                    
                         n=atoi(a1);
                         s=atoi(a2);
                          p=atoi(a3);
                         
                         
                         i++;
                       j=0;  
                   for(;i<strlen(buffer);i++)
                   {  //4
                         if(buffer[i]!=' ' || buffer[i+1]=='\n')
                         {  //2                       
                         temp[j++]=buffer[i];
                         }//2
                         
                         if(buffer[i]==' ' || buffer[i]=='\n' || i==strlen(buffer)-1)
                         { //3
                         
                                         temp[j]='\0';
                                         j=0;
                                         num=atoi(temp);
                                     //  printf("%d\n",num);
                                         if(num>(p-1)*3)
                                         total++;
                                         else if((num==(p-1)*3) || (num==(p-1)*3-1) )
                                         {
                                              if(num>=p)
                                              {
                                                if(s!=0)
                                               {
                                                      s--;
                                                total++;
                                               } 
                                            }
                                              
                                         }
                                         
                         } //3
                                           
                    }    //for  //4 
                                               
                                          
                                              
                                               
                 
                   
                
                   fprintf(stream2,"Case #%d: ",N);
                   fprintf(stream2,"%d\n",total);
                   j++;
                   N++;
                       
              } //else
           else
           break;
                
                           
            }        
            
            }  
            
       }//while
   
   
   return 0;   
}
     
       

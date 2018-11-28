#include<stdio.h>

#include<stdlib.h>
#include<string.h>

char translate(char i)
{
     switch(i)
     {
              case 'a': return 'y';break;
              case 'b': return 'h';break;
              case 'c': return 'e';break;
              case 'd': return 's';break;
              case 'e': return 'o';break;
              case 'f': return 'c';break;
              case 'g': return 'v';break;
              case 'h': return 'x';break;
              case 'i': return 'd';break;
              case 'j': return 'u';break;
              case 'k': return 'i';break;
              case 'l': return 'g';break;
              case 'm': return 'l';break;
              case 'n': return 'b';break;
              case 'o': return 'k';break;
              case 'p': return 'r';break;
              case 'q': return 'z';break;
              case 'r': return 't';break;
              case 's': return 'n';break;
              case 't': return 'w';break;
              case 'u': return 'j';break;
              case 'v': return 'p';break;
              case 'w': return 'f';break;
              case 'x': return 'm';break;
              case 'y': return 'a';break;
              case 'z': return 'q';break;
              case ' ': return ' ';break;
              case '\n': return '\0';break;
     } 
}  
int main()
{
      int i=0,j=0,t,c=1,n=1;   
      FILE *stream,*stream2;
      stream=fopen("A-small-attempt1.in","r");
      stream2=fopen("out1.txt","w");
       char ans[102],buffer[102];
      while(!feof(stream))
      {
                          
       if((fgets(buffer,sizeof(buffer),stream)!=NULL))
        {
            if(c==1)
            {
                    
                    t=atoi(buffer);
                    c=0;
            }       
            else
            {   
                if(n<=t)
                {
                   for(i=0;i<strlen(buffer);i++)
                   { 
                                               
                                              
                                               ans[i]=translate(buffer[i]);
                                               
                   }
                   ans[i]='\0';
                
                   fprintf(stream2,"Case #%d: ",n);
                   fprintf(stream2,"%s\n",ans);
                   j++;
                   n++;
                       
                }  
                else
                break;
                
                           
            }        
            
        }   
            
      }
 return 0;
}
     
       

#include<stdio.h>
#include<conio.h>

int main()
{
        char seq[100],oinpos='N',binpos='N',cc;
        int c,t,sec=0,o[100],b[100],o1=-1,b1=-1,num,i=0,opos,bpos,cas=1;
        
        FILE *fp, *fp1;
        fp= fopen ("C:\\abc\\inp.txt","r");
        fp1=fopen("C:\\abc\\out.txt","w");
        
        fscanf(fp,"%d",&t);
        while(t--)
        {
              i=0;o1=-1;b1=-1,opos=1;bpos=1;
              fscanf(fp,"%d",&num);
              while(num--)
               {
                   fscanf(fp,"%c",&cc);
                   fscanf(fp,"%c",&cc);
                   seq[i]=cc;
                   if(cc == 'O')
                      {
                        ++o1; 
                        fscanf(fp,"%d",&o[o1]);
                      } 
                   else
                    {
                       ++b1;  
                       fscanf(fp,"%d",&b[b1]);
                     }  
               i++;
               }      
      seq[i]='N';
      o1=0;b1=0;i=0,sec=0;
      while(1)
       {
          
          if(seq[i] == 'N')
           break;
          sec++;  
             if(opos == o[o1])
                oinpos = 'Y';
             else if(opos > o[o1])
              opos--;
             else if(opos< o[o1])
               opos++;
          
          if(bpos == b[b1])
                binpos = 'Y';
          else if(bpos > b[b1])
              bpos--;
          else if(bpos < b[b1])
               bpos++;     
          
          if (seq[i] == 'O' && oinpos == 'Y')
           {
                     oinpos='N';
                     i++;
                     o1++;
                     continue;
           }
           if (seq[i] == 'B' && binpos == 'Y')
           {
                     binpos='N';
                     i++;
                     b1++;
                     continue;
           }
                     
         
       }         
       fprintf(fp1, "Case #%d: %d\n",cas,sec);
       cas++;
      
      
      }  
fclose(fp);
 fclose(fp1);
return 0;
}                   


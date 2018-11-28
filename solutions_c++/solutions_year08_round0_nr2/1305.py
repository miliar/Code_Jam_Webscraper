#include <fstream.h>
#include <iostream.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int compare(int  *arg1,   int   *arg2 )  
{
         return *arg1-*arg2;
}   

int inline getvalue(char timestr[])
{
    return ((timestr[0]-'0')*10+timestr[1]-'0')*60+(timestr[3]-'0')*10+timestr[4]-'0';    
}

int main()
{
//  freopen("OUTPUT.FIL","w",stdout);
 int allnum,casenum;
 int i,j,k,addtime,numa,numb;
 int ain[100],bin[100],aout[100],bout[100],cnta,cntb,tmp; 
 char buffer[100];
 freopen("b.in","r",stdin);
 //fstream fin("A-large.in");
 
 cin>>allnum;
 for(casenum=1;casenum<=allnum;casenum++)
 {
   cin>>addtime>>numa>>numb;
   for(i=0;i<numa;i++)
   {
     cin>>buffer;
     ain[i] = getvalue(buffer);
     cin>>buffer;
     aout[i] = getvalue(buffer);                    
   }
   for(i=0;i<numb;i++)
   {
     cin>>buffer;
     bin[i] = getvalue(buffer);
     cin>>buffer;
     bout[i] = getvalue(buffer);                    
   }
   cnta = numa;
   cntb = numb;
   qsort((void *)ain,numa,sizeof(int),(int(*)(const void*, const   void*))compare);
   qsort((void *)aout,numa,sizeof(int),(int(*)(const void*, const   void*))compare);
   qsort((void *)bin,numb,sizeof(int),(int(*)(const void*, const   void*))compare);
   qsort((void *)bout,numb,sizeof(int),(int(*)(const void*, const   void*))compare);

   i=0;
   j=0;
   while(i<numa)
   {
       if(j>=numb)
            break;
       tmp = aout[i]+addtime;
       if(tmp<=bin[j])
       {
            cntb--;
            i++;
            j++;    
       }        
       else
           j++;                     
   }
   
   i=0;
   j=0;
   while(i<numb)
   {
       if(j>=numa)
            break;
       tmp = bout[i]+addtime;
       if(tmp<=ain[j])
       {
            cnta--;
            i++;
            j++;    
       }        
       else
           j++;                     
   }
   
   printf("Case #%d: %d %d\n",casenum,cnta,cntb);
   
 }

}

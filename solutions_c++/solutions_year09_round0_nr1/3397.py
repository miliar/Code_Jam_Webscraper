#include<iostream>
#include<cstdio>
#include<string>

using namespace std;

int main()
{
   char str[29][11],tstr[29][300],temp[11],ch;
   int l,d,n,k,j,found,i,ctr[12]={0},cpy,test_case;
   scanf("%d%d%d",&l,&d,&n);
   for(int m=0;m<=d;m++){
   gets(temp); 
  // cout<<m; 
   for( cpy=0;temp[cpy]!='\0';cpy++)
   str[m][cpy]=temp[cpy];
   
   str[m][cpy]='\0';
         }
      //   for(int m=0;m<=d;m++){
   //cout<<str[m]; 
//}

   
  // cout<<m; 
  for(int m=0;m<n;m++){
   gets(temp); 
  // cout<<m; 
   for( cpy=0;temp[cpy]!='\0';cpy++)
   tstr[m][cpy]=temp[cpy];
   
   tstr[m][cpy]='\0';
         }

    i=0;
   k=0;
   test_case=0;
   while(test_case<n)
   {
            ctr[test_case]=0;
         k=0;            
   while(k<d)
   {
             found=1;
             j=0;i=0;
   while(tstr[test_case][i]!='\0'&&j<l)
   {      
         if(tstr[test_case][i]=='(')
         {
         i++;
         
             while(tstr[test_case][i]!=')')
             {
             if (tstr[test_case][i]==str[k][j])
                  {
                           found=2;
                               
                  }                   
                                
                 i++;                   
             }
             
             if(found==2)
             found=1;
             else
             {
             found=0;
             break;
             }
             
             
             
                                
         } 
         
         else 
         {
             if(tstr[test_case][i]!=str[k][j])
             {
             found=0;
             break;
             }
             
         }
         
                     
                       
     i++; 
     j++;                 
   }
   if(found==1)
    ctr[test_case]+=1;
    
    k++;
   }
   
   
   
   
   
   test_case++; 
   }
   for(int i=0;i<n;i++)
   cout<<"\nCase #"<<i+1<<":  "<<ctr[i];
   
cin>>ch;

     return 0;
 }

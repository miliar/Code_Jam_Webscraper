#include<iostream>
#include<stdio.h>
#include<algorithm>
#include<iostream>
#include<string.h>
#include<stdlib.h>
using namespace std;
unsigned long long power(unsigned long long a, unsigned long long b)
{
unsigned long long i,temp=1;
for(i=1;i<=b;i++)
temp=temp*a;
return temp;
}

void reversestr( char str[],int len){
    char *tempstr;int i,j,count=0;
    tempstr=(char *)malloc(sizeof(char)*(len+1));
    for(i=len-1,j=0;i>=0;i--,count++,j++)    tempstr[j]=str[i];
    tempstr[count]='\0';
    for(i=0;i<=count;i++)    str[i]=tempstr[i];
    free(tempstr);
}

//  12345
// 00123     
//
unsigned long long convert_to_decimal(int b,char *result){
     unsigned long long ans=0,c=0;
     int i,l=strlen(result);
     for(i=l-1;i>=0;i--)
               ans+=((unsigned long long)((int)result[i]-48))*(unsigned long long)power((unsigned long long)b,c++);                 
    return ans;

}


unsigned long long sum_modulus_base(unsigned long long b, char *n1, char *n2){
      int d,temp,f,s,i,l1=strlen(n1),l2=strlen(n2),maxlen=l1>l2?l1:l2;
      char *result=new char[100];
      if(l1>l2)
      {
            d=l1-l2;
            for(i=l2;i>=0;i--)
                n2[i+d]=n2[i];
            for(i=0;i<d;i++)
                 n2[i]=48;
      }
      else if(l2>l1){
           d=l2-l1;
            for(i=l1;i>=0;i--)
                n1[i+d]=n1[i];
            for(i=0;i<d;i++)
                 n1[i]=48;
      }                  
     // cout<<n1<<" "<<n2<<endl;
      for(i=maxlen-1;i>=0;i--){
                  f=(int)n1[i]-48;
                  s=(int)n2[i]-48;             
                  temp=f+s;
                  
                  //carry=temp/b;
                  temp%=b;
                  result[i]=temp+48;
                  
                  l1--; l2--;          
      }
      result[maxlen]='\0';
     // cout<<result<<endl;
     return convert_to_decimal(b,result);
     // return result;
}

char* convert_to_base(unsigned long long b, unsigned long long num){
      char *num1=new char[100];
       //123 base 5
       int i=0;
       while(num>0)
       {
            num1[i++]=(char)(num%b+48);
            num/=b;
       }
       num1[i]='\0';                  
      reversestr(num1,i);
      return num1;
      
}

unsigned long long arr[1000],sum[1000][1000],b=2,ans;
char *num1=new char[100],*num2=new char[100];
int t,n,i,k,l,m,j;
       

int main(){
   scanf("%d",&t);
   for(k=1;k<=t;k++){
           ans=0;          
          scanf("%d",&n);
          for(i=0;i<n;i++)
              scanf("%d",&arr[i]);
          sort(arr,arr+n);
          
          for(i=0;i<n;i++){   
             for(j=i;j<n;j++)
              {
                  unsigned long long x;
                  if(j-1>=0)
                    x=sum[i][j-1];
                   else 
                     x=0;
                                
                  num1=convert_to_base(b,x);
                  num2=convert_to_base(b,arr[j]);
                  
                             
                  sum[i][j]=sum_modulus_base(b,num1,num2);    
                  //printf("sum[%d][%d]=%ull\n",i,j,sum[i][j]);         
                               
              }            
           }     
           
           for(i=0;i<n;i++)
           {
               if(sum[0][i]==sum[i+1][n-1])
                   break;                
           }             
         
           printf("Case #%d: ",k); 
         
         
           if(i==n)
               goto failed;
           
           for(i=i+1;i<n;i++)
               ans+=arr[i];  
                   
          /*cin>>n1>>n2;
          num1=convert_to_base(b,n1);
          num2=convert_to_base(b,n2);
         // cout<<num1<<" "<<num2<<endl;
          cout<<sum_modulus_base(b,num1,num2)<<endl;
    
          */
         printf("%llu\n",ans); 
         continue;
         failed:
         printf("NO\n");
    }              
    return 0;
}


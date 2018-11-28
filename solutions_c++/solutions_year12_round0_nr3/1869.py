#include<iostream>
using namespace std;

int main()
{
    int t,k=1,cnt,j,count,cnt2;
    
    long int num1,i,A,B,num,dig,tot,num2;
    
    cin>>t;
    while(t--)
    {
              cin>>A>>B;
              tot=0;
              
              for(i=A;i<B;i++)
              {
                               num1 = i;
                               cnt = 0;
                               count = 0;
                               num = i;
                               while(num1)
                               {
                                          num1/=10;
                                          cnt++;
                               }
                               
                               for(j=0;j<cnt;j++)
                               {
                                                 dig = num%10;
                                                 
                                                 if(dig)
                                                 {
                                                        num1 = num/10;
                                                        while(num1)
                                                        {
                                                                   num1/=10;
                                                                   dig*=10;
                                                        }
                                                        dig+=num/10;
                                                        num=dig;
                                                        if(num<=B && num>i)
                                                        count++;
                                                        if(num==i)
                                                        break;
                                                 }
                                                 else
                                                 {
                                                     num1=num;
                                                     cnt2=0;
                                                     while(num1%10==0)
                                                     {
                                                      num1/=10;
                                                      cnt2++;                
                                                     }
                                                     
                                                     dig = num1%10;
                                                     num1/=10;
                                                     
                                                     while(cnt2--)
                                                     {
                                                      dig*=10;
                                                     }
                                                     
                                                     num2=num1;
                                                     while(num2)
                                                     {
                                                      num2/=10;
                                                      dig*=10;
                                                     }
                                                     
                                                     dig += num1;
                                                     num = dig;
                                                     
                                                     if(num<=B && num>i)
                                                     count++;
                                                     if(num==i)
                                                     break;
                                                 }
                               }
                               
                               tot += count;
              }
              
              cout<<"Case #"<<k++<<": "<<tot<<'\n';
    }
    
    return(0);
}

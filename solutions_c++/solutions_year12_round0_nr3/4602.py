#include<iostream>

using namespace std;

int main()
{int t,count=1,i,a,b,arr[3],num1,num2,c,k,temp;

     cin>>t;
   
    while(count<=t)
    {  
        c=0; 
          
       cin>>a>>b;
       
        for(i=a;i<=b;i++)
        {k=0; 
        num1=0;
        num2=0; 
        temp=i;
          while(temp!=0)
            { arr[k]=temp%10;
              temp=temp/10;            
             k++;
            } 
            if(k==2)
           {num1=arr[0]*10+arr[1];
               if((num1>i)&&(num1<=b))
                 c++;
           }
            else
            { if(k==3)
                 { num1=arr[0]*100+arr[2]*10+arr[1];
                   num2=arr[1]*100+arr[0]*10+arr[2];      
                  if((num1>i)&&(num1<=b))
                     c++;
                  if((num2>i)&&(num2<=b))
                      c++;                         
                  }
              else
                 c=0;
             } 
           }               
                      cout<<"Case #"<<count<<": "<<c<<"\n";
               
           count++;
           }      
   return 0;
}                                               

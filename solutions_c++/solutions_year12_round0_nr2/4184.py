#include<iostream>
using namespace std;
int main()
  {
  int t, s, p , n ,count,count2, temp ,i,diff;
 int num=1;
   cin>>t;
   while(t--)
   {
             int  a[101]={0};
             cin>>n>>s>>p;
             count= count2=0;temp=diff=0;
             for(i=0;i<n;i++)
             cin>>a[i];
              temp = 3*p;
              
              for(i=0;i<n;i++)
               {
                if(a[i]<p)
                continue;
                                 diff=abs(temp-a[i]);             
                if(a[i]>temp)
                count++;
                if(a[i]<= temp && diff<=2)
                 count ++;
                 else if((a[i]<temp) && (diff <5 && diff >2) &&  (count2<s))
                 count2++;
              
               /* if((a[i]>temp) && (diff <7 && diff >2) )
                 {count2++;cout<< "for" <<a[i]<<endl;}
                else if((a[i]<temp) && (diff <5 && diff >2) &&  (count2<s))
                  {count2++;cout<< "for" <<a[i]<<endl;}
                 //else  if((a[i]<temp) && (diff >2 && diff<5)  && (count2<s))
                   //count2++;
                 if(diff<=2)
                    count++;
                    
                    */
                }
                
                cout<<"Case #"<<num++<<": "<<count+count2<<endl;
              
             }
   //system("pause");
     return 0;
}

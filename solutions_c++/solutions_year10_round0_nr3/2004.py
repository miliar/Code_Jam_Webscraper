#include<iostream>
//#include<conio.h>

using namespace std;

int main()
{
    int tc;
    int r,k,n;
    
    int counter =0;
    cin>>tc;
    
    while(counter<tc)
    {
               cin>>r>>k>>n;
               int g[n];
               long long int tot_arrsum =0;
               for(int i=0;i<n;i++)
               {
                       cin>>g[i];
                       tot_arrsum += g[i];
               }
               long long int tot_euros =0;
               int rinitial =0;
               int sum = 0;
               int i =0;
               while(rinitial <r)
               {  
                  if(tot_arrsum < k)
                  sum = tot_arrsum;
                  else
                  {
			
                           do
                           {
                                      sum += g[i];
                                      i++;
                                      if(i == n)
                                      i=0;
                           }while(sum+g[i]<=k);
                  }              
                     //cout<<"Sum added "<<sum<<"\n";
                     tot_euros += sum;
                     sum=0;
                     rinitial++;
               }
               cout<<"Case #"<<counter+1<<": "<<tot_euros<<"\n";
               counter++;
    }
    //getch();
}           

#include<iostream>
#include<fstream>

using namespace std;
int main()
{
    int cases,no_groups,rides,max,euro,i,k;
     int group[10]; 
    
 euro=0;
     ifstream newin("c.in");
    ofstream newout("C-smallout.txt");
   newin>>cases;
    for(i=1;i<=cases;i++)
    {
    euro=0;
     newin>>rides;
     newin>>max;
     cout<<cases;
    
     newin>>no_groups;
int max_sum=0;
                  
     for(k=0;k<no_groups;k++)
            {
             newin>>group[k];
             max_sum=max_sum+group[k];
              }
              
              int sum,a=0;
     while(rides>0)
     {
     sum=0;
     while(sum<=max && sum<=max_sum)
     {
     sum=sum+group[a];   
      a++;          
      a=a%no_groups; 
     }
     a=(a+no_groups-1)%no_groups;
     sum=sum-group[a];
     euro=euro+sum;
     rides--;               
    
      }
     
    
    newout<<"Case #"<<i<<": "<<euro<<endl;
}
newin.close();
newout.close();
cin.get();
}

#include <fstream>
#include <iostream>
#include <string>
#include <algorithm>

using namespace std;
int t, n, s, p;
int main ()
{
    freopen("B-large.in","r",stdin);   
    freopen("B-large.out","w",stdout);
    cin>>t;
    
    for (int i=1;i<=t;++i)
    {
        cout<<"Case #"<<i<<": ";
        
        cin>>n>>s>>p;
        //N is the number of dancers
        //S is the number of surprising scores
        //P is the minimum Max score to count.
        int count = 0;
        int total,indiv;
        
        //Greedy should work (let the first dancer who needs to be a surprise be 1 - it results in at most 1 loss later anyway)
        for (int j=0;j<n;j++)
        {
                cin>>total;
                indiv = total/3;
                if (3*indiv==total)
                {
                   if (indiv>=p)
                      count++;
                   else if (indiv==p-1 & s>0)
                   {
                        if (indiv!=0 & indiv!=10)
                        {
                                     s--;
                                     count++;     
                        }
                   }                 
                }
                else if (3*indiv+1==total)
                {
                     if (indiv+1>=p)
                        count++;
                }
                else
                {
                    if (indiv+1>=p)
                         count++;
                    else if (s>0 & indiv+2>=p & indiv+2<11)
                    {
                       count++;
                       s--;        
                    }
                }
        }
                
        cout<<count<<"\n";         
    }
    return 0;   
}

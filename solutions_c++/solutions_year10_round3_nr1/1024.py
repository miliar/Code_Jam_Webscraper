
# include <iostream>
# include <vector>

using namespace std;

bool comp(pair<int, int> p1, pair<int, int> p2)
{
    return p1.first<p2.first;
}

int main()
{
    int t, cnt=0;
    cin>>t;
    while(t--)
    {
         int n,i,j,intr=0;
         vector < pair<int,int> > ar1(1000);
         cin>>n;
         for(i=0;i<n;i++)
         {
              cin>>ar1[i].first>>ar1[i].second;                
         }
         sort(ar1.begin(),ar1.begin()+n, comp); 
         /*for(i=0;i<n;i++)
           {
               cout<<ar1[i].first<<" "<<ar1[i].second<<endl;              
           }*/
         for(i=0;i<n;i++)
         {
              for(j=i+1;j<n;j++)
               {
                   if(ar1[i].second > ar1[j].second)
                       intr++;                 
               }                
         }  
         cout<<"Case #"<<++cnt<<": "<<intr<<endl;       
    }    
}

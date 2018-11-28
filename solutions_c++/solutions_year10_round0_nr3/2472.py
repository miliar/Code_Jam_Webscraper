#include<iostream>
#include<deque>
#include<fstream>
#define cin fin
#define cout fout
using namespace std;
int main()
{
   ifstream fin("C-small-attempt0.in");
   ofstream fout("C.out");
   int t;
   cin>>t;
   for(int count=1;count<=t;count++)
   {
      int r,k,n;
      cin>>r>>k>>n;
      int temp;
      deque<int> line;
      for(int i=0;i<n;i++)
      {
         cin>>temp;
         line.push_back(temp);
      }
      int ans=0;
      for(int i=0;i<r;i++)
      {
         int sum=0,pop[2000],l=0;
         while(!line.empty() && sum+line.front()<=k)
         {
            sum+=line.front();
            pop[l++]=line.front();
            line.pop_front();
         }
         ans+=sum;
         for(int j=0;j<l;j++)
            line.push_back(pop[j]);
      }
      cout<<"Case #"<<count<<": "<<ans<<endl;
   }
   system("pause");
}
            

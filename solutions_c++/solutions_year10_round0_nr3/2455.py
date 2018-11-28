#include<iostream>
#include<vector>

using namespace std;

int main()
{
     int t,r,k,n,i,j,a,c,cost=0,count=0;
     vector<int> v;
     cin>>t;
     for(i=1;i<=t;i++)
     {
          cin>>r>>k>>n;
          cost=0;
          c=0;
          count=0;
          v.clear();
          for(j=0;j<n;j++)
          {
               cin>>a;
               v.push_back(a);
          }
          j=0;
          while(r)
          {
               if((c+v[j])>k || count==n)
               {
                    r--;
                    cost+=c;
                    c=0;
                    count=0;
               }
               else
               {
                    c+=v[j];
                    j++;
                    if(j>=n) j=0;
                    count++;
               }
          }
          cout<<"Case #"<<i<<": "<<cost<<"\n";
     }
     //system("pause");
     return 0;
}

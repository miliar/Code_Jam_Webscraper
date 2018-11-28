#include<iostream>
#include<string>
using namespace std;
main()
{
      long long int n,i;
      cin>>n;
      string a,p,s;
      for(i=0;i<n;i++)
      {
              cin>>a;
              p=a;
              next_permutation(a.begin(),a.end());
              if(a<=p)
              {
                        a="0"+p;
                        next_permutation(a.begin(),a.end());
                        }
                        cout<<"Case #"<<i+1<<": "<<a<<endl;
            }
}
              
      


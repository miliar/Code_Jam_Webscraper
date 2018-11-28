#include<iostream>
#include<string>
using namespace std;
int main()
{
    string s,s1;
    int t;
    int k=1;
    cin>>t;
    while(t>0)
    {
       cin>>s;
       s1=s;
       next_permutation(s.begin(),s.end());
       if(s<=s1)
          {s="0"+s1;
           next_permutation(s.begin(),s.end());
           cout<<"Case #"<<k<<": "<<s<<endl;
           }
      else
         cout<<"Case #"<<k<<": "<<s<<endl;
         k++;
         t--;
    }
    return 0;
}

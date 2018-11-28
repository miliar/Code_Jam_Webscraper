#include<iostream>
using namespace std;
int main()
{
    int n;
    string str,s;
    cin>>n;
    for(int i=0;i<n;i++)
    {
      cin>>str;
      s=str;
      next_permutation(str.begin(),str.end());
      if(str<=s)
      {
        s="0"+s;
        next_permutation(s.begin(),s.end());
        str=s;
        }
      cout<<"Case #"<<i+1<<": "<<str<<endl;
    }
    return 0;
}

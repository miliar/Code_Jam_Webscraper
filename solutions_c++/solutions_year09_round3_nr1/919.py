#include<iostream>
#include<cstdio>
#include<map>
#include<string>
using namespace std;
int c[]={1,0,2,3,4,5,6,7,8,9};
main()
{
    freopen("A-small-attempt1.in","r",stdin);
    freopen("out.txt","w+",stdout);
    int n;
    cin>>n;
    for(int k=1;k<=n;k++)
    {
      string s;
      cin>>s;
      map<char,int> mp;
      int inc=0;
      for(int i=0;i<s.size();i++)
      {
        if(mp.find(s[i])==mp.end())
        {
          mp.insert(pair<char,int>(s[i],c[inc++]));
        }
      }
      int base=mp.size();
      if(base==1)base++;
      //cout<<base<<endl;
      long long int res=0;
      for(int i=0;i<s.size();i++)
      {
         int t=mp.find(s[i])->second;
         res=res*base+t;
      }
      printf("Case #%d: %I64d\n",k,res);
    }
    return 0;
}

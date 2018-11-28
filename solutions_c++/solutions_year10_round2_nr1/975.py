#include<iostream>
#include<fstream>
#define cin fin
#define cout fout
using namespace std;
int main()
{
   ifstream fin("A-large.in");
   ofstream fout("A-large.out");
   int t;
   cin>>t;
   for(int count=1;count<=t;count++)
   {
      int n,m;
      cin>>n>>m;
      string dir[10000];
      for(int i=0;i<n;i++)
         cin>>dir[i];
      int ans=0;
      string s;
      for(int i=0;i<m;i++)
      {
         cin>>s;
         int sum=0;
         bool check=true,find=false;
         for(int j=s.size()-1;j>=0;j--)
         {
            if(check)
            {
               for(int k=0;k<n;k++)
                  if(s==dir[k])
                  {
                     find=true;
                     break;
                  }
               dir[n++]=s;
            }
            if(find)break;
            if(s[j]=='/')
            {
               check=true;
               sum++;
            }
            else check=false;
            s.assign(s,0,s.size()-1);
         }
         ans+=sum;
      }
      cout<<"Case #"<<count<<": "<<ans<<endl;
   }
   system("pause");
   return 0;
}
      

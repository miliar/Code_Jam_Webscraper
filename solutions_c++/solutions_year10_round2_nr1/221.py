#include <iostream>
#include <set>
using namespace std;
set<string> st;
string s;
int i,n,m,it,t,k;
int sheqmna(string s)
{
int k=0;
string a="";
for(int i=0;i<s.size();i++)
   {
   a+=s[i];
   if(i+1==s.size()||s[i+1]=='/')
      if(!st.count(a))
         {
         k++;
         st.insert(a);
         }
   }
return k;
}
int main()
{
freopen("A-large.in","r",stdin);
freopen("A-large.out","w",stdout);
cin>>t;
for(it=1;it<=t;it++)
   {
   st.clear();
   st.insert("");
   printf("Case #%d: ",it);
   cin>>n>>m;
   for(i=0;i<n;i++)
      {
      cin>>s;
      sheqmna(s);
      }
   for(k=i=0;i<m;i++)
      {
      cin>>s;
      k+=sheqmna(s);
      }
   printf("%d\n",k);
   }
return 0;
}

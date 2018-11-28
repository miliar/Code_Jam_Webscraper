#include<iostream>
#include<vector>
#include<algorithm>
#include<string>
#include<map>
using namespace std;

int main()
{
       int T;
       cin >> T;
       int cc =1;
       while(T--){
               string s;
               cin>>s;
               map<char,long long int> m;
               int i,j =2;
               int len=s.size();
               bool b=true;
               m[s[0]]=1;
               char c=s[0];
               for(i=1;i<len;i++){
                       if(s[i]==c)continue;
                       if(b){m[s[i]]=0;b=false;}
                       else if(m.count(s[i])>0) continue;
                       else m[s[i]]=j++;
               }
               int siz=m.size();
               siz>?=2;
               long long int ans=0;
               long long int df = 1;
               for(i=len-1;i>=0;i--)
               {
                       ans+=m[s[i]]*df;
                       df*=siz;
               }
               cout<<"Case #"<<cc<<": "<<ans<<endl;
               ++cc;
       }

}
 
 

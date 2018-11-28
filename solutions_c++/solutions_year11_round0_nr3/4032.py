#include<fstream>
#include<algorithm>
#include<string>
using namespace std;
ifstream cin("C.in");
ofstream cout("C.out");
int N;
int lst[1010];
string binary[1010];
string tobin(int x)
{
   string ret="";
   while(x)
   {
       if(x%2)ret+="1";
       else ret+="0";
       x=x/2;
   }
   return ret;
}
string add(string x,string y)
{
       string ret="";
       for(int i=0;i<min(x.size(),y.size());i++)
       {
           if(x[i]=='1'&&y[i]=='1')
           ret+="0";
           else
           if(x[i]=='0'&&y[i]=='0')
           ret+="0";
           else
           ret+="1";
       }
       if(x.size()<y.size())
       {
           ret+=y.substr(x.size(),y.size()-x.size());
       }
       if(x.size()>y.size())
       {
           ret+=x.substr(y.size(),x.size()-y.size());
       }
       return ret;
}
bool cmpP(string s1,string s2)
{
    for(int i=0;i<min(s1.size(),s2.size());i++)
    if(s1[i]!=s2[i])return 0;
    if(s1.size()<s2.size())
    for(int i=s1.size();i<s2.size();i++)
    if(s2[i]=='1')return 0;
    if(s1.size()>s2.size())
    for(int i=s2.size();i<s1.size();i++)
    if(s1[i]=='1')return 0;
    bool ok=0;
    for(int i=0;i<s1.size();i++)
    if(s1[i]=='1'){ok=1;break;}
    if(!ok)
    return 0;
    return 1;
}
long long part(int ind,string p1,string p2)
{
    string x1=p1,x2=p2;
    if(ind==N&&!cmpP(p1,p2))return -(1<<30);
    if(ind==N)return 0;
    string np1=add(p1,binary[ind]),np2=add(p2,binary[ind]);
    int o1,o2;
    o2=part(ind+1,p1,np2)+lst[ind];
    o1=part(ind+1,np1,p2);
    int res=max(o1,o2);
    return res;
}
int main()
{
    int T;
    cin>>T;
    for(int k=1;k<=T;k++)
    {
        cin>>N;
        for(int i=0;i<N;i++)
        {
           cin>>lst[i];
           binary[i]=tobin(lst[i]);
        }
        //cout<<add("101","110")<<endl;
        long long res=part(0,"0","0");
        if(res<=0)
        cout<<"Case #"<<k<<": NO"<<endl;
        else
        cout<<"Case #"<<k<<": "<<res<<endl;
    }
    return 0;
}

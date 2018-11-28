#include<fstream>
#include<iostream>
#include<string>
#include<algorithm>
using namespace std;
int same(string &s1,string &s2)
{
    int i,t=-1;
    for(i=0;i<s1.length();i++)
    {
        if(s1[i]!=s2[i])return t;
        if(s1[i]=='/' && s2[i]=='/')t++;
    }    
    return t;
}    
main()
{
    int t,n,m,i,j,k;
    
    int max;
    
    ifstream in("a.txt");
    ofstream out("a.out");
    string s1[200],s;
    int temp;
    int ans;
    in>>t;
    for(int tt=1;tt<=t;tt++)
    {
        in>>n>>m;
        ans=0;
        for(i=0;i<n;i++)
        {
            in>>s1[i];            
            s1[i]+='/';            
        }    
        for(j=0;j<m;j++)
        {
            int mp;
            in>>s;
            s+='/';           
            max=0;
            mp=-1;
            for(i=0;i<n;i++)
            {
                temp=same(s,s1[i]);
                if(temp>max)
                {
                    max=temp;
                    mp=i;
                }    
            }   
            for(temp=k=0;k<s.length();k++)if(s[k]=='/')temp++; 
            temp--;
            if(mp!=-1)ans+=temp-max;else ans+=temp;
            s1[n++]=s;
        }    
        out<<"Case #"<<tt<<": "<<ans<<endl;
    }    
}    

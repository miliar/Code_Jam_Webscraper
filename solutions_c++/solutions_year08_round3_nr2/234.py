#include<iostream>
#include<fstream>
#include<cstdio>
#include<vector>
#include<algorithm>
#include<string>
#include<math.h>
#define Q 100001
using namespace std;
long long sum;
void dfs(string s,long long n)
{
    //cout<<"   "<<s<<" "<<n<<endl;
    if(s.size()==0)
    {
        if(n%2==0||n%3==0||n%5==0||n%7==0)
        sum++;
        return ;
    }
    long long m=0;
    for(int i=0;i<s.size();i++)
    {
        m=m*10+s[i]-'0';
        //cout<<"  "<<m<<" "<<s[i]<<endl;
        string str=s.substr(i+1,s.size());
        //cout<<" "<<str<<endl;
        dfs(str,n+m);
        dfs(str,n-m);
    }
}
int main()
{
    freopen("B-small-attempt2.in","r",stdin);freopen("out.txt","w",stdout);
    int N;
    scanf("%d",&N);
    for(int i=0;i<N;i++)
    {
       string str;
       cin>>str;
       //cout<<" "<<str<<endl;
       sum=0;
       long long m=0;
       for(int j=0;j<str.size();j++)
       {
           m=m*10+str[j]-'0';
           dfs(str.substr(j+1,str.size()),m);
       }
       printf("Case #%d: %lld\n",i+1,sum);
    }
}

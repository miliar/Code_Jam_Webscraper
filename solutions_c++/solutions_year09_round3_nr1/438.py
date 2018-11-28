#include <iostream>
#include <vector>
#include <memory.h>
#include <math.h>
using namespace std;
long long exp(int a,int b)
{
    if (b==0)return 1;
    if (b%2)return a*exp(a,b-1);
    long long t=exp(a,b/2);
    return t*t;
}

int main()
{
    freopen("A-large.in","r",stdin);

   freopen("A-large.out","w",stdout);
    int t,g=1;
    cin>>t;
    for (int n=1;n<=t;++n)
    {
        string str;
        cin>>str;
        int size=str.size();
        int chars[256];
        memset(chars,0,sizeof(chars));
        int count=0;
        for (int b=0;b<size;++b)
        {
            if (chars[str[b]]==0)
            {
                count++;
                chars[str[b]]++;
            }
        }
        bool covered[256];
        memset(chars,0,sizeof(chars));
        memset(covered,0,sizeof(covered));

        chars[str[0]]=1;
        covered[str[0]]=1;
        int curr=0;
        for (int b=1;b<size;++b)
        {
            if (curr==1)
            {
                curr=2;
            }
            if (!covered[str[b]])
            {
                chars[str[b]]=curr;
           // cout<<str[b]<<" "<<curr<<endl;
                curr++;
                covered[str[b]]=1;
            }

        }
        if(count==1){++count;}
        unsigned long long val=0;
        for (int b=size-1;b>=0;--b)
        {
            val+=(unsigned long long)chars[str[b]]*exp(count,(size-1-b));
        }
        cout<<"Case #"<<g<<": "<<val<<endl;
        g++;
    }

}

#include <iostream>
#include <algorithm>
#include <string>
#include <vector>
#include <cstdio>

#include <map>
using namespace std;
int main()
{
    int t;
    cin>>t;
    for(int i=1;i<=t;i++)
    {
        string inp;
        cin>>inp;
        long int n=0;
        map<char,int> num;
        for(int j=0;j<inp.size();j++)
        {
                if(num.find(inp[j])==num.end()){
                        if(n==1)
                            num[inp[j]]=0;
                        else
                            num[inp[j]]=n?n:n+1;
                        n++;
                }
        }
/*
        map<char,int>::iterator it;

        for ( it=num.begin() ; it != num.end(); it++ )
    cout << (*it).first << " => " << (*it).second << endl;

        cout<<"DEBUG:n="<<n<<inp[inp.size()-1]<<endl;*/
        unsigned long long ans=0,factor=1;
        if (n==1) n++;
        for(int j=inp.size()-1;j>=0;j--){
            ans+=num[inp[j]]*factor;
            factor*=n;
        }

        cout<<"Case #"<<i<<": "<<ans<<endl;
    }
    return 0;
}

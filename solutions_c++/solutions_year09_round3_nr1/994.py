/*
OS: Microsoft Windows XP Professional
Compiler: Bloodshed Dev-C++ 4.9.9.2
*/
#include <iostream>
#include <string>
using namespace std;
int main()
{
    freopen("ayb.in", "r", stdin);
    freopen("ayb.out", "w", stdout);
    string num, num2;
    int kind;
    int mark[130]={0};
    int count=0;
    int i, k;
    int t;
    long long pow[70], ans;
    
    cin>>t;
    for (k=1; k<=t; k++)
    {
        for (i=0; i<130; i++)
             mark[i]=-1;
        count=0;
        cin>>num;
        mark[num[0]]=1;
        num2[0]=1+'0';
        for (i=1; i<num.length(); i++)
        {
            if (mark[num[i]]==-1)
            {
                mark[num[i]]=count;
                if (count==0)
                    count=2;
                else
                    count++;
            }
            num2[i]=mark[num[i]]+'0';
        }
        if (count==0)
            count=2;
        pow[0]=1;
        for (i=1; i<num.length(); i++)
            pow[i]=pow[i-1]*count;
        ans=0;
        for (i=0; i<num.length(); i++)
            ans+=(num2[i]-'0')*pow[num.length()-1-i];
        cout<<"Case #"<<k<<": "<<ans<<endl;
    }
    fclose(stdin);
    fclose(stdout);   
    return 0;
}

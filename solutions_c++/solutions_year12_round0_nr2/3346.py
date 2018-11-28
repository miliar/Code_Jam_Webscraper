#include<iostream>
using namespace std;
int main()
{
    int n;
    cin>>n;
    int h=1;
    while(n--)
    {
        int N,s,p;
        cin>>N>>s>>p;
        int t[N];
        for(int i=0;i<N;i++)
        cin>>t[i];
        int c=0;
        int ct=0;
        for(int i=0;i<N;i++)
        {
            if(t[i]%3==0 && t[i]!=0)
            {
                if((t[i]/3)>=p)
                ct++;
                else
                {
                    if(((t[i]/3)+1)>=p && c<s)
                    {
                        ct++;
                        c++;
                    }
                }
            }
            else if(t[i]%3==1)
            {
                if((((t[i]-1)/3)+1)>=p)
                ct++;
            }
            else if(t[i]%3==2)
            {
                if(((t[i]+1)/3)>=p)
                ct++;
                else if((((t[i]+1)/3)+1)>=p && c<s)
                {
                    ct++;
                    c++;
                }
            }
            if(p==0)
            ct=N;
        }
        cout<<"Case #"<<h++<<": "<<ct<<endl;

    }
    return 0;
}

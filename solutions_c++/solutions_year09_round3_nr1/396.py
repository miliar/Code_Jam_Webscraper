#include<iostream>
#include<cmath>

#define forn(i,n) for(int i=0;i<n;i++)

using namespace std;

int main()
{
    int T;
    cin>>T;
    string s;
    int chk[36];
    int eq[36];
    int ct;
    int chk1[36];
    long long res,m;
    int base;
    int u=T;
    while(T--)
    {
             cin>>s;
             forn(i,36)
             {
                    chk[i]=0;
                    eq[i]=-1;
                    chk1[i]=0;
             }
             forn(i,s.length())
             {
                if(s[i]>='a'&&s[i]<='z')
                {
                    chk[s[i]-97]=1;
                }
                else
                {
                    chk[s[i]-'0'+26]=1;
                }
             }
             base=0;
             forn(i,36)
             {
                if(chk[i]==1)
                	base++;
             }
             if(base==1)
               base++;
             ct=1;
             if(s.length()==1)
             {
                cout<<"Case #"<<u-T<<": "<<"1"<<endl;
                continue;
             }
             forn(i,s.length())
             {
                if(s[i]>='a'&&s[i]<='z')
                {
                    if(chk1[s[i]-97])
                        continue;
                    eq[s[i]-97]=ct;
                    chk1[s[i]-97]=1;
                }
                else
                {
                    if(chk1[s[i]-'0'+26])
                        continue;
                    eq[s[i]-'0'+26]=ct;
                    chk1[s[i]-'0'+26]=1;
                }
                if(ct==1)
                {
                    ct=0;
                    continue;
                }
                if(ct==0)
                {
                    ct=2;
                    continue;
                }
                ct++;
             }
             res=0;
             m=1;
             for(int i=s.length()-1;i>=0;i--)
             {
					if(s[i]>='a'&&s[i]<='z')
                    {
                        res+=(eq[s[i]-97]*m);
                    }
                    else
                    {
                		res+=eq[s[i]-'0'+26]*m;
                    }
                    m*=base;
             }
             cout<<"Case #"<<u-T<<": "<<res<<endl;
    }
    return 0;
}

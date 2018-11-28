#include<iostream>
#include<algorithm>
#include<vector>
#include<queue>
#include<set>
#include<map>
#include<cstdlib>
#include<cmath>
#include<stack>
#include<string>
#include<cstdio>
using namespace std;
map<string,bool>mp;
int main()
{
    freopen("A.in","r",stdin);
    freopen("Aout.txt","w",stdout);
    int i,j,test,kase=0,n,m;
    cin>>test;
    string st;
    while(test--)
    {
        cin>>n >> m;
        mp.clear();
        for(i=0;i<n;i++)
        {
            cin>>st;
            string temp="",temp1="";
            temp+="/";
            temp1+="/";
            for(j=1;j<st.size();j++)
            {
                if(st[j]=='/')
                {
                    mp[temp]=true;
                    mp[temp1]=true;
                    temp1="";
                    temp1+="/";
                    temp+="/";
                }
                temp+=st[j];
                temp1+=st[j];
            }
            if(mp[temp]==false)
            {
                mp[temp]=true;
            }
            if(mp[temp1]==false)
            {
                mp[temp1]=true;
            }
        }
        int cnt=0;
        for(i=0;i<m;i++)
        {
            cin>>st;
            string temp="",temp1="";
            temp+="/";
            temp1+="/";

            for(j=1;j<st.size();j++)
            {
                if(st[j]=='/')
                {
                    if(mp[temp]==false)
                        cnt++;
                    //if(mp[temp1]==false)
                     //   cnt++;
                    mp[temp]=true;

                    mp[temp1]=true;
                    temp1="";
                    temp1+="/";
                    temp+="/";
                }
                temp+=st[j];
                temp1+=st[j];
            }
            if(mp[temp]==false)
            {
                cnt++;
                mp[temp]=true;
            }
//            if(mp[temp1]==false)
//            {
//                cnt++;
//                mp[temp1]=true;
//            }

        }
        cout<<"Case #"<<++kase<<": "<<cnt<<endl;
    }
return 0;
}

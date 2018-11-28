#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include<cstring>
using namespace std;
int check[26],opp[26][26];

bool isset(char ch)
{
    int i;
    for(i=0;i<26;i++)
    {
        if(check[i])
        {
            if(opp[i][ch-'A'])
                return true;
        }
    }
    return false;
}
int main()
{
    int T,tt,C,d,n,i,j;
    char deco[26][26];
    stack <char> st;
    cin>>T;
    string str;
    for(tt=1;tt<=T;tt++)
    {
        memset(check,0,sizeof(check));
        memset(opp,0,sizeof(opp));
        while(!st.empty())
                    st.pop();
        for(i=0;i<26;i++)
            for(j=0;j<26;j++)
                deco[i][j]='*';
        cin>>C;
        for(i=0;i<C;i++)
        {
            cin>>str;
            deco[str[0]-'A'][str[1]-'A']=str[2];
            deco[str[1]-'A'][str[0]-'A']=str[2];
        }
        cin>>d;
        for(i=0;i<d;i++)
        {
            cin>>str;
            opp[str[0]-'A'][str[1]-'A']=1;
            opp[str[1]-'A'][str[0]-'A']=1;
        }
        cin>>n;
        cin>>str;
        for(i=0;i<n;i++)
        {
            char temp;
            if(!st.empty())
                temp=st.top();
            if(!st.empty() && deco[str[i]-'A'][temp-'A']!='*')
            {
                //cout<<"2\n";
                //char temp=st.top();
                if(deco[str[i]-'A'][temp-'A']!='*')
                {
                    st.pop();
                    check[temp-'A']--;
                    st.push(deco[str[i]-'A'][temp-'A']);
                    //cout<<deco[str[i]-'A'][temp-'A']<<endl;
                    check[deco[str[i]-'A'][temp-'A']]++;
                }
                else
                {
                    st.push(str[i]);
                    check[str[i]-'A']++;
                    //cout<<"4\n";
                }
            }
            else if(isset(str[i]))
            {
                //cout<<"1\n";
                memset(check,0,sizeof(check));
                while(!st.empty())
                    st.pop();
            }
            else
            {
                //cout<<"3\n";
                st.push(str[i]);
                check[str[i]-'A']++;
            }
        }
        string out="";
        cout<<"Case #"<<tt<<": [";
        while(!st.empty())
            out=st.top()+out, st.pop();
        if(out.length()==0)
            cout<<"]\n";
        else
        {
            for(i=0;i<out.length()-1;i++)
                cout<<out[i]<<", ";
            cout<<out[out.length()-1]<<"]\n";
        }
    }
    return 0;
}

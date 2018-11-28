#include<cstdio>
#include<iostream>
#include<vector>
#include<cmath>
#include<cstring>
using namespace std;
int main()
{
    long i,j,n,l,C,D,N;
    long eli[26][26];
    char com[26][26];
    vector<char> list;
    char c,d;
    string s;
    cin>>n;
    for (l=0;l<n;l++)
    {
        list.clear();
        memset(com,0,sizeof(com));
        memset(eli,0,sizeof(eli));
        cin>>C;
        for (i=0;i<C;i++)
        {
            cin>>s;
            //cout<<"!"<<s<<"!";
            com[s[0]-65][s[1]-65]=s[2];
            com[s[1]-65][s[0]-65]=s[2];
        }
        cin>>D;
        for (i=0;i<D;i++)
        {
            cin>>s;
            eli[s[0]-65][s[1]-65]=1;
            eli[s[1]-65][s[0]-65]=1;
        }
        cin>>N;
        cin>>s;
        //cout<<"!"<<s<<"!";
        for (i=0;i<N;i++)
        {
            c=s[i];
            if ((list.size()!=0) && (com[list[list.size()-1]-65][c-65]!=0))
            {
                d=list[list.size()-1];
                list.pop_back();
                list.push_back(com[d-65][c-65]);
            }
            else
            {
                list.push_back(c);
            }
            for (j=0;j<list.size()-1;j++)
            {
                if (eli[list[j]-65][list[list.size()-1]-65]==1)
                {
                    list.clear();
                    break;
                }
            }
        }
        cout<<"Case #"<<l+1<<": [";
        if (list.size()>0)
        {
            for (i=0;i<list.size();i++)
            {
                if (list.size()-1!=i)
                {
                    cout<<list[i]<<", ";
                }
                else
                {
                    cout<<list[i];
                }
            }
        }
        cout<<"]\n";
    }
}

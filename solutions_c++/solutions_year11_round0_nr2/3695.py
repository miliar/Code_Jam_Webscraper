///shakil
#include <map>
#include <queue>
#include <stack>
#include <cmath>
#include <cctype>
#include <set>
#include <bitset>
#include <algorithm>
#include <list>
#include <vector>
#include <sstream>
#include <iostream>

#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <math.h>
#include <ctype.h>


#define print1(a) cout<<a<<endl
#define print2(a,b) cout<<a<<" "<<b<<endl
#define print3(a,b,c) cout<<a<<" "<<b<<" "<<endl
#define PI (2*acos(0))
#define ERR 1e-5
#define ll long long
#define VI vector<int>
#define mem(a,b) memset(a,b,sizeof a)
#define pb push_back
#define popb pop_back

using namespace std;


stack<char>s;
stack<char>tmp_s;

//vector<char>v;

string str;
string n_str;
string m_str;

map<string,string>M;
int opposed[300];

bool opposed_chk(string str,char c)
{
    if(opposed[c]==0) return false;
    else
    {
        for(int i=0;i<(int)str.size();i++ )
        {
            if(opposed[c]==str[i]) return true;
        }
    }

    return false;
}
int main(void)
{
//    freopen("B-small-attempt0.in","r",stdin);
//    freopen("B-small-attempt0.out","w",stdout);


    freopen("B-small-attempt1.in","r",stdin);
    freopen("B-small-attempt1.out","w",stdout);


    int loop,c,i,d,n,cas=0;
    string ccc;
//    char ch;
    scanf("%d",&loop);
    while(loop--)
    {
        M.clear();
        while(!s.empty()) s.pop();
        while(!tmp_s.empty()) tmp_s.pop();
//        v.clear();
        mem(opposed,0);

        scanf("%d",&c);
        for(i=0;i<c;i++)
        {
            cin>>str;
            n_str.clear();
            n_str+=str[0];
            n_str+=str[1];

            m_str.clear();
            m_str+=str[2];
            M[n_str]=m_str;
//            cout<<"n_str "<<n_str<<"  m_str "<<m_str<<endl;

            n_str.clear();
            n_str+=str[1];
            n_str+=str[0];

//            n_str[0]=str[1];
//            n_str[1]=str[0];
            M[n_str]=m_str;

//            cout<<"n_str "<<n_str<<"  m_str "<<m_str<<endl;
        }

        scanf("%d",&d);
        for(i=0;i<d;i++)
        {
            cin>>str;
            opposed[str[0]]=str[1];
            opposed[str[1]]=str[0];
//            cout<<str[0]<<" op-> "<<opposed[str[0]] <<"  "<<str[1]<<"  op-> "<<opposed[str[1]]<<endl;

        }

        scanf("%d",&n);
        cin>>str;
//        print1(str);
        for(i=0;i<(int)str.size();i++)
        {
            if(s.empty()) {s.push(str[i]);continue;}

            n_str.clear();
            n_str+=s.top();
            n_str+=str[i];
            if(M.find(n_str)!=M.end())
            {
//                cout<<"popped  "<<s.top()<<endl;
                s.pop();
                ccc=M[n_str];
//                puts("matched ");
//                cout<<"cc  "<<ccc<<"  cha  "<<ccc[0]<<endl;
                s.push(ccc[0]);
//                cout<<"pused  "<<s.top()<<endl;
                continue;
            }

            if(opposed[str[i]])
            {
                n_str.clear();
                while(!tmp_s.empty()) tmp_s.pop();

                while(!s.empty())
                {
                    n_str+=s.top();
                    tmp_s.push(s.top());
                    s.pop();
                }
//                cout<<"before chk "<<n_str<<endl;
                if(opposed_chk(n_str,str[i])==false)
                {
//                    puts("don't match");
                    while(!tmp_s.empty())
                    {
                        s.push(tmp_s.top());tmp_s.pop();
                    }
                    s.push(str[i]);
                }
//                else puts("delted ");
                continue;
            }
            else s.push(str[i]);

//            cout<<"pused  "<<s.top()<<endl;
        }

        n_str.clear();

        while(!s.empty())
        {
//            cout<<"in stack "<<s.top();
//            ch=s.top();
            n_str+=s.top();s.pop();
        }

        reverse(n_str.begin(),n_str.end());

        printf("Case #%d: [",++cas);

        if((int)n_str.size()==1)
        {
            printf("%c]\n",n_str[0]);
            continue;
        }
        for(i=0;i<(int)n_str.size();i++)
        {
            if(i==0) printf("%c,",n_str[i]);
            if(i>0 && i!=(int)n_str.size() -1 ) printf(" %c,",n_str[i]);
            else if(i==(int)n_str.size() -1) printf(" %c",n_str[i]);

        }
        puts("]");

    }

    return 0;
}


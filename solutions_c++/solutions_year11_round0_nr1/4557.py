#include<iostream>
#include<vector>
#include<string>
#include<bitset>
#include<algorithm>
#include<sstream>
#include<map>
#include<set>
#include<cmath>
#include<queue>
using namespace std;
int main()
{
    queue<int>O;
    queue<int>B;
    queue<char>s;
    int t;
    cin>>t;
    for(int i=0;i<t;++i)
    {
            int n;
            cin>>n;
            for(int j=0;j<n;++j)
            {
                    char c;int p;
                    cin>>c>>p;
                    if(c=='O')O.push(p);
                    else{B.push(p);}
                    s.push(c);
            }
            int time=0,o=1,b=1,p=0;
            char s1;
            for(int j=0;j<n;++j)
            {
                    s1=s.front();
                    s.pop();
                    if(s1=='O')
                    {
                               if(o<O.front()){p=O.front()-o;o+=p;time+=p;O.pop();}
                               else if(o>O.front()){p=o-O.front();o-=p;time+=p;O.pop();}
                               else{O.pop();p=0;}
                               if(B.empty());
                               else
                               {
                                   if(b==B.front());
                                   else if(b<B.front()){if(b+p+1<B.front())b+=(p+1);else b=B.front();}
                                   else if(b>B.front()){if(b-p-1>B.front())b-=(p+1);else b=B.front();}
                               }
                    }
                    else
                    {
                               if(b<B.front()){p=B.front()-b;b+=p;time+=p;B.pop();}
                               else if(b>B.front()){p=b-B.front();b-=p;time+=p;B.pop();}
                               else{B.pop();p=0;}
                               if(O.empty());
                               else
                               {
                                   if(o==O.front());
                                   else if(o<O.front()){if(o+p+1<O.front())o+=(p+1);else o=O.front();}
                                   else if(o>O.front()){if(o-p-1>O.front())o-=(p+1);else o=O.front();}
                               }
                    }
                    time++;
                    
            }
            cout<<"Case #"<<i+1<<": "<<time<<endl;
    }
}

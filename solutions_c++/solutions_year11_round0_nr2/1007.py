#include<iostream>
#include<math.h>
#include<fstream>
#include<algorithm>
#include<string>
#include<stack>
#include<vector>

using namespace std;
int main()
{
    freopen("agrahri.in","r",stdin);
    freopen("test-large.out","w",stdout);
    int tt;cin>>tt;
    for(int xx=1;xx<=tt;xx++)
    {
        int c,D,n; char *m,*t;string str;cin>>c;char *r,*e,*d;r=new char[c];e=new char[c];d=new char[c];for(int x=0;x<c;x++)cin>>r[x]>>e[x]>>d[x];
        cin>>D;m=new char[D];t=new char[D]; if(D>0) for(int x=0;x<D;x++)cin>>m[x]>>t[x];
        cin>>n;
        cin>>str;
        vector<char> mystack;
        mystack.push_back(str[0]);
        for(int x=1;x<str.size();x++)
        {
            mystack.push_back(str[x]);
            if(c)
            for(int y=mystack.size()-1;y>=0;y--)
            {
                for(int z=0;z<c;z++)
                {if(y>0&&mystack[y]==r[z]&&mystack[y-1]==e[z])
                {mystack.erase(mystack.begin()+mystack.size()-2);mystack.erase(mystack.begin()+mystack.size()-1);mystack.push_back(d[z]);}
                if(y>0&&mystack[y]==e[z]&&mystack[y-1]==r[z])
                {mystack.erase(mystack.begin()+mystack.size()-2);mystack.erase(mystack.begin()+mystack.size()-1);mystack.push_back(d[z]);}}
            }
            if(D)
            {
                for(int z=0;z<D;z++)
                {if(mystack[mystack.size()-1]==m[z])
                {
                    for(int x=0;!mystack.empty()&&x<mystack.size()-1;x++)
                    {
                        if(mystack[x]==t[z])
                        {
                            mystack.clear();
                        }
                    }
                }
                if(mystack[mystack.size()-1]==t[z])
                {
                    for(int x=0;!mystack.empty()&&x<mystack.size()-1;x++)
                    {
                        if(mystack[x]==m[z])
                        {
                            mystack.clear();
                        }
                    }
                }}
            }

        }
        if(mystack.empty())
        cout<<"Case #"<<xx<<": []\n";
        else
        {cout<<"Case #"<<xx<<": [";
       for(int x=0;x<mystack.size()-1;x++)
       cout<<mystack[x]<<", ";
       cout<<mystack[mystack.size()-1]<<"]\n";
        }
    }
	return 0;
}

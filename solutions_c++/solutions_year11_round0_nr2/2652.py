//Bismillahir Rahmanir Rahim
#include <iostream>
#include <cstdio>
#include <cmath>
#include <vector>
using namespace std;

vector<string>vs[30];
vector<char>op[30];


int main()
{
    freopen("B-large.in","r",stdin);
    freopen("B-large.out","w",stdout);
    int kas,cas;cin>>kas;
    for(cas=1;cas<=kas;cas++)
    {
        for(int i=0;i<30;i++)
        vs[i].clear(),op[i].clear();;

        int a;
        cin>>a;
        string str,ch;
        for(int i=0;i<a;i++){
            ch.clear();
            cin>>str;

            ch+=str[0];ch+=str[2];

            vs[str[1]-'A'].push_back(ch);

            ch.clear();
            ch+=str[1];ch+=str[2];
            vs[str[0]-'A'].push_back(ch);
        }
        cin>>a;
        for(int i=0;i<a;i++)
        {
            cin>>str;
            op[str[0]-'A'].push_back(str[1]);
            op[str[1]-'A'].push_back(str[0]);
        }
        int si;
        cin>>si;
        string inp;
        cin>>inp;
        string res;
        for(int i=0;i<inp.size();i++)
        {
            bool t=true;
            char p = inp[i];
            res+=p;
            while(t){
                t=false;
             for(int k=0;k<vs[(p-'A')].size();k++)
             {
                 if(vs[p-'A'][k][0]==res[res.size()-2])
                 {
                     string tt;
                     for(int j=0;j<res.size()-2;j++)
                     tt+=res[j];
                     tt+=vs[p-'A'][k][1];
                     res=tt;
                     p=tt[tt.size()-1];
                     t=true;
                     break;
                 }
             }
            }

            int ss;
            if(res.size()>=2)ss=res.size()-1;
            else ss=0;
            for(int j=0;j<ss;j++)
            {
                int flag=0,up;

              int ks = res.size();
                if(ks>0)
                up=res[ks-1]-'A';
                else continue;
                for(int k=0;k<op[up].size();k++)
                {
                    if(res[j]==op[up][k]){
                        res.clear();
                        flag=1;
                        break;
                    }
                }
                if(flag)break;
            }
        }
        cout<<"Case #"<<cas<<": [";
        for(int i=0;i<res.size();i++)
        {
            if(i)cout<<", ";
            cout<<res[i];
        }
        cout<<"]"<<endl;
    }

}

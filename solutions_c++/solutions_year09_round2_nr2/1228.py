#include <iostream>
#include <algorithm>
#include <vector>
#include <sstream>
#include <math.h>
#include <memory.h>

#define input(a) scanf("%d",&a);
#define REP(a,b,c) for(int a=b;a<c;++a)

using namespace std;
void getnew(string n,int pos,int g)
{
    string final="";
    string p1=n.substr(0,pos);
    n=n.substr(pos+1,n.size()-pos-1);
    reverse(n.begin(),n.end());
    cout<<"Case #"<<g<<": ";
    cout<<p1<<n[0]<<"0"<<n.substr(1,n.size()-1)<<endl;
    return ;

}
int main()
{
 freopen("B-large.in","r",stdin);
 freopen("B-output.out","w",stdout);

    int t;
    cin>>t;
    int g=1;
    while (t--)
    {
        string n;
        cin>>n;
        int D[10];
        memset(D,0,sizeof(D));
        for (int a=n.size()-1;a>=0;--a)
        {
            D[n[a]-'0']++;
        }
        if (n[n.size()-1]!='0')
        {int pos;
            int check=0;
            for (int a=n.size()-1;a>=0;--a)
            {
                if (a==0)
                {
                    check=2;
                    break;
                }
                if (n[a-1]=='0')
                {
                    getnew(n,a-1,g);
                    break;
                }

                if (n[a]>n[a-1])
                {
                   // swap(n[a],n[a-1]);
                    pos=a-1;
                    check=1;
                    break;
                }
            }
            if (check==1)
            {

                string p1="";
                p1=n.substr(0,pos);
                cout<<"Case #"<<g<<": ";
                cout<<p1;
                n=n.substr(pos,n.size()-pos);
                string t=n.substr(1,n.size()-1);
                sort(t.begin(),t.end());
                for (int c=0;c<t.size();++c)
                {
                    if (t[c]>n[0])
                    {
                        cout<<t[c];
                        swap(n[0],t[c]);
                        sort(t.begin(),t.end());
                             cout<<t<<endl;
                             break;
                         }
                     }

            }
            else if (check==2)
            {
                reverse(n.begin(),n.end());
                string temp=n.substr(1,n.size()-1);
                cout<<"Case #"<<g<<": ";
                cout<<n[0]<<"0"<<temp<<endl;
            }
        }
        else
        {
            int check=0,pos;
            int G[10];
            for (int a=n.size()-2;a>=0;--a)
            {
                if (a==0)
                {
                    check=2;
                    break;
                }

                if (n[a]>n[a-1])
                {
                    check=1;
                    pos=a-1;
                    break;
                }
                if (n[a]=='0')
                {
                    continue;
                }
            }
            if (check==1)
            {
                string p1="";
                p1=n.substr(0,pos);
                cout<<"Case #"<<g<<": ";
                cout<<p1;
                n=n.substr(pos,n.size()-pos);
                string t=n.substr(1,n.size()-1);
                sort(t.begin(),t.end());
                for (int c=0;c<t.size();++c)
                {
                    if (t[c]>n[0])
                    {
                        cout<<t[c];
                        swap(n[0],t[c]);
                        sort(t.begin(),t.end());
                             cout<<t<<endl;
                             break;
                         }
                     }

                 }

                 if (check==2)
            {   cout<<"Case #"<<g<<": ";
                string d=n;
                sort(d.begin(),d.end());
                for (int c=0;c<d.size();++c)
                {
                    if (d[c]>'0')
                    {
                        cout<<d[c];
                        d[c]='0';
                        cout<<d<<endl;
                        break;
                    }
                }

            }


        }
        g++;
    }
    return 0;
}

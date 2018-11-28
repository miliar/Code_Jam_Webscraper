#include <iostream>
#include <string>
#include <cmath>
#include <complex>
#include <utility>
#include <cstdio>
#include <stack>
#include <queue>
#include <map>
#include <vector>
#include <algorithm>
#include <list>
#include <set>
#include <sstream>
#include <iterator>
#include <numeric>
#include <functional>
#include <climits>
#include <cstddef>
#include <bitset>
#include <ctime>
#include <memory.h>
#include <stdlib.h>
#include <string.h>


using namespace std;
map<string ,char>mp1;
map<string ,int>mp2;
vector<char>v;
int main()
{

    freopen("B-large.in","r",stdin);
    freopen("B-large.out","w",stdout);
   // freopen("B-small-attempt0.in","r",stdin);
   // freopen("B-small-attempt1.out","w",stdout);

   //B-small-attempt1.in
   //
    int T,n,m,l,i,j,flag,cas=0;
    string st ,st2,st3;
    char a[20000],b[20000],q[20001];
    cin>>T;
    while(T--)
    {
        cin>>n;
        mp1.clear();
        mp2.clear();
        v.clear();
        st3+="";
        st+="";

        for(i=0;i<n;i++)
        {
            cin>>a;

            st="";st+=a[0];st+=a[1];
            mp1[st]=a[2];
            st="";st+=a[1];st+=a[0];
            mp1[st]=a[2];

        }

        cin>>m;
        for(i=0;i<m;i++)
        {
            cin>>b;
           //cout<<b<<endl;
            st="";st+=b[0];st+=b[1];
            mp2[st]=1;
            st="";st+=b[1];st+=b[0];
            mp2[st]=1;

        }

        cin>>l;
        cin>>q;
        st2="";
        st3="";
        for(i=0;i<l;i++)
        {
            flag=0;
            if(v.size()==0)
            {
                flag=1;

                v.push_back(q[i]);
                continue;

            }

            st2="";
            st2+=q[i];
            st2+=v[v.size()-1];

            //cout<<v.size()<<endl;
            //cout<<"st2="<<st2<<" st3="<<st3<<"i="<<i<<endl;
            if(mp1[st2])
            {
                //cout<<"mp1"<<mp1[st2]<<" "  <<mp1[st3]<<endl;
                v[v.size()-1]=mp1[st2];
                flag=1;
            }
            else
            {
                for(j=v.size()-1;j>=0;j--)
                {
                    //cout<<"1mp2"<<endl;
                    st2="";
                    st2+=q[i];
                    st2+=v[j];
                    //cout<<"fg="<<"st2="<<st2<<" st3="<<st3<<"i="<<i<<endl;
                    if(mp2[st2])
                    {
                        v.clear();
                        flag=1;
                        break;
                    }
                }

            }
            if(flag==0)
                v.push_back(q[i]);
        }
        printf("Case #%d: ",++cas);
        if(v.size()==0)
        {
            cout<<"[]"<<endl;
        }
        else if(v.size()==1)
        {
            printf("[%c]\n",v[0]);
        }
        else
        {
            cout<<"["<<v[0];
            for(i=1;i<v.size();i++)
            cout<<", "<<v[i];
           cout<<"]"<<endl;
        }

    }
    return 0;
}

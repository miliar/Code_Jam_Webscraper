#include<iostream>
#include<list>
#include<string>
#include<cstring>
#include<sstream>
#include<cctype>
#include<string.h>
#include<algorithm>
#include<cmath>
#include<stack>
#include<fstream>
#include<cstdlib>
#include<vector>
#include<map>
#include<utility>
#include<iomanip>
#include<queue>
using namespace std;
#define clr(a) memset(a,0,sizeof(a))
#define fill(a,v) memset(a,v,sizeof(a))
#define PB push_back
#define pi acos(-1.0)
#define eps 1e-9

int main()
{
    long a,b,i,cnt,tc,kk=1,num,l;
    string s,s2;
    map<pair<long,long>,long>mark;
    //freopen("C-small-attempt1.in","r",stdin);
    //freopen("C.out","w",stdout);

    cin>>tc;
    while(tc--)
    {
        cin>>a>>b;
        mark.clear();
        cnt=0;
        for(i=a;i<=b;i++)
        {
            stringstream ss;
            ss<<i;
            ss>>s;
            l=s.length();

            for(int j=1;j<l;j++)
            {
                s2="";
                s2+=s[l-1];
                for(int k=0;k<l-1;k++)
                s2+=s[k];

                stringstream ss2;
                ss2<<s2;
                ss2>>num;

                s=s2;

                if(mark[make_pair(i,num)]!=1 && num>=a && num<=b && i!=num)
                {
                    cnt++;
                    mark[make_pair(i,num)]=1;
                    mark[make_pair(num,i)]=1;
                    //cout<<i<<" "<<num<<endl;
                }
            }
        }
        cout<<"Case #"<<kk++<<": "<<cnt<<endl;
    }
return 0;
}

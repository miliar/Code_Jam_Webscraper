#include<iostream>
#include<vector>
#include<iostream>
#include<fstream>
#include<map>
#include<sstream>
#include<cstring>
using namespace std;

# define mp make_pair

int main()
{
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
    int t;
    cin>>t;
    int c=0;
    while(t--)
    {
        c++;
        int a,b;
        int cnt=0;
        map<pair<int,int>,int> mm;
        cin>>a>>b;
        int ar[1001];
        memset(ar,0,sizeof(ar));
        for(int i=a;i<=b;i++)
        {
            stringstream ss;
            ss<<i;
            string s=ss.str();
            int sz=s.size();
            string st,tmp;
            for(int k=sz-1;k>=1;k--)
            {
                if(s[k]=='0') continue;
                tmp="";
                tmp+=s[k];
                tmp+=st;
                st=tmp;
                tmp=st;
                for(int m=0;m<k;m++)
                {
                    tmp+=s[m];
                }
                stringstream s1(tmp);
                int num;
                s1>>num;
                if(mm[mp(i,num)]) continue;
                mm[mp(i,num)]=mm[mp(num,i)]=1;
                if(num>=a&&num<=b&&num!=i)
                cnt++;
            }
        }
        cout<<"Case #"<<c<<": "<<cnt<<"\n";
    }
    return 0;
}

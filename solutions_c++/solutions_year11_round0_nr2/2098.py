#include <iostream>
#include <cstdio>
#include <cstring>
#include <algorithm>
#include <string>
using namespace std;

string s;
bool iscombin[30][30];
bool isopp[30][30];
char map[30][30];
int combin;
int opp;
char ans[200];
int main()
{
    freopen("B-large.in","r",stdin);
    freopen("outlarge.txt","w",stdout);
    int t;
    int cas = 1;
    cin>>t;
    while(t--)
    {
        memset(iscombin,0,sizeof(iscombin));
        memset(isopp,0,sizeof(isopp));
        cin>>combin;
        while(combin--)
        {
            cin>>s;
            int p1 = s[0]-'A';
            int p2 = s[1]-'A';
            iscombin[p1][p2] = iscombin[p2][p1] = true;
            map[p2][p1] = map[p1][p2] = s[2];
        }
        cin>>opp;
        while(opp--)
        {
            cin>>s;
            int p1 = s[0]-'A';
            int p2 = s[1]-'A';
            isopp[p1][p2] = isopp[p2][p1] = true;
        }
        int l;
        int leng = 0;
        cin>>l;
        cin>>s;
        for(int i = 0;i<l;i++)
        {
            //cout<<leng<<endl;
            ans[leng++] = s[i];
            if(leng>=2)
            {
                int p1 = ans[leng-1]-'A';
                int p2 = ans[leng-2]-'A';
                if(iscombin[p1][p2])
                {
                    ans[leng-2] = map[p1][p2];
                    leng--;
                    continue;
                }
                for(int j = leng-2;j>=0;j--)
                {
                    p2 = ans[j]-'A';
                    if(isopp[p1][p2])
                    {
                        leng = 0;
                        break;
                    }
                }
            }
        }
        ans[leng] = 0;
        cout<<"Case #"<<cas++<<": [";
        for(int i=0;i<leng;i++)
        {
            if(i)
                cout<<", ";
            cout<<ans[i];
        }
        cout<<']'<<endl;
    }
    return 0;
}

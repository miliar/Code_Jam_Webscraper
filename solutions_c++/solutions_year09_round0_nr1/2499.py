#include <iostream>
#include <vector>
#include <map>
#include <set>
#include <algorithm>
#include <math.h>
#include <bitset>
#include <string.h>
#include <stack>
#include <queue>
#include <memory.h>

using namespace std;
#define MAXL 10
#define MAXN 10
#define MAXD 25
int main()
{
 freopen("A-small-attempt0.in","r",stdin);
 //   freopen("input","r",stdin);

    freopen("A-small.out","w",stdout);
    int l,d,n;
    cin>>l>>d>>n;


    vector<string> lang;

    string temp;
    int k,count[MAXN+1];

    k=d;
    while (k--)
    {
        cin>>temp;
        lang.push_back(temp);
    }

    char patt[MAXN+1][27][27];
    int pattsize[MAXN+1][27];

    memset(pattsize,0,sizeof(pattsize));
    memset(count,0,sizeof(count));
    for (int a=0;a<n;++a)
    {
        cin>>temp;

        bool ib=0;
        int pos=0;

        for (int b=0;b<temp.size();++b)
        {
            if (temp[b]=='(')
            {
                ib=1-ib;
                continue;
            }
            if (temp[b]==')')
            {
                ib=1-ib;
                pos++;
                continue;
            }
            patt[a][pos][pattsize[a][pos]++]=temp[b];

            if (!ib)
            {
                pos++;
            }
        }
    }

//consider each word
    for (int a=0;a<d;++a)
    {
        temp=lang[a];
        for (int b=0;b<n;++b)
        {
            bool exist=1;
            for (int c=0;c<l;++c)
            {
                char t=temp[c];
                bool check=0;
                for (int d=0;d<pattsize[b][c];++d)
                {
                    if (patt[b][c][d]==t)
                    {
                        check=1;
                        break;
                    }
                }
                if (!check)
                {
                    exist=0;
                    break;
                }
            }
            if (exist==1)
            {
                count[b]++;

            }
        }
    }
    for (int a=0;a<n;++a)
    {
        cout<<"Case #"<<a+1<<": "<<count[a]<<endl;
    }


    return 0;
}

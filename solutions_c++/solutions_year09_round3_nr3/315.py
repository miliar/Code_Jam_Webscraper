#include <iostream>
#include <sstream>
#include <cmath>
#include <algorithm>
#include <string>
#include <vector>
#include <sstream>
using namespace std;

#define two(x)  (1<<x)
#define twol(x) ((long long)1<<x)
#define sqr(x)  ((x)*(x))

main()
{
    freopen("in.txt","r",stdin);
    freopen("out.txt","w",stdout);
    int t;
    cin>>t;
    for (int task=1;task<=t;task++)
    {
        bool c[100];
        int p,q;
        cin>>p>>q;
        for (int i=0;i<p;i++)   c[i]=1;
        vector<int> ind,pos;
        for (int i=0;i<q;i++)
        {
            int num;
            cin>>num;
            pos.push_back(num-1);
            ind.push_back(i);
        }
        int ret=-1;
        do{
            //for (int i=0;i<q;i++)   cout<<pos[ind[i]]<<" ";
            //cout<<endl;
            for (int i=0;i<p;i++)   c[i]=1;
            int cur=0;
            for (int i=0;i<q;i++)
            {
                c[pos[ind[i]]]=0;
                int now=pos[ind[i]]-1;
                while (now>=0&&c[now])
                    cur++,now--;
                now=pos[ind[i]]+1;
                while (now<p&&c[now])
                    cur++,now++;
                //cout<<cur<<endl;
            }
            if (ret==-1||cur<ret)   ret=cur;
            //cout<<cur<<endl;
        }while (next_permutation(ind.begin(),ind.end()));
        printf("Case #%d: %d\n",task,ret);
    }
}

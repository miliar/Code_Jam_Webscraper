#include <iostream>
#include<fstream>
#include<string>
#include<algorithm>
#include<vector>
using namespace std;
#define pb push_back

int abs(int n)
{
    if(n<0)
    return n*-1;
    else
    return n;
}

int main()
{
    ifstream in("D:\\inp.txt");
    ofstream out("D:\\out.txt");
    int t,n;
    in>>t;
    for(int ii=1;ii<=t;ii++)
    {
        in>>n;
        int ora[101][2];
        int blu[101][2];
        char tmp;
        int t1;
        int so=0,sb=0;
        for(int i=0;i<n;i++)
        {
            in>>tmp>>t1;
            if(tmp=='O')
            {
                ora[so][0]=t1;
                ora[so][1]=i;
                so++;
            }
            else
            {
                blu[sb][0]=t1;
                blu[sb][1]=i;
                sb++;
            }

        }
        int ans=0;
        int o=0,b=0,co=1,cb=1;
        for(int i=0;i<n;i++)
        {
            int t2,t3;
            t2=ora[o][0];
            t3=blu[b][0];
            if(o<so && ((ora[o][1]<blu[b][1]) || b>=sb))
            {
                ans+=abs(t2-co);
                ans++;

                if(abs(t3-cb)>(abs(t2-co)+1))
                {
                    int tt=abs(t3-cb)-abs(t2-co)-1;
                    if((t3-cb)>0)
                    cb+=(t3-cb)-tt;
                    else
                    cb+=(t3-cb)+tt;
                }
                else
                {
                    cb=t3;
                }
                co=t2;
                o++;
            }
            else
            {
                ans+=abs(t3-cb);
                ans++;

                if(abs(t2-co)>(abs(t3-cb)+1))
                {
                    int tt=abs(t2-co)-abs(t3-cb)-1;
                    if((t2-co)>0)
                    co+=(t2-co)-tt;
                    else
                    co+=(t2-co)+tt;
                }
                else
                {
                    co=t2;
                }
                cb=t3;
                b++;
            }
        }
        out<<"Case #"<<ii<<": "<<ans<<endl;
    }
    return 0;
}

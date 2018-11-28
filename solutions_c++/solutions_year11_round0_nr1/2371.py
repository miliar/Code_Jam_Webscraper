#include <iostream>
#include<fstream>
#include<string>
#include<algorithm>
#include<vector>
using namespace std;
#define pb push_back

int absolute(int n)
{
    if(n<0)
    return n*-1;
    else
    return n;
}

int main()
{
    ifstream f_in("D:\\inp.txt");
    ofstream f_out("D:\\out.txt");
    int t,n;
    f_in>>t;
    for(int ii=1;ii<=t;ii++)
    {
        f_in>>n;
        int orange[101][2];
        int blue[101][2];
        char temp;
        int temp1;
        int so=0,sb=0;
        for(int itr=0;itr<n;itr++)
        {
            f_in>>temp>>temp1;
            if(temp=='B')
            {
                blue[sb][0]=temp1;
                blue[sb][1]=itr;
                sb++;
            }
            else
            {
                orange[so][0]=temp1;
                orange[so][1]=itr;
                so++;
            }
        }
        int ans=0;
        int o=0,b=0,co=1,cb=1;
        for(int itr=0;itr<n;itr++)
        {
            int t2,t3;
            t2=orange[o][0];
            t3=blue[b][0];
            if(o<so && ((orange[o][1]<blue[b][1]) || b>=sb))
            {
                ans+=absolute(t2-co);
                ans++;

                if(absolute(t3-cb)>(absolute(t2-co)+1))
                {
                    int tt=absolute(t3-cb)-absolute(t2-co)-1;
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
                ans+=absolute(t3-cb);
                ans++;

                if(absolute(t2-co)>(absolute(t3-cb)+1))
                {
                    int tt=absolute(t2-co)-absolute(t3-cb)-1;
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
        f_out<<"Case #"<<ii<<": "<<ans<<endl;
    }
    return 0;
}

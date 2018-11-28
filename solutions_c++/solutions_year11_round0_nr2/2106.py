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
    int t;
    int c,d,n;
    in>>t;
    for(int ii=1;ii<=t;ii++)
    {
        in>>c;
        vector<string> comb(c);
        for(int i=0;i<c;i++)
        in>>comb[i];
        in>>d;
        vector<string> opp(d);
        for(int i=0;i<d;i++)
        in>>opp[i];
        in>>n;
        string inp;
        in>>inp;
        string res;
        res.pb(inp[0]);
        int len=1;
        char t1,t2;
        int flag;
        for(int i=1;i<n;i++)
        {
            flag=0;
            t1=res[len-1];
            t2=inp[i];
            for(int j=0;j<c;j++)
            {
                if((t1==comb[j][0] && t2==comb[j][1]) || (t1==comb[j][1] && t2==comb[j][0]) )
                {
                    res[len-1]=comb[j][2];
                    flag=1;
                    break;
                }
            }
            for(int j=0;j<d && flag==0;j++)
            {
                if(t2==opp[j][1])
                {
                    t1=opp[j][0];
                    for(int q=0;q<len;q++)
                    {
                        if(t1==res[q])
                        {
                            res.clear();
                            len=0;
                            flag=2;
                            break;
                        }
                    }
                }
                else if(t2==opp[j][0])
                {
                    t1=opp[j][1];
                    for(int q=0;q<len;q++)
                    {
                        if(t1==res[q])
                        {
                            res.clear();
                            len=0;
                            flag=2;
                            break;
                        }
                    }
                }
            }
            if(flag==0)
            {
                res.pb(t2);
                len++;
            }

        }
        out<<"Case #"<<ii<<": [";
        for(int i=0;i<len;i++)
        {
            if(i!=0)
            out<<", ";
            out<<res[i];
        }
        out<<"]"<<endl;
    }
    return 0;
}

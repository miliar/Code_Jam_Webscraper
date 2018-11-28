#include <iostream>
#include <fstream>
#include <stack>

using namespace std;

int main()
{
    ifstream be("jam.be");
    ofstream ki("jam.ki");
    int t;
    be>>t;
    for(int testcase=1;testcase<=t;testcase++)
    {
        int n,s,p;
        be>>n>>s>>p;
        int tuti=0,lehet=0;
        for(int i=0;i<n;i++)
        {
            int m;
            be>>m;
            int k=m/3;
            switch (m)
            {
                case 0 : if(p==0) tuti++; break;
                case 1 : if(p<=1) tuti++; break;
                case 29 : if(p<=10) tuti++; break;
                case 30 : if(p<=10) tuti++; break;
                default:
                    switch (m%3)
                    {
                        case 0 : if(k>=p) tuti++;
                                 if(k+1==p) lehet++;
                                 break;
                        case 1 : if(k+1>=p) tuti++;
                                 break;
                        case 2 : if(k+1>=p) tuti++;
                                 if(k+2==p) lehet++;
                                 break;
                    }
            }

        }
        int max = tuti;
        if(s<lehet)
            max += s;
        else
            max += lehet;
        ki<<"Case #"<<testcase<<": "<<max<<endl;
    }
    be.close();
    ki.close();
    return 0;
}

#include<iostream>
#include<vector>
#include<string>
#include<sstream>
#include<map>
#include<fstream>
#include<cmath>
#include<stdlib.h>
#include<iomanip>
#include <algorithm>

using namespace std;

int main()
{
    ifstream f("B-small-attempt2.in");
    ofstream of("B-small-attempt2.out");

    int T;
    f >> T;

    map<int, int> nsp;
    map<int, int> sp;
    nsp[0] = 0;
    sp[0] = 0;
    nsp[1] = 1;
    sp[1] = 1;
    nsp[2] = 1;
    sp[2] = 2;
    for(int t1 = 1; t1<=T; ++t1)
    {
        of<<"Case #"<<t1<<": ";

        int sum = 0;

        int n,s,p;
        f >>n>>s>>p;

        int t[n];

        for(int i =0; i< n; ++i)
            f >> t[i];

        for(int i =0; i< n; ++i)
        {
            if(nsp.find(t[i]) == nsp.end())
            {
                //calculate the best of not suprise and suprice case
                int a = t[i] / 3;
                //cout<<t[i]<<endl;
                int b = t[i] % 3;
                if(b == 0)
                {
                    nsp[t[i]] = a;
                    sp[t[i]] = a + 1;
                }
                else if(b == 1)
                {
                    nsp[t[i]] = a + 1;
                    sp[t[i]] = a + 2;
                }
                else if(b == 2)
                {
                    nsp[t[i]] = a + 1;
                    sp[t[i]] = a + 2;
                }

            }

            //cout<<t[i]<<" "<<nsp[t[i]]<<" "<<sp[t[i]]<<" "<<p<<" "<<sum<<" "<<s<<endl;
            if(nsp[t[i]] >= p)
                sum++;
            else if(sp[t[i]] >= p && s > 0)
            {
                sum++;
                s--;
            }
        }

        of<<sum<<endl;

    }

//    map<int, int>::iterator it;
//    for(it = nsp.begin(); it!=nsp.end(); ++it)
//    {
//        cout<<it->first<<" "<<it->second<<" "<<sp[it->first]<<endl;
//    }

    //m.close();
    f.close();
    of.close();
    return 0;
}

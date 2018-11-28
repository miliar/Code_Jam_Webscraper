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
    ifstream f("C-large.in");
    ofstream of("C-large.out");

    int T;
    f >> T;

    for(int t = 1; t<=T; ++t)
    {
        int test=0;

        of<<"Case #"<<t<<": ";

        int ans = 0;

        int A,B;
        f>>A>>B;
        if(A==B)
        {
            of<<"0"<<endl;
            continue;
        }

        for(int n = A; n < B; ++n)
        {
            string ns;
            std::ostringstream nstring(ns);
            nstring << n;
            ns = nstring.str();
            string originS = ns;
            for(int i = 0; i<ns.size()-1;++i)
            {
                ns = ns.substr(ns.size()-1, 1) + ns.substr(0, ns.size()-1);
                if(ns == originS) break;

                int m;
                m = atoi(ns.c_str());
                if(m>n && m<=B)
                {
                    ans++;
                    //cout<<n<<","<<m<<endl;
//                    if(test == m)
//                        cout<<"--------------"<<endl;
//                    test = m;
                }

            }
        }

        of<<ans<<endl;

    }

//    map<char, char>::iterator it;
//    for(it = lang.begin(); it!=lang.end(); ++it)
//    {
//        of<<it->first<<it->second<<endl;
//    }

    //m.close();
    f.close();
    of.close();
    return 0;
}

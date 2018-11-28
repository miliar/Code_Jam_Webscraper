#include <iostream>
#include <algorithm>
#include <sstream>
#include <string>
#include <cmath>
#include <vector>
#include <cstdlib>

using namespace std;

#define FOR(i,a,b) for(int i=(a);i<(b);++i)
#define VI vector<int>
#define pb push_back

char a[10000];


int main()
    {

    int TC;
    gets(a);
    sscanf(a,"%d",&TC);

    FOR(tc, 0, TC)
        {
        gets(a);
        string b;
        FOR(i,0,strlen(a))
            b+=a[i];
        stringstream SS(b);

        int N; SS >> N;
        
        VI koji(N);
        VI poz(N);

        FOR(i,0,N)
            {
            string s1, s2;
            char c;
            SS >> s1 >> s2;
            sscanf(s1.c_str(),"%c",&c);
            sscanf(s2.c_str(),"%d",&poz[i]);
            if ( c == 'B' ) koji[i] = 0;
            else koji[i] = 1;
            }

        int sol = 0;
        int p0 = 1, p1 = 1, t0 = 0, t1 = 0;

        FOR(i,0,N)
            {
            if( koji[i] == 0 )
                {
                int d = abs( p0 - poz[i] );
                int t = max( 1, d + 1 - ( sol - t0 ));
                sol += t;
                p0 = poz[i];
                t0 = sol;
                }
            else
                {
                int d = abs( p1 - poz[i] );
                int t = max( 1, d + 1 - ( sol - t1 ));
                sol += t;
                p1 = poz[i];
                t1 = sol;
                }
            //cout << p0 << " " << t0 << " " << p1 << " " << t1 << endl;
            //cout << sol << endl;
            }

        printf("Case #%d: %d\n",tc+1,sol);
        }
    //system("pause");
    return 0;
    }

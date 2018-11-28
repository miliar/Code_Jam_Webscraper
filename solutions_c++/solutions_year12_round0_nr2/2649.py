#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <algorithm>
#include <math.h>
#include <map>

using namespace std;

int main()
{
    ifstream is;
    ofstream rs;
    is.open("./B-small-attempt.in");
    rs.open("./res.out");
    int num_of_test;
    is >>  num_of_test;
    string _str;
    getline(is,_str);
    for(int num=0; num<num_of_test; num++)
    {
        int N, S, P;
        is >> N;
        is >> S;
        is >> P;
        int res=0;
        int sum[P];
        int rates[N][3];
        int s_rates[N][3];
        for(int i=0; i<N; i++)
        {
            is >> sum[i];
        }
        for(int i=0; i<N; i++)
        {
            div_t divresult;
            divresult = div (sum[i],3);
            int n = divresult.quot;
            int mod = divresult.rem;
            if (mod==0)
            {
                rates[i][0]=n;rates[i][1]=n;rates[i][2]=n;
                if(n>0) {s_rates[i][0]=n-1;s_rates[i][1]=n;s_rates[i][2]=n+1;}
                else {s_rates[i][0]=-1;s_rates[i][1]=-1;s_rates[i][2]=-1;}
            }
            else if(mod==1)
            {
                rates[i][0]=n;rates[i][1]=n;rates[i][2]=n+1;
                if(n>0) {s_rates[i][0]=n-1;s_rates[i][1]=n+1;s_rates[i][2]=n+1;}
                else {s_rates[i][0]=-1;s_rates[i][1]=-1;s_rates[i][2]=-1;}
            }
            else if(mod==2)
            {
                rates[i][0]=n;rates[i][1]=n+1;rates[i][2]=n+1;
                if(n>0) {s_rates[i][0]=n;s_rates[i][1]=n;s_rates[i][2]=n+2;}
                else {s_rates[i][0]=-1;s_rates[i][1]=-1;s_rates[i][2]=-1;}
            }
        }
        for(int i=0; i<N; i++)
        {
            if((rates[i][0]>=P)||(rates[i][1]>=P)||(rates[i][2]>=P))
                res=res+1;
            else if((s_rates[i][0]>=P)||(s_rates[i][1]>=P)||(s_rates[i][2]>=P))
            {
                if(S>0)
                {
                    res=res+1;
                    S=S-1;
                }
            }
        }

        rs << "Case #" << num+1 << ": " << res << endl;
    }
    return 0;
}



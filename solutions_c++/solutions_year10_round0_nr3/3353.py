#include <iostream>
#define REP(i,a,b) for(unsigned int i=a; i<b; i++)
#include <fstream>

using namespace std;

int main(int argc, char *argv[])
{
    long long T, R, K, N, *g, sum, act, gon, actO, up;

    fstream plikIn ("large.in", fstream::in | fstream::out);
    fstream plikOut ("large.out", fstream::in | fstream::out);

    plikIn >> T;


    REP(i,0,T)
    {
        sum = 0;
        up = 0;
        plikIn >> R >> K >> N;
        g = new long long[N];
        REP(k,0,N)
        {
            plikIn >> g[k];
            up += g[k];
        }

        if(*argv[1]=='h' && i<42)continue;
        else if(*argv[1]=='l' && i>42)continue;

        if(K>up)
        {
            cout << "Case #" << i+1 << ": " << R*up << endl;
            plikOut << "Case #" << i+1 << ": " << R*up << endl;
            continue;
        }



        act = 0;
        actO = 0;
        gon = 0;
        while(R>0)
        {
            if(act!=actO-1 && !(act==N-1 && actO==0))
            {
                if(gon+g[act]<=K)
                {
                    gon += g[act];
                    if(act!=N-1)act++;else act = 0;

                }else
                {
                    sum += gon;
                    actO = act;
                    R--;
                    gon = 0;

                }
            }else
            {
                if(gon+g[act]<=K)
                {
                    gon += g[act];
                    act = actO;
                }else actO = act;
                R--;
                sum += gon;
                gon = 0;

            }

        }
        delete []g;
        cout << "Case #" << i+1 << ": " << sum << endl;
        plikOut << "Case #" << i+1 << ": " << sum << endl;
    }

    plikIn.close();
    plikOut.close();
    return 0;
}

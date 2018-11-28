#include <iostream>
#include <fstream>
#include <string>
#include <cstdio>

using namespace std;




int main()
{
    ifstream sisend;
    ofstream valjund;

    sisend.open("A-small.in");
    valjund.open("A-small.out");

    int T, N, M;

    sisend >> T;

    for(int u = 1; u<=T; u++)
    {
        string sdir[210];
        for(int i = 0; i<=205; i++)
            sdir[i]="";
        int sol = 0;
        string stemp1;


        sisend >> N >> M;

        int itemp=N;

        for(int i = 1; i<=N; i++)
        {
            sisend >> sdir[i];
        }
        for(int i = 1; i<=M; i++)
        {
            sisend >> stemp1;
            cout << stemp1;
            //system("PAUSE");
            string stemp2 = "/";
            for(int j = 1; j<=stemp1.size(); j++)
            {

                if(stemp1[j]=='/'||j==stemp1.size())
                {
                    cout << stemp2;

                    int inc = 1;
                    for(int k= 1; k<=200; k++)
                        if(sdir[k]==stemp2)
                            inc=0;
                    sol=sol+inc;
                    cout << sol;
                    //system("PAUSE");
                    itemp++;
                    sdir[itemp]=stemp2;
                }
                stemp2= stemp2 + stemp1[j];
            }
        }
        valjund << "Case #" << u << ": " << sol << "\n";
    }



    return 0;
}

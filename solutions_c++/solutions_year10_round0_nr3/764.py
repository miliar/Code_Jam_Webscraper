#include <iostream>
#include <fstream>

using namespace std;

int T, N;
int64_t  R, k, ans;
int64_t g[1001];
int64_t h[1001][2];
//int a[500][2];
//int ind=0;


int main()
{

    ifstream b_file ( "input.txt" );
    ofstream a_file ( "output.txt" );

    for (int j=0; j<1001; j++)
        {
            g[j] = 0;
            h[j][0] = 0;
            h[j][1] = 0;
        }



    b_file >> T;
    for (int i=1; i<=T; i++)
        {

        for (int j=0; j<1001; j++)
        {
            g[j] = 0;
            h[j][0] = 0;
            h[j][1] = 0;
        }

        b_file >> R;
        b_file >> k;
        b_file >> N;

        for (int j=0; j<N; j++)
        {
            b_file >> g[j];
        }


        int j=0;
        while(j<N)
        {
            h[j][0] = g[j];
            int z = 1;
            while ((h[j][0] + g[(j+z)%(N)] <= k) && ((j+z)%(N) != j))
            {
             h[j][0] += g[(j+z)%N];
             z++;
            }

            h[j][1] = (j+z)%N;
            j++;


        }


        int pos = 0;
        ans = 0;
        for (int j=0; j<R; j++)
        {
            ans += h[pos][0];
            pos = h[pos][1];
        }





       /*
       cout << R <<" ";
        cout << k<<" ";
        cout << N<<"\n";

        for (int j=0; j<N; j++)
        {
            cout <<g[j]<<" ";
        }
        cout <<"\n";
            */


        //cout<<i<<"\n";
//a_file
        a_file<<"Case #"<<i<<": "<<ans<<"\n";
        }

    //cout<< 10%7;
    cin.get();    // wait for a keypress
    // b_file is closed implicitly here
    return 0;
}


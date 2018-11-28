/* Song Qiang
 */ 

#include <cmath>

#include <string>
#include <vector>
#include <iostream>
#include <fstream>
#include <algorithm>
#include <limits>
#include <list>

using namespace std;

int
main(int argc, const char **argv)
{
    ifstream in(argv[1]);
    ofstream out(argv[2]);
    
    int T;
    in >> T;

    for (size_t t = 0; t < T; ++t)
    {
        int N;
        in >> N;
        in.ignore();
        
        vector<vector<int> > a(N, vector<int>(N));
        for (size_t i = 0; i < N; ++i)
        {
            
            for (size_t j = 0; j < N; ++j)
            {

                char ch;
                in >> ch;
                if (ch == '\n') in >> ch;
                // cerr << ch;
                switch (ch)
                {
                case '1': a[i][j] = 1; break;
                case '0': a[i][j] = 0; break;
                case '.': a[i][j] = 2; break;
                }
                // cerr << a[i][j] << " ";
                
            }

            // cerr <<  endl;
        }
        
        vector<double> total(N), win(N);
        for (size_t i = 0; i < N; ++i)
        {
            int t = 0, w = 0;
            for (size_t j = 0; j < N; ++j)
            {
                switch (a[i][j])
                {
                case 1: t++; w++; break;
                case 0: t++; break;
                case 2: ; break;
                }
            }
            total[i] = t;
            win[i] = w;

//            cerr << i << "\t" << w << "\t" << t << endl;
         }
        
        vector<double> wp(N);
        for (size_t i = 0; i < N; ++i)
            wp[i] = win[i] / total[i];

        vector<double> owp(N);
        for (size_t i = 0; i < N; ++i)
        {
            double s = 0;
            for (size_t j = 0; j < N; ++j)
                if (a[i][j] != 2)
                {
                    s += (win[j] - a[j][i]) / (total[j] - 1);
                }
            owp[i] = s / total[i];
        }

        vector<double> oowp(N);
        for (size_t i = 0; i < N; ++i)
        {
            double s = 0;
            for (size_t j = 0; j < N; ++j)
                if (a[i][j] != 2)
                {
                    s += owp[j];
                }
            oowp[i] = s / total[i];
        }
        
        cout << "Case #" << t+1 << ":" << endl;
        for (size_t i = 0; i < N; ++i)
            cout << 0.25 * wp[i] + 0.5*owp[i] + 0.25 * oowp[i] << endl;
    }
  
    return EXIT_SUCCESS;
}

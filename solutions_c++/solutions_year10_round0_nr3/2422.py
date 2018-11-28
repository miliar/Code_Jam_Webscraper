#include <iostream>
#include <string>
#include <fstream>
#include <sstream>
#include <list>
#include <math.h>

using namespace std;

int getEarnedMoney(int R, int k, int N, list<int> G);

// Main
int main(int arg, char** argv)
{
    // If no input file, print the usage, and exit.
    if(arg != 2)
    {
        cout << "Usage: " << endl;
        cout << "sc <filename>" << endl << endl;
	exit(0);
    }
	
    int T, R, k, N;
    list<int> G;

    // Parse file
    ifstream ifs(argv[1], ifstream::in);
    string sln;
    
    getline(ifs, sln);
    istringstream iss(sln, istringstream::in);
    iss >> T;
    // cout << "There are " << T << " test cases." << endl;

    // There are T cases
    for(int i = 1; i < T + 1; i ++)
        {
            getline(ifs, sln);
            istringstream iss1(sln);
            iss1 >> R >> k >> N;
            // cout << "R = " << R << ", k = " << k << ", N = " << N << endl;
            getline(ifs, sln);
            istringstream iss2(sln);
	    for(int j = 0; j < N; j ++)
                {
                    int g;
                    iss2 >> g;
                    // cout << "G[" << j << "] = " << g << ", ";
                    G.push_back(g);
                }
            // cout << endl;
            cout << "Case #" << i << ": " << getEarnedMoney(R, k, N, G) << endl;
            G.clear();
	}
    ifs.close();

    return 0;
}

int getEarnedMoney(int R, int k, int N, list<int> G)
{
    int m = 0;
    for(int i = 0; i < R; i ++)
        {
            // cout << "R: " << i << "; ";
            int sm = 0;
            int g = 0;
            /* for(int j = 0; j < N; j ++)
                {
                    int temp = G.front();
                    cout << temp << ", ";
                    G.pop_front();
                    G.push_back(temp);
                    } */
            while((sm + G.front() <= k) && (g < N))
                {
                    int gm = G.front();
                    sm += gm;
                    G.pop_front();
                    G.push_back(gm);
                    g++;
                }
            m += sm;         
        }
    return m;
}

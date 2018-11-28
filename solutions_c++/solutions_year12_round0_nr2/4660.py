#include <vector>
#include <iostream>
#include <fstream>
#include <algorithm>
#include <functional>
#include <map>
#include <math.h>
#include <iomanip>

using namespace std;
typedef unsigned long long int ui;
#define PI M_PI

short **dp;
int *score;
int p;
int S;

int normal(int j, int k)
{
    int sc = score[k];
    int ret = k<1 ? 0 : dp[j][k-1];
    int diff = 3;
    int n = 0;
    
    if (sc == 0)
    {
        if (p == 0) return ret+1;
        else        return ret;
    }
    
    if (3*p-2 <= sc) ret++;
    
//    do {
//        diff--;
//        n = (sc - diff)/3;
//    } while (3*n+diff != sc);
//    
//    if (diff) n++;
//    
//    if (p <= n) ret++;
    
    return ret;
}

int sup(int j, int k)
{
    if (j == 0) return 0;
    
    int sc = score[k];
    int ret = k<1 || j<1 ? 0 : dp[j-1][k-1];
    int diff = 5;
    int n = 0;
    
    if (sc == 0)
    {
        if (p == 0) return ret+1;
        else        return ret;
    }
    
    if (3*p-4 <= sc) ret++;
    
//    do {
//        diff--;
//        n = (sc - diff)/3;
//    } while (3*n+diff != sc);
//    
//    if (2 <= diff) n+=2;
//    
//    if (p <= n) ret++;
    
    return ret;
}

int main()
{
	ifstream ifp("./B-large.in");
	//ifstream ifp("./test.txt");
	ofstream ofp("./output.txt");
	
    int T, N;
    
	ifp >> T;
	cout << "testcase : " << T << endl;
	for (int i = 0; i < T; i++)
	{
        ifp >> N >> S >> p;
        cout << N << "," << S << "," << p << endl;
        S++;
        
        
        score = new int [N];
        dp = new short* [S];
        for (int j = 0; j < S; j++)
        {
            dp[j] = new short[N];
        }

        for (int j = 0; j < N; j++)
        {
            ifp >> score[j];
        }
        
        for (int j = 0; j < S; j++)
        {
            for (int k = 0; k < N; k++)
            {
                if ((k < j-1 && k < S-2) || (j+(N-S) < k))
                {
                    dp[j][k] = 0;
                } else
                {
                    dp[j][k] = 1;
                }
            }
        }
        
        //---------------------------------
        
        for (int j = 0; j < S; j++)
        {
            for (int k = 0; k < N; k++)
            {
                if (dp[j][k])
                {
                    dp[j][k] = max(normal(j, k), sup(j, k));
                    cout << dp[j][k] << ",";
                }
                else {
                    cout << "0,";
                }
            }
            cout << endl;
        }
        
		ofp << "Case #" << i+1 << ": " << dp[S-1][N-1] << endl;
        
		cout << "Case #" << i+1 << ": " << dp[S-1][N-1] << endl;
        
        delete [] score;
        for (int j = 0; j < S; j++) delete [] dp[j];
        delete [] dp;
	}
}



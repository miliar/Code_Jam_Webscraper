#include <map>
#include <set>
#include <cmath>
#include <queue>
#include <vector>
#include <string>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cassert>
#include <climits>
#include <numeric>
#include <algorithm>
#include <iostream>
#include <fstream>
#include <sstream>
#include <ctime>
#include <stdio.h>
#include <conio.h>
using namespace std;

typedef long long int64;
typedef vector<int> vi;
typedef vector<string> vs;
typedef vector<double> vd;
typedef pair<int,int> pii;

#define _CRT_SECURE_NO_WARNINGS
#define For(i,a,b) for (int i(a),_b(b); i <= _b; ++i)
#define Ford(i,a,b) for (int i(a),_b(b); i >= _b; --i)
#define Rep(i,n) for (int i(0),_n(n); i < _n; ++i)
#define Repd(i,n) for (int i((n)-1); i >= 0; --i)
#define Fill(a,c) memset(&a, c, sizeof(a))
#define MP(x, y) make_pair((x), (y))
#define All(v) (v).begin(), (v).end()

template<typename T, typename S> T cast(S s) {
	stringstream ss;
	ss << s;
	T res;
	ss >> res;
	return res;
}

template<typename T> inline T sqr(T a) { return a*a; }
template<typename T> inline int Size(const T& c) { return (int)c.size(); }
template<typename T> inline void checkMin(T& a, T b) { if (b < a) a = b; }
template<typename T> inline void checkMax(T& a, T b) { if (b > a) a = b; }

// Global variables
int H, W;
int Map[101][101];
int Basins[101][101];
int CurrentSink = 0;
int Altitudes[4];
int Order[4];
int k, l, m, Aux;

int Explore (int i, int j)
{
     // Already checked
     if (Basins[i][j] != 0)
        return Basins[i][j];
     //cout << Map[i][j] << " ";
     
     // North
     Order[0] = 0;
     if (i - 1 >= 0)
        Altitudes[0] = Map[i-1][j];
     else
         Altitudes[0] = -1;
     // West
     Order[1] = 1;
     if (j - 1 >= 0)
        Altitudes[1] = Map[i][j-1];
     else
         Altitudes[1] = -1;
     // East
     Order[2] = 2;
     if (j + 1 < W)
        Altitudes[2] = Map[i][j+1];
     else
         Altitudes[2] = -1;
     // South
     Order[3] = 3;
     if (i + 1 < H)
        Altitudes[3] = Map[i+1][j];
     else
         Altitudes[3] = -1;             
         
     // Sort
     For (k, 0, 2)
     {
         For (l, k+1, 3)
         {
             if ((Altitudes[k] > Altitudes[l]) || ((Altitudes[k] == Altitudes[l]) && (Order[k] > Order[l])))
             {
                // Exchange Altitudes
                Aux = Altitudes[k];
                Altitudes[k] = Altitudes[l];
                Altitudes[l] = Aux;
                
                // Exchange Order
                Aux = Order[k];
                Order[k] = Order[l];
                Order[l] = Aux;
             }
         }
     }     
     
     // Select Lower
     m = 0;
     while (Altitudes[m] == -1)
           m++;
     if (Altitudes[m] < Map[i][j])
     {
        switch (Order[m])
        {
               case 0 :  Basins[i][j] = Explore (i-1, j);
                         break;
               case 1 :  Basins[i][j] = Explore (i, j-1);
                         break;
               case 2 :  Basins[i][j] = Explore (i, j+1);
                         break;
               case 3 :  Basins[i][j] = Explore (i+1, j);
                         break;
        }
        
     }
     else
     {
         CurrentSink++;
         Basins[i][j] = CurrentSink;
     }
     return Basins[i][j];
}

int main() 
{
    /* Files */
    ifstream fin ("B-large.in");
	 ofstream fout ("B-test.out");
    
    /* Variables */
    int T;
    
    /* Read File */
    fin >> T;
    For (n, 1, T)
    {
        // Read Map
        fin >> H >> W;
        Rep (i, H)
        {
            Rep (j, W)
            {
                fin >> Map[i][j];
            }
        }
        
        // Process
        memset (Basins, 0, sizeof(Basins));
        CurrentSink = 0;
        Rep (i, H)
        {
            Rep (j, W)
            {
                //cout << i << "-" << j << ":";
                Explore (i, j);
                //cout << endl;
            }
        }
               
        /* Print answer */
        char Traslate[50];
        char CurrentChar = 'a';
        memset (Traslate, 0, sizeof(Traslate));
        fout << "Case #" << n << ":" << endl;
        Rep (i, H)
        {
            Rep (j, W)
            {
                if (Traslate[Basins[i][j]] == 0)
                {
                   Traslate[Basins[i][j]] = CurrentChar;
                   CurrentChar++;
                }
                fout << Traslate[Basins[i][j]] << " ";
            }
            fout << endl;
        }
    }
    
    //getch();
    //cin.get();
    fout.close();
    fin.close();
	 exit(0);
}

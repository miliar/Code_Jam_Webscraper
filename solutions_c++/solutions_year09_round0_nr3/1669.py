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
char Text[510];
char Welcome[] = "welcome to code jam*";
int64 Result;
int i;

void Explore (int poscad, int poswelcome, int64 Cuenta)
{
     //cout << poscad << " " << poswelcome << " " << Cuenta << endl;
     int Conteo;
     
     // Finish
     if (poswelcome == strlen(Welcome) - 1)
     {
        Result += Cuenta;
        Result %= 10000;
        //cout << "Res : " << Result << endl;
     }
     
     // Find current letter occurrences
     Conteo = 0;
     while (poscad < strlen(Text))
     {
           if (Text[poscad] == Welcome[poswelcome])
              Conteo++;
           else
           {
               if (Conteo > 0)
               {
                  if (Text[poscad] == Welcome[poswelcome + 1])
                  {
                     Explore(poscad, poswelcome + 1, Cuenta == 0 ? Conteo : Cuenta * Conteo);
                     Conteo = 0;
                  }
               }
           }
           
           poscad++;
     }
     

}

int main() 
{
    /* Files */
    ifstream fin ("C-small.in");
	 ofstream fout ("C-test.out");
    
    /* Variables */
    int N;
    char ResultCad[20];
    
    /* Read File */
    fin >> N;
    fin.getline(Text, 502);
    For (n, 1, N)
    {
        // Read string
        fin.getline(Text, 502);
        strcat(Text, "*");
        
        // Process
        Result = 0;
        Explore (0, 0, 0);
        //getch();
               
        /* Print answer */
        sprintf (ResultCad, "%04d", Result);
        fout << "Case #" << n << ": " << ResultCad << endl;
    }
    
    //getch();
    fout.close();
    fin.close();
	 exit(0);
}

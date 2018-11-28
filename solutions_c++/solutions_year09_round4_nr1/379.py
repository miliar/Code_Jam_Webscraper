#include<algorithm>
#include<cmath>
#include<fstream>
#include<iomanip>
#include<iostream>
#include<map>
#include<queue>
#include<set>
#include<sstream>
#include<stack>
#include<vector>

using namespace std;

#define forn(i,n) for(int i = 0; i < (n); i++)
#define dforn(i,n) for(int i = (int)(n-1); i >= 0; i--)
#define all(v) v.begin(), v.end()
#define pb push_back

vector<string> tabla;
vector<int> entra;
int main()
{
    ifstream fin("A-large.in");
    ofstream fout("A-large.out");
	int casos;
	fin >> casos;
	forn(casito,casos)
	{
	    tabla.clear();
	    entra.clear();
	    int k;
	    fin >> k;
	    entra.resize(k);
	    string st;
	    forn(i,k)
        {
            fin >> st;
            tabla.push_back(st);
        }
        forn(i,k)
        {
            entra[i] = 0;
            forn(j,k)
            {
                if(tabla[i][j] == '1')
                    entra[i] = j;
            }
        }
        int pasos = 0;
        int pos = 0;
        while(pos<k)
        {
            int t = pos;
            while(entra[t]>pos)
                t++;
            int et = entra[t];
            for(int i=t;i>pos;i--)
            {
                entra[i] = entra[i-1];
            }
            entra[pos] = et;
            pasos += t-pos;
            pos++;
        }
	    fout << "Case #" << casito+1 << ": " << pasos << endl;
	}
}

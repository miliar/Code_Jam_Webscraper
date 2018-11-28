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

int tabla[50][50];
bool vecinos[100][100];
int pos[16];

bool sigue(int n)
{
    int pos1 = n-1;
    while(pos[pos1]==1)
    {
        pos1--;
        if(pos1==-1)
            return false;
    }
    pos[pos1]=1;
    for(int i=pos1+1;i<n;i++)
        pos[i] = 0;
    return true;
}

int main()
{
    ifstream fin("C-small.in");
    ofstream fout("C-small.out");
	int casos;
	fin >> casos;
	forn(casito,casos)
	{
	    int n,k;
	    fin >> n >> k;
	    forn(i,n)
	    forn(j,k)
            fin >> tabla[i][j];
        forn(i,n)
        forn(j,n)
        {
            vecinos[i][j] = true;
            forn(ii,k)
            forn(jj,k)
            {
                if(tabla[i][ii]<=tabla[j][ii]&&tabla[i][jj]>=tabla[j][jj])
                    vecinos[i][j] = false;
            }
        }
        int res = 0;
        forn(i,n)
            pos[i] = 0;
        cout << "Hola";
        while(sigue(n)==true)
        {
            bool p = true;
            forn(i,n)
            {
                forn(j,n)
                {
                    if(pos[i]==1&&pos[j]==1&&vecinos[i][j]==true)
                    {
                        p=false;
                        break;
                    }
                }
                if(p==false)
                    break;
            }
            if(p==true)
            {
                res>?=count(pos,pos+n,1);
            }
        }
	    fout << "Case #" << casito+1 << ": " << res << endl;
	}
}

#include<algorithm>
#include<cmath>
#include<iomanip>
#include<map>
#include<queue>
#include<set>
#include<stack>
#include<vector>
#include<iostream>
#include<fstream>
#include<string>

using namespace std;

#define forn(i,n) for(int i = 0; i < (n); i++)
#define dforn(i,n) for(int i = (int)(n-1); i >= 0; i--)
#define all(v) v.begin(), v.end()
#define pb push_back

int tablero[102][102];
char tabl[102][102];
vector< vector<int> > vecinos;
int h,w,ww;

void bfs(int i, int j, char c)
{
    queue<int> cola;
    cola.push(i*ww+j);
    tabl[i][j] = c;
    int k;
    while(!cola.empty())
    {
        k = cola.front();
        cola.pop();
        tabl[k/ww][k%ww] = c;
        forn(i,vecinos[k].size())
        {
            if(tabl[vecinos[k][i]/ww][vecinos[k][i]%ww]=='.')
            {
                cola.push(vecinos[k][i]);
            }
        }
    }
}

int main()
{
    ifstream fin("B-large.in");
    ofstream fout("B-large.out");
    int casos;
    fin >> casos;
    forn(casitos,casos)
    {
        fin >> h >> w;
        ww = w+2;
        vecinos.clear();
        vecinos.resize((h+2)*(w+2));
        forn(i,h+2)
        {
            tablero[i][0] = 10000;
            tablero[i][w+1] = 10000;
            tabl[i][0] = '-';
            tabl[i][w+1] = '-';
        }
        forn(i,w+2)
        {
            tablero[0][i] = 10000;
            tablero[h+1][i] = 10000;
            tabl[0][i] = '-';
            tabl[h+1][i] = '-';
        }
        for(int i=1;i<=h;i++)
        for(int j=1;j<=w;j++)
        {
            tabl[i][j] = '.';
        }
        for(int i=1;i<=h;i++)
        for(int j=1;j<=w;j++)
        {
            fin >> tablero[i][j];
        }
        for(int i=1;i<=h;i++)
        for(int j=1;j<=w;j++)
        {
            int k = min(min(tablero[i-1][j],tablero[i][j-1]),min(tablero[i][j+1],tablero[i+1][j]));
            if(k>=tablero[i][j])
                continue;
            if(k==tablero[i-1][j])
            {
                vecinos[(i-1)*ww+j].push_back(i*ww+j);
                vecinos[i*ww+j].push_back((i-1)*ww+j);
            }
            else if(k==tablero[i][j-1])
            {
                vecinos[i*ww+j-1].push_back(i*ww+j);
                vecinos[i*ww+j].push_back(i*ww+j-1);
            }
            else if(k==tablero[i][j+1])
            {
                vecinos[i*ww+j+1].push_back(i*ww+j);
                vecinos[i*ww+j].push_back(i*ww+j+1);
            }
            else if(k==tablero[i+1][j])
            {
                vecinos[(i+1)*ww+j].push_back(i*ww+j);
                vecinos[i*ww+j].push_back((i+1)*ww+j);
            }
        }
        char c = 'a';
        for(int i=1;i<=h;i++)
        for(int j=1;j<=w;j++)
        {
            if(tabl[i][j] == '.')
            {
                bfs(i,j,c);
                c++;
            }
        }
        fout << "Case #" << casitos+1 << ":" << endl;
        for(int i=1;i<=h;i++)
        {
            for(int j=1;j<=w;j++)
            {
                fout << tabl[i][j];
                if(j<w)
                    fout << ' ';
            }
            fout << endl;
        }
    }
}

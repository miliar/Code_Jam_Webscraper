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
#include<sstream>

using namespace std;

#define forn(i,n) for(int i = 0; i < (n); i++)
#define dforn(i,n) for(int i = (int)(n-1); i >= 0; i--)
#define all(v) v.begin(), v.end()
#define pb push_back

int cant[500][19];

int main()
{
    ifstream fin("C-large.in");
    ofstream fout("C-large.out");
    int casos;
    string stri;
    getline(fin,stri);
    istringstream iss;
    iss.str(stri);
    iss.clear();
    iss >> casos;
    string gcj = "welcome to code jam";
    forn(casitos,casos)
    {
        int res = 0;
        string st;
        getline(fin,st);
        forn(i,st.size())
        forn(j,19)
            cant[i][j] = 0;
        dforn(i,st.size())
        {
            forn(j,19)
            {
                if(st[i] == gcj[j])
                {
                    if(j==18)
                    {
                        cant[i][j] = 1;
                    }
                    else
                    {
                        for(int k=i+1;k<st.size();k++)
                        {
                            cant[i][j] += cant[k][j+1];
                            cant[i][j] %= 10000;
                        }
                    }
                }
            }
        }
        forn(i,st.size())
            res+=cant[i][0];
        res%=10000;
        fout << "Case #" << casitos+1 << ": ";
        if(res<1000)
            fout << 0;
        if(res<100)
            fout << 0;
        if(res<10)
            fout << 0;
        fout << res << endl;
    }
}

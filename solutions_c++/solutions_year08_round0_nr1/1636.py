#include<iostream>
#include<fstream>
#include<vector>
#include<stdio.h>
#include<string>

using namespace std;

#define forn(i,n) for(i=0;i<(n);i++)

int main()
{
    int n;
    int s;
    int q;
    string inp;
    vector<string> engines;
    vector<string> querys;
    vector<int> contador;
    vector<int> res(0);
    int i,j,k,t;
    ifstream text("A-large.in");
    getline(text,inp);
    n = atoi(inp.c_str());
    while(n > 0)
    {
        getline(text,inp);
        s = atoi(inp.c_str());
        engines.resize(0);
        while(s > 0)
        {
            getline(text, inp);
            engines.push_back(inp);
            s--;
        }
        getline(text,inp);
        q = atoi(inp.c_str());
        querys.resize(0);
        while(q > 0)
        {
            getline(text, inp);
            querys.push_back(inp);
            q--;
        }
        contador.resize(engines.size());
        forn(i,engines.size())
        {
            contador[i] = 0;
        }
        k = 0;
        forn(i,querys.size())
        {
            forn(j,engines.size())
            {
                if(querys[i] == engines[j])
                {
                    contador[j] = 1;
                }
            }
            t = 1;
            forn(j,contador.size())
            {
                if(contador[j] == 0)
                {
                    t = 0;
                }
            }
            if(t == 1)
            {
                forn(j,contador.size())
                {
                    if(querys[i] != engines[j])
                    {
                        contador[j] = 0;
                    }
                }
                k++;
            }
        }
        res.push_back(k);
        n--;
    }
    ofstream resu("A-large.out");
    forn(i,res.size())
    {
        j = i+1;
        resu << "Case #" << j << ": " << res[i] << '\n';
    }
    resu.close();
}

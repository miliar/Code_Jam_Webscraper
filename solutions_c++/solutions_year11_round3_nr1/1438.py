#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <iostream>
#include <queue>
#include <algorithm>
#include <vector>
#include <stack>
using namespace std;


void print(vector<string> ar)
{
    for(int i=0;i<ar.size();i++)
            cout << ar[i] << '\n';


        cout << "-----\n";
}

bool tryar(vector<string> ar, int ni, int nj)
{
    for(int i=0;i<ni;i++)
    {
        for(int j=0;j<nj;j++)
        {
            if(ar[i][j] == '#')
            {
                if(i+1 < ni && j+1 < nj)
                {
                    if(ar[i+1][j] != '#' || ar[i+1][j+1] != '#' || ar[i][j+1] != '#')
                        return false;
                    else
                    {
                        ar[i][j] = '/';
                        ar[i+1][j] = '\\';
                        ar[i][j+1] = '\\';
                        ar[i+1][j+1] = '/';

                        print(ar);

                        return true;
                    }
                }
                else
                {
                    return false;
                }
            }
        }
    }
    return false;
}


bool isok(vector<string> ar)
{
    for(int i=0;i<ar.size();i++)
        for(int j=0;j<ar[i].size();j++)
            if(ar[i][j] == '#')
                return false;
    return true;
}

void solve(int k)
{
    vector<string> ar;
    int ni,nj; cin >> ni >> nj;
    for(int i=0;i<ni;i++)
    {
        string s; cin >> s;
        ar.push_back(s);
    }
    bool tryar = true;
    while(tryar)
    {
        tryar = false;
        for(int i=0;i<ni;i++)
        {
            for(int j=0;j<nj;j++)
            {
                if(ar[i][j] == '#')
                {
                    if(i+1 < ni && j+1 < nj)
                    {
                        if(ar[i+1][j] != '#' || ar[i+1][j+1] != '#' || ar[i][j+1] != '#')
                        {
                            tryar = false;
                            goto end;
                        }
                        else
                        {
                            ar[i][j] = '/';
                            ar[i+1][j] = '\\';
                            ar[i][j+1] = '\\';
                            ar[i+1][j+1] = '/';

                            tryar = true;
                            goto end;
                        }
                    }
                    else
                    {
                        tryar = false;
                        goto end;
                    }
                }
            }
        }
        end: ;
    }

    printf("Case #%d:\n", k);

    if(!isok(ar))
        printf("Impossible\n");
    else
    {
        for(int i=0;i<ni;i++)
            cout << ar[i] << '\n';
    }
}

int main()
{
    int n; cin >> n;
    for(int i=0;i<n;i++)
    {
        solve(i+1);
    }
    return 0;
}


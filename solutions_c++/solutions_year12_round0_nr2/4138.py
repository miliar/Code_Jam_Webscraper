#include <iostream>
#include <map>
#include <vector>
#include <string>
#include <fstream>

using namespace std;

ifstream fin("input.txt");
ofstream fout("output.txt");

int punt(int n, int s, int p, vector <int>& v)
{
    int res = 0;
    for (int i = 0; i < n; i++)
    {
        int x = (v[i] - p)/2;
        if (v[i]<p) continue;
        if ((p-x)<2) res++;
        if ((p-x)==2 and s>0) {s--; res++;}
    }
    return res;
}

int main()
{
    int t;
    fin >>t;
    
    for (int k = 0; k < t; k++)
    {
        fout <<"Case #"<<k+1<<": ";
        int n, s, p;
        fin >>n>>s>>p;
        vector <int> v(n, 0);
        for (int i = 0; i < n; i++) fin >>v[i];
        fout <<punt(n, s, p, v)<<endl;
    }
    //fin >>t;
}

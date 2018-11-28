#include <iostream>
#include <fstream>
#include <vector>

using namespace std;

int nor_add(int a, int b)
{ return a^b; }

struct CandySplit
{
    vector<int> d_candy;
};

vector<CandySplit*> g_Cases;

void read_input(char* filename)
{
    ifstream fin(filename);
    int nCases;
    fin >> nCases;
    for (int i = 0; i < nCases; ++i)
    {
        int n;
        fin >> n;
        int nTmp;
        CandySplit* cs = new CandySplit;
        for (int j = 0; j < n; ++j)
        {
            fin >> nTmp;
            cs->d_candy.push_back(nTmp);
        }
        g_Cases.push_back(cs);
    }
    fin.close();
}

bool splitCandy(const CandySplit* cs, int& maxVal)
{
    int minVal = 1e7;
    int totalValue = 0;
    for ( int i = 0; i < cs->d_candy.size(); ++i)
    {
        if (minVal > cs->d_candy[i])
            minVal = cs->d_candy[i];

        totalValue = nor_add(totalValue, cs->d_candy[i]);
        maxVal += cs->d_candy[i];
    }

    if (totalValue == 0)
    {
        maxVal -= minVal;
        return true;
    }
    else 
        return false;
}

int main()
{
    read_input("C-large.in");
    
    ofstream fout("a_large.out");
    for (int i = 0; i < g_Cases.size(); ++i)
    {
        int val = 0;
        if (splitCandy(g_Cases[i], val))
            fout << "Case #" << i+1 << ": " << val << endl;
        else
            fout << "Case #" << i+1 << ": " << "NO" << endl;
    }/**/
    //cout << nor_add(56, 56) << endl;

    return 0;
}
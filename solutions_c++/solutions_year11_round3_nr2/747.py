#include <iostream>
#include <fstream>
#include <vector>
#include <set>

using namespace std;

struct Case
{
    //int d_size;
    int d_L;
    double d_t;
    int d_N;
    int d_C;
    vector<int> d_stars;
    multiset<int> d_remain;
    int result;
};

int g_nCases;
vector<Case*> g_cases;

void read_input(char* filename)
{
    ifstream fin (filename);
    if (!fin)
    {
        cerr << "Can't open the file " << filename << endl;
        exit(-1);
    }

    fin >> g_nCases;
    for (int i = 0; i < g_nCases; ++i)
    {
        Case* cs = new Case;
        int tmp;
        fin >> cs->d_L >> cs->d_t >> cs->d_N >> cs->d_C;
        for (int j = 0; j < cs->d_C; ++j)
        {
            fin >> tmp;
            cs->d_stars.push_back(tmp);
        }
        g_cases.push_back(cs);
    }
    fin.close();
}

void solve(Case* cs)
{
    int sum = 0;
    int start = cs->d_N;
    int totalTime = 0;
    for (int i = 0; i < cs->d_N; ++i)
    {
        totalTime += cs->d_stars[i%cs->d_C]*2;
    }

    for (int i = 0; i < cs->d_N; ++i)
    {
        int val = cs->d_stars[i % cs->d_C]*2;
        if (sum + val <= cs->d_t)
        {
            sum += val;
            continue;
        }
        else
        {
            start = i+1;
            cs->d_remain.insert( val/2 - (cs->d_t - sum)/2 );
            break;
        }
    }
    for (int i = start; i < cs->d_N; ++i)
    {
        cs->d_remain.insert(cs->d_stars[i%cs->d_C]);
    }

    //
    int reducetime = 0;
    for (int i = 0; i < cs->d_L; ++i)
    {
        multiset<int>::iterator it = cs->d_remain.end();
        --it;
        reducetime += *it;
        cs->d_remain.erase(it);
        if (cs->d_remain.size()==0)
            break;
    }

    cs->result = totalTime - reducetime;
}

int main(int argc, char**argv)
{
    read_input("B-small-attempt1.in");

    ofstream fout("b_small.out");
    for (int i = 0; i < g_nCases; ++i)
    {
        fout << "Case #" << i+1 << ": " ;
        solve(g_cases[i]);
        fout << g_cases[i]->result << endl ;
    }
    fout.close();
    return 0;
}
#include <iostream>
#include <fstream>
#include <vector>
#include <set>

using namespace std;

struct Case
{
    int d_size;
    int d_h;
    int d_l;
    set<int> d_player;
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
        fin >> cs->d_size >> cs->d_l >> cs->d_h;
        for (int j = 0; j < cs->d_size; ++j)
        {
            fin >> tmp;
            cs->d_player.insert(tmp);
        }
        g_cases.push_back(cs);
    }
    fin.close();
}

bool solve (Case* cs)
{
    for (int i = cs->d_l; i <= cs->d_h; ++i)
    {
        bool ret = true;
        for (set<int>::iterator it = cs->d_player.begin(); it != cs->d_player.end(); ++it)
        {
            if (*it>i)
            {
                if ((*it)%i != 0)
                {
                    ret = false;
                    break;
                }
            }
            else
            {
                if (i%(*it) != 0)
                {
                    ret = false;
                    break;
                }
            }
        }
        if (ret)
        {
            cs->result = i;
            return true;
        }
    }

    return false;
}

int main(int argc, char**argv)
{
    read_input("C-small-attempt0.in");

    ofstream fout("c_small.out");
    for (int i = 0; i < g_nCases; ++i)
    {
        fout << "Case #" << i+1 << ": " ;
        if (solve(g_cases[i]))
            fout << g_cases[i]->result << endl;
        else
            fout << "NO" << endl;
        //<< minSteps << endl;
    }
    fout.close();
    return 0;
}
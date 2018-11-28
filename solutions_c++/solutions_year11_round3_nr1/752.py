#include <iostream>
#include <fstream>
#include <vector>

using namespace std;

struct Case
{
    //int d_size;
    int d_height;
    int d_width;
    char** d_data;
};

int g_nCases;
vector<Case*> g_cases;

bool solve (Case* cs)
{
    bool ret = true;
    for (int i = 0; i < cs->d_height; ++i)
    {
        for (int j = 0; j < cs->d_width; ++j)
        {
            if (cs->d_data[i][j]=='#')
            {
                if (j >= cs->d_width-1 || i >= cs->d_height-1)
                {
                    ret = false;
                    break;
                }
                if (cs->d_data[i][j+1] == '#' && cs->d_data[i+1][j] == '#' && cs->d_data[i+1][j+1] == '#')
                {
                    cs->d_data[i][j] = '/';
                    cs->d_data[i+1][j] = '\\';
                    cs->d_data[i][j+1] = '\\';
                    cs->d_data[i+1][j+1] = '/';
                }
                else
                {
                    ret = false;
                    break;
                }
            }
        }
        if (ret == false)
            break;
    }
    return ret;
}

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
        char ch;
        Case* cs = new Case;
        fin >> cs->d_height >> cs->d_width;
        cs->d_data = new char*[cs->d_height];
        for (int j = 0; j < cs->d_height; ++j)
        {
            cs->d_data[j] = new char[cs->d_width];
            for (int k = 0; k < cs->d_width; ++k)
            {
                fin >> cs->d_data[j][k];
            }
        }
        g_cases.push_back(cs);
    }
    fin.close();
}

int main(int argc, char**argv)
{
    read_input("A-large.in");

    ofstream fout("a_large.out");
    for (int i = 0; i < g_nCases; ++i)
    {
        fout << "Case #" << i+1 << ":" <<endl ;
        if (solve(g_cases[i]))
        {
            for (int j = 0; j < g_cases[i]->d_height; ++j)
            {
                for (int k = 0; k < g_cases[i]->d_width; ++k)
                {
                    fout << g_cases[i]->d_data[j][k];
                }
                fout <<endl;
            }
        }
        else
            fout << "Impossible" << endl;
        //int minSteps = calMinSteps(g_BScases[i]);
        //<< minSteps << endl;
    }
    fout.close();
    return 0;
}
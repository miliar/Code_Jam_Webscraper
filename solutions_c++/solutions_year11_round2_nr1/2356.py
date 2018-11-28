#include <iostream>
#include <fstream>
#include <vector>

using namespace std;

struct Matches
{
    int d_size;
    char** d_mat;
    double WP (int cur)
    {
        int win = 0;
        int loss = 0;
        for (int i = 0; i < d_size; ++i)
        {
            if (d_mat[cur][i] == 1)
                ++win;
            if (d_mat[cur][i] == 0)
                ++loss;
        }
        return (double)win/ (double)(win+loss);
    }
    double WP (int cur, int tar)
    {
        int win = 0;
        int loss = 0;
        for (int i = 0; i < d_size; ++i)
        {
            if (i==tar)
                continue;
            if (d_mat[cur][i] == 1)
                ++win;
            if (d_mat[cur][i] == 0)
                ++loss;
        }
        return (double)win/ (double)(win+loss);
    }
    double OWP (int cur)
    {
        double avg = 0;
        int n = 0;
        for (int i = 0; i < d_size; ++i)
        {
            if (d_mat[cur][i] != 2)
            {
                avg += WP(i, cur);
                n++;
            }
        }
        return avg/n;
    }
    double OOWP (int cur)
    {
        double avg = 0;
        int n = 0;
        for (int i = 0; i < d_size; ++i)
        {
            if (d_mat[cur][i] != 2)
            {
                avg += OWP(i);
                n++;
            }
        }
        return avg/(double)n;
    }
    double RPI (int cur)
    {
        /*for (int i = 0; i < d_size; ++ i)
        {
            cout << WP(i) << endl;
        }*/
        return 0.25*WP(cur) + 0.50*OWP(cur) + 0.25*OOWP(cur);
    }
};

int g_nCases;
vector<Matches*> g_cases;


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
        int nTeam;
        fin >> nTeam;
        Matches* mt = new Matches;
        mt->d_mat = new char*[nTeam];
        mt->d_size = nTeam;
        for (int j = 0; j < nTeam; ++j)
        {
            char ch;
            mt->d_mat[j] = new char[nTeam];
            for (int k = 0; k < nTeam; ++k)
            {
                fin >> ch;
                if (ch == '0')
                    mt->d_mat[j][k] = 0;
                else if (ch == '1')
                    mt->d_mat[j][k] = 1;
                else
                    mt->d_mat[j][k] = 2;
            }
        }
        g_cases.push_back(mt);
    }
    fin.close();
}

int main(int argc, char**argv)
{
    read_input("A-small-attempt0.in");

    ofstream fout("a_small.out");
    for (int i = 0; i < g_nCases; ++i)
    {
        fout << "Case #" << i+1 << ":" <<endl ;
        for (int j = 0; j < g_cases[i]->d_size; ++j)
        {
            fout << g_cases[i]->RPI(j) << endl;
            /*cout << g_cases[i]->WP(j) << endl;*/
            //cout << g_cases[i]->OWP(j) << endl;
            //cout << g_cases[i]->OOWP(j) << endl;
        }
        //int minSteps = calMinSteps(g_BScases[i]);
        //<< minSteps << endl;
    }
    fout.close();
    return 0;
}
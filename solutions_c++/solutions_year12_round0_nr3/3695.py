#include <iostream>
#include <fstream>
#include <vector>
#include <string>
#include <math.h>

using namespace std;

struct JamCase
{
    int A;
    int B;
    int recycle(int num)
    {
        vector<int> pa;
        int nDigi = log((double)num)/log(10.0)+1;
        int temp = num;
        for (int i = 1; i < nDigi; ++i)
        {
            int remainder = temp%10;
            temp = temp/10 + remainder*pow(10.0,nDigi-1);
            if (temp <= B && temp > num)
            {
                bool exist = false;
                for (int j = 0; j < pa.size(); ++j)
                {
                    if (pa[j] == temp)
                    {
                        exist = true;
                        break;
                    }
                }
                if (!exist)
                    pa.push_back(temp);
            }
        }
        return pa.size();
    }
    int output()
    {
        int tot = 0;
        for (int i = A; i <= B; ++i)
            tot += recycle(i);
        return tot;
    }
};

int g_nCases;
vector<JamCase*> g_cases;

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
        JamCase* s = new JamCase;
        fin >> s->A;
        fin >> s->B;
        g_cases.push_back(s);
    }
    fin.close();
}

int main(int argc, char**argv)
{
    read_input("C-large.in");

    ofstream fout("c_large.out");
    for (int i = 0; i < g_nCases; ++i)
    {
        /*cout << g_cases[i]->A << ' ' << g_cases[i]->B << endl;
        fout << g_cases[i]->output() << endl;*/
        fout << "Case #" << i+1 << ": " ;
        fout << g_cases[i]->output() << endl;
        //fout << g_cases[i]->output << endl;
        //for (int j = 0; j < g_cases[i]->d_size; ++j)
        //{
        //    fout << g_cases[i]->RPI(j) << endl;
        //    /*cout << g_cases[i]->WP(j) << endl;*/
        //    //cout << g_cases[i]->OWP(j) << endl;
        //    //cout << g_cases[i]->OOWP(j) << endl;
        //}
        //int minSteps = calMinSteps(g_BScases[i]);
        //<< minSteps << endl;
    }
    fout.close();
    return 0;
}
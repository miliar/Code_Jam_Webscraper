#include <iostream>
#include <fstream>
#include <vector>
#include <string>

using namespace std;

//char rep[27] = "ynficwlbkuomxsevzpdrjgthaq";
char rep[27] = "yhesocvxduiglbkrztnwjpfmaq";


struct GString
{
    string input;
    string output;
    void genOutput()
    {
        for (int i = 0; i < input.size(); ++i)
        {
            if (input[i] == ' ')
                output += ' ';
            else
                output += rep[input[i]-'a'];
        }
    }
};

int g_nCases;
vector<GString*> g_cases;

void read_input(char* filename)
{
    ifstream fin (filename);
    if (!fin)
    {
        cerr << "Can't open the file " << filename << endl;
        exit(-1);
    }

    fin >> g_nCases;
    string s;
    getline(fin, s); // pass '/n'
    for (int i = 0; i < g_nCases; ++i)
    {
        GString* s = new GString;
        getline(fin, s->input);
        g_cases.push_back(s);
    }
    fin.close();
}

int main(int argc, char**argv)
{
    read_input("A-small-attempt0.in");

    ofstream fout("a_small.out");
    for (int i = 0; i < g_nCases; ++i)
    {
        g_cases[i]->genOutput();
        //cout << g_cases[i]->output << endl;
        fout << "Case #" << i+1 << ": " ;
        fout << g_cases[i]->output << endl;
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